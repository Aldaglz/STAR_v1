import sys
import os
import math
import time
import threading
from pathlib import Path

from guinew import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QThread, Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow

import cv2
import mediapipe as mp
import serial

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Modelo" / "Data"
LBPH_MODEL_PATH = BASE_DIR / "modelito2LBPH.xml"
if not LBPH_MODEL_PATH.exists():
    alt = BASE_DIR / "Modelo" / "modelito2LBPH.xml"
    if alt.exists():
        LBPH_MODEL_PATH = alt

CAMERA_INDEX = 0
IDLE_SLEEP = 0.002

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


class LatestFrameBuffer:
    """Conserva solo el frame mas reciente para evitar atraso acumulado."""
    def __init__(self):
        self.lock = threading.Lock()
        self.frame = None
        self.frame_id = 0

    def publish(self, frame):
        with self.lock:
            self.frame = frame
            self.frame_id += 1

    def get_if_new(self, last_id):
        with self.lock:
            if self.frame is None or self.frame_id == last_id:
                return None, last_id
            return self.frame, self.frame_id


class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        self.ui.Top_frame.mouseMoveEvent = self.mover_ventana

        self.ui.btn_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page))
        self.ui.btn_Streaming.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Streaming_page))

        self.ui.btn_maximizar.clicked.connect(self.control_btn_maximizar)
        self.ui.btn_minimizar.clicked.connect(self.control_btn_minimizar)
        self.ui.btn_restaurar.clicked.connect(self.control_btn_restaurar)
        self.ui.btn_cerrar.clicked.connect(self.close)
        self.ui.btn_restaurar.hide()
        self.ui.btn_menu.clicked.connect(self.mover_menu)

        self.Streaming = None
        self.ui.btn_TurnOn.clicked.connect(self.start_video)
        self.ui.btn_TurnOff.clicked.connect(self.cancel)

        # Igual que tu version original: arranca al abrir.
        self.start_video()

    def start_video(self):
        # Evita abrir /dev/video0 dos veces.
        if self.Streaming is not None and self.Streaming.isRunning():
            print("La captura ya esta ejecutandose.")
            return

        self.Streaming = Streaming()
        self.Streaming.ImageEmotion.connect(self.Imageupd_slot_Emotions)
        self.Streaming.ImageSkeleton.connect(self.Imageupd_slot_Skeleton)

        self.Streaming.Shoulder_Right.connect(self.Angulo_Shoulder_Derecho)
        self.Streaming.Shoulder_Left.connect(self.Angulo_Shoulder_izquierdo)
        self.Streaming.Elbow_Right.connect(self.Angulo_Elbow_Derecho)
        self.Streaming.Elbow_Left.connect(self.Angulo_Elbow_izquierdo)
        self.Streaming.Wrist_Right.connect(self.Angulo_Wrist_Derecho)
        self.Streaming.Wrist_Left.connect(self.Angulo_Wrist_izquierdo)
        self.Streaming.Cuello.connect(self.Angulo_Cuello)
        self.Streaming.Expresion.connect(self.Expresion)
        self.Streaming.premio.connect(self.games)

        print("Iniciando captura de video...")
        self.Streaming.start()

    def Angulo_Shoulder_Derecho(self, v):
        self.Shoulder_Right = v
        trama = bytes("S" + str(int(v)) + "\n", "utf-8")
        # self.serial.enviar_datos(trama)

    def Angulo_Shoulder_izquierdo(self, v):
        self.Shoulder_Left = v
        trama = bytes("s" + str(int(v)) + "\n", "utf-8")
        # self.serial.enviar_datos(trama)

    def Angulo_Elbow_Derecho(self, v):
        self.Elbow_Right = v
        trama = bytes("E" + str(int(abs(v - 180))) + "\n", "utf-8")
        self.ui.lb_RSA.setText(str(int(v)) + "°")

    def Angulo_Elbow_izquierdo(self, v):
        self.Elbow_Left = v
        trama = bytes("e" + str(int(abs(v - 180))) + "\n", "utf-8")
        self.ui.lb_LSA.setText(str(int(v)) + "°")

    def Angulo_Wrist_Derecho(self, v):
        self.Wrist_Right = v
        trama = bytes("W" + str(abs(int(v - 90))) + "\n", "utf-8")
        self.ui.lb_RAA.setText(str(int(v)) + "°")

    def Angulo_Wrist_izquierdo(self, v):
        self.Wrist_Left = v
        trama = bytes("w" + str(abs(int(v - 90))) + "\n", "utf-8")
        self.ui.lb_LAA.setText(str(int(v)) + "°")

    def Angulo_Cuello(self, v):
        self.Cuello = v
        trama = bytes("N" + str(int(v)) + "\n", "utf-8")

    def Expresion(self, v):
        trama = bytes("G" + str(v) + "\n", "utf-8")

    def games(self, premio):
        if premio == 1:
            self.ui.lb_Exercise.setText("Levantaste el brazo izquierdo")
        elif premio == 2:
            self.ui.lb_Exercise.setText("Levantaste el brazo derecho")
        elif premio == 3:
            self.ui.lb_Exercise.setText("Levantaste los dos brazos")

    def Imageupd_slot_Emotions(self, image):
        self.ui.lb_Emotion.setPixmap(QPixmap.fromImage(image))

    def Imageupd_slot_Skeleton(self, image):
        self.ui.lb_Skeleton.setPixmap(QPixmap.fromImage(image))

    def cancel(self, *args):
        self.ui.lb_Skeleton.clear()
        self.ui.lb_Emotion.clear()
        if self.Streaming is not None and self.Streaming.isRunning():
            print("Deteniendo captura de video...")
            self.Streaming.stop()
            self.Streaming.wait(3000)

    def control_btn_minimizar(self):
        self.showMinimized()

    def control_btn_restaurar(self):
        self.showNormal()
        self.ui.btn_restaurar.hide()
        self.ui.btn_maximizar.show()

    def control_btn_maximizar(self):
        self.showMaximized()
        self.ui.btn_maximizar.hide()
        self.ui.btn_restaurar.show()

    def mover_menu(self):
        width = self.ui.Lateral_frame.width()
        extender = 200 if width == 0 else 0
        self.animacion = QPropertyAnimation(self.ui.Lateral_frame, b"minimumWidth")
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if not self.isMaximized() and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()

    def closeEvent(self, event):
        if self.Streaming is not None and self.Streaming.isRunning():
            self.Streaming.stop()
            self.Streaming.wait(3000)
        event.accept()


class Streaming(QThread):
    """
    Arquitectura:

        Captura -> buffer de ultimo frame
                    |              |
                    v              v
               Pose worker    Face/LBPH worker
                    |              |
                    +------ GUI ---+

    Pose y LBPH ya NO esperan uno por el otro.
    """
    ImageEmotion = pyqtSignal(QImage)
    ImageSkeleton = pyqtSignal(QImage)

    Shoulder_Right = pyqtSignal(int)
    Shoulder_Left = pyqtSignal(int)
    Elbow_Right = pyqtSignal(int)
    Elbow_Left = pyqtSignal(int)
    Wrist_Right = pyqtSignal(int)
    Wrist_Left = pyqtSignal(int)
    Cuello = pyqtSignal(int)

    Expresion = pyqtSignal(int)
    premio = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.hilo_corriendo = False
        self.frames = LatestFrameBuffer()
        self.pose_thread = None
        self.face_thread = None

    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(CAMERA_INDEX)

        if not cap.isOpened():
            print("ERROR: no se pudo abrir la camara.")
            self.hilo_corriendo = False
            return

        self.pose_thread = threading.Thread(target=self._pose_worker, daemon=True)
        self.face_thread = threading.Thread(target=self._face_worker, daemon=True)
        self.pose_thread.start()
        self.face_thread.start()

        try:
            while self.hilo_corriendo:
                ret, frame = cap.read()
                if ret:
                    self.frames.publish(frame)
                else:
                    time.sleep(0.01)
                time.sleep(IDLE_SLEEP)
        finally:
            self.hilo_corriendo = False
            cap.release()
            if self.pose_thread is not None:
                self.pose_thread.join(timeout=2.0)
            if self.face_thread is not None:
                self.face_thread.join(timeout=2.0)
            print("Captura finalizada.")

    def _face_worker(self):
        try:
            image_paths = os.listdir(DATA_PATH)
            print("imagePaths=", image_paths)
        except Exception as exc:
            print("ERROR leyendo Modelo/Data:", exc)
            return

        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
        except AttributeError:
            print("ERROR: falta cv2.face. Instala opencv-contrib-python.")
            return

        try:
            recognizer.read(str(LBPH_MODEL_PATH))
        except Exception as exc:
            print("ERROR cargando modelo LBPH:", exc)
            return

        face_classifier = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        last_id = -1
        count = 0
        fps_start = time.perf_counter()

        while self.hilo_corriendo:
            frame, frame_id = self.frames.get_if_new(last_id)
            if frame is None:
                time.sleep(IDLE_SLEEP)
                continue
            last_id = frame_id

            t0 = time.perf_counter()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            output = frame.copy()
            expression_value = None

            for (x, y, w, h) in faces:
                rostro = gray[y:y+h, x:x+w]
                rostro = cv2.resize(rostro, (48, 48), interpolation=cv2.INTER_CUBIC)
                result = recognizer.predict(rostro)

                if result[1] < 170:
                    label = image_paths[result[0]] if result[0] < len(image_paths) else "unknown"
                    cv2.putText(output, label, (x, y-25), 2, 1.1, (0, 0, 255), 3, cv2.LINE_AA)
                    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    if label == "happy":
                        expression_value = 1
                    elif label == "angry":
                        expression_value = 2
                else:
                    cv2.putText(output, "Desconocido", (x, y-20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if expression_value is not None:
                self.Expresion.emit(expression_value)

            output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
            elapsed_ms = (time.perf_counter() - t0) * 1000
            cv2.putText(output, f"FACE/LBPH {elapsed_ms:.0f} ms", (10, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255), 1, cv2.LINE_AA)
            self.ImageEmotion.emit(self._to_qimage(output))

            count += 1
            now = time.perf_counter()
            if now - fps_start >= 2.0:
                fps = count / (now - fps_start)
                print(f"[FACE/LBPH] {fps:.2f} FPS | {elapsed_ms:.1f} ms")
                count = 0
                fps_start = now

    def _pose_worker(self):
        last_id = -1
        count = 0
        fps_start = time.perf_counter()

        try:
            with mp_pose.Pose(
                static_image_mode=False,
                model_complexity=1,
                smooth_landmarks=True,
                enable_segmentation=False
            ) as pose:
                while self.hilo_corriendo:
                    frame, frame_id = self.frames.get_if_new(last_id)
                    if frame is None:
                        time.sleep(IDLE_SLEEP)
                        continue
                    last_id = frame_id

                    t0 = time.perf_counter()
                    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    flip = cv2.flip(rgb, 1)
                    flip.flags.writeable = False
                    results = pose.process(flip)
                    flip.flags.writeable = True

                    if results.pose_landmarks is not None:
                        self._process_pose(results, flip)

                    elapsed_ms = (time.perf_counter() - t0) * 1000
                    cv2.putText(flip, f"POSE {elapsed_ms:.0f} ms", (10, 25),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255,255,255), 1, cv2.LINE_AA)
                    self.ImageSkeleton.emit(self._to_qimage(flip))

                    count += 1
                    now = time.perf_counter()
                    if now - fps_start >= 2.0:
                        fps = count / (now - fps_start)
                        print(f"[POSE] {fps:.2f} FPS | {elapsed_ms:.1f} ms")
                        count = 0
                        fps_start = now
        except Exception as exc:
            print("ERROR en MediaPipe Pose:", exc)

    def _process_pose(self, results, flip):
        lm = results.pose_landmarks.landmark
        world = results.pose_world_landmarks
        height, width = flip.shape[:2]

        nariz_x = int(lm[0].x * width)
        R_ear_x = int(lm[7].x * width)
        L_ear_x = int(lm[8].x * width)

        R_Shou_x, R_Sho_y = int(lm[12].x * width), int(lm[12].y * height)
        L_Shou_x, L_Sho_y = int(lm[11].x * width), int(lm[11].y * height)
        R_Elb_x, R_Elb_y = int(lm[14].x * width), int(lm[14].y * height)
        L_Elb_x, L_Elb_y = int(lm[13].x * width), int(lm[13].y * height)
        R_Wri_x, R_Wri_y = int(lm[16].x * width), int(lm[16].y * height)
        L_Wri_x, L_Wri_y = int(lm[15].x * width), int(lm[15].y * height)

        angHombroIzq = 90.0
        angHombroDer = 90.0
        angleBrazoIzq = 90.0
        angleBrazoDer = 90.0

        def pendiente(y2, y1, x2, x1):
            return (y2-y1)/(x2-x1)

        def codo(m1, m2):
            den = 1 + m1*m2
            if abs(den) < 1e-9:
                return 90.0
            return math.degrees(math.atan((m2-m1)/den))

        try:
            m1 = pendiente(R_Wri_y, R_Elb_y, R_Wri_x, R_Elb_x)
            m2 = pendiente(R_Elb_y, R_Sho_y, R_Elb_x, R_Shou_x)
            m3 = pendiente(L_Wri_y, L_Elb_y, L_Wri_x, L_Elb_x)
            m4 = pendiente(L_Elb_y, L_Sho_y, L_Elb_x, L_Shou_x)

            angHombroIzq = abs(math.degrees(math.atan((L_Sho_y-L_Elb_y)/(L_Shou_x-L_Elb_x))) + 90)
            angleBrazoIzq = codo(m1, m2)
            angHombroDer = abs(math.degrees(math.atan((R_Sho_y-R_Elb_y)/(R_Shou_x-R_Elb_x))) + 90)
            angleBrazoDer = codo(m3, m4)
        except ZeroDivisionError:
            pass

        if nariz_x > R_ear_x:
            angulo_cuello = 140
        elif nariz_x < L_ear_x:
            angulo_cuello = 50
        else:
            angulo_cuello = 90

        if world is not None:
            # Mucho mas barato y robusto que str(landmark).split(...)
            r_z = abs(world.landmark[14].z * 100)
            l_z = abs(world.landmark[13].z * 100)
            if r_z > 22:
                angHombroDer = 0
                angleBrazoIzq = 0
            if l_z > 22:
                angHombroIzq = 180
                angleBrazoDer = 0

        mp_drawing.draw_landmarks(
            flip,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(128,0,250), thickness=5, circle_radius=3),
            mp_drawing.DrawingSpec(color=(255,255,0), thickness=10)
        )

        # Se conserva el mapeo de señales de tu codigo original.
        self.Elbow_Left.emit(int(angHombroIzq))
        self.Elbow_Right.emit(int(angHombroDer))
        self.Wrist_Right.emit(int(angleBrazoIzq))
        self.Wrist_Left.emit(int(angleBrazoDer))
        self.Cuello.emit(int(angulo_cuello))

        if angHombroDer > 150:
            self.premio.emit(1)
        if angHombroIzq < 30:
            self.premio.emit(2)

    @staticmethod
    def _to_qimage(rgb):
        h, w, ch = rgb.shape
        return QImage(rgb.data, w, h, ch*w, QImage.Format_RGB888).copy()

    def stop(self):
        self.hilo_corriendo = False
        self.requestInterruption()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
