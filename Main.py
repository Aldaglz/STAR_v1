import sys
#Libreria de la GUI
from guinew import *

#Libreria necesarias para el funcionamiento de los componentes visuales
from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, QThread, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#Librerias para la toma y manipulación de los frames
import cv2
import mediapipe as mp
import numpy as np
import os
import math
import time
import threading

#Variable configurada inicialmente
video_running = False

#Librerias para la comunicación con el Arduino Nano
import serial
#from Comunicacion_Serial import Comunicacion #Es necesario daptar esta

#Creaciones de las soluciones para dibujar sobre los frames y obtener la pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
mpDibujo = mp.solutions.drawing_utils
ConfDibu = mpDibujo.DrawingSpec(thickness=1, circle_radius=1)

#Variables necesarias para la toma de angulos
degrees=math.degrees
acos=math.acos


class MiApp(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#eliminar barra y de titulo - opacidad
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setWindowOpacity(1)

		#SizeGrip
		self.gripSize = 10
		self.grip = QtWidgets.QSizeGrip(self)
		self.grip.resize(self.gripSize, self.gripSize)

		#Mover ventana
		self.ui.Top_frame.mouseMoveEvent = self.mover_ventana

		#Acceder a las paginas
		self.ui.btn_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page))
		self.ui.btn_Streaming.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Streaming_page))

		#control barra de titulos
		self.ui.btn_maximizar.clicked.connect(self.control_btn_maximizar)
		self.ui.btn_minimizar.clicked.connect(self.control_btn_minimizar)
		self.ui.btn_restaurar.clicked.connect(self.control_btn_restaurar)
		self.ui.btn_cerrar.clicked.connect(lambda: self.close())

		self.ui.btn_restaurar.hide()

		#menu lateral
		self.ui.btn_menu.clicked.connect(self.mover_menu)
		
        #switches buttons
		self.ui.btn_TurnOn.clicked.connect(self.start_video)
		self.ui.btn_TurnOff.clicked.connect(self.cancel)
		self.start_video()
			

	

	def start_video(self):
		global video_running
		
        #Se iguala a los valores de la clase Streaming
		self.Streaming = Streaming()
		
        #Se conectan con las imagenes generadas
		self.Streaming.ImageEmotion.connect(self.Imageupd_slot_Emotions)
		self.Streaming.ImageSkeleton.connect(self.Imageupd_slot_Skeleton)

        #Se conectan con los angulos tomados
		self.Streaming.Shoulder_Right.connect(self.Angulo_Shoulder_Derecho)
		self.Streaming.Shoulder_Left.connect(self.Angulo_Shoulder_izquierdo)
		self.Streaming.Elbow_Right.connect(self.Angulo_Elbow_Derecho)
		self.Streaming.Elbow_Left.connect(self.Angulo_Elbow_izquierdo)
		self.Streaming.Wrist_Right.connect(self.Angulo_Wrist_Derecho)
		self.Streaming.Wrist_Left.connect(self.Angulo_Wrist_izquierdo)
		self.Streaming.Cuello.connect(self.Angulo_Cuello)			
        
        #Pantalla LCD
		self.Streaming.Expresion.connect(self.Expresion)
		
        #Inicia la captura
		
		print("Iniciando captura de video...")
		self.Streaming.start()
		
    #Funciones para enviar los datos a cada articulacion del cuerpo 

	def Angulo_Shoulder_Derecho(self,Shoulder_Right):#LISTO
		self.Shoulder_Right=Shoulder_Right
		trama=bytes(('S'+str((int(Shoulder_Right)))+"\n"), "utf-8")
		#self.serial.enviar_datos(trama)

	def Angulo_Shoulder_izquierdo(self,Shoulder_Left):
		self.Shoulder_Left=Shoulder_Left
		trama=bytes(('s'+str((int(Shoulder_Left)))+"\n"), "utf-8")
		#self.serial.enviar_datos(trama)

	def Angulo_Elbow_Derecho(self,Elbow_Right): #LISTO
		self.Elbow_Right=Elbow_Right
		trama=bytes(('E'+str((int(abs(Elbow_Right-180))))+"\n"), "utf-8")
		self.ui.lb_RSA.setText(str((int(Elbow_Right)))+"°")
		#self.serial.enviar_datos(trama)

	def Angulo_Elbow_izquierdo(self,Elbow_Left): #LISTO
		self.Elbow_Left=Elbow_Left
		trama=bytes(('e'+str((int(abs(Elbow_Left-180))))+"\n"), "utf-8")
		self.ui.lb_LSA.setText(str((int(Elbow_Left)))+"°")
		#self.serial.enviar_datos(trama)

	def Angulo_Wrist_Derecho(self,Wrist_Right): #LISTO
		self.Wrist_Right=Wrist_Right
		trama=bytes(('W'+str(abs(int(Wrist_Right-90)))+"\n"), "utf-8")
		self.ui.lb_RAA.setText(str((int(Wrist_Right)))+"°")
		#self.serial.enviar_datos(trama)

	def Angulo_Wrist_izquierdo(self,Wrist_Left):#LISTO
		self.Wrist_Left=Wrist_Left
		trama=bytes(('w'+str(abs(int(Wrist_Left-90)))+"\n"), "utf-8")
		self.ui.lb_LAA.setText(str((int(Wrist_Left)))+"°")
		#self.serial.enviar_datos(trama)

	def Angulo_Cuello(self,Cuello):
		self.Cuello=Cuello
		trama=bytes(('N'+str((int(Cuello)))+"\n"), "utf-8")
		#self.serial.enviar_datos(trama)

	#Funcion q manda la cara al LCD

	def Expresion(self,Expresion):
		trama=bytes('G'+(str(Expresion)+"\n"), "utf-8")
		#self.serial.enviar_datos(trama)
		
	def games(self,premio):
		if(premio==1):
			self.ui.lb_Exercise.setText("Levantaste el brazo izquierdo")
		elif(premio==2):
			self.ui.lb_Exercise.setText("Levantaste el brazo derecho")
		elif(premio==3):
			self.ui.lb_Exercise.setText("Levantaste los dos brazos")
		


	#Funcion que coloca las imagenes generadas del hilo en el label
	def Imageupd_slot_Emotions(self, ImageEmotion):
		self.ui.lb_Emotion.setPixmap(QPixmap.fromImage(ImageEmotion))

	def Imageupd_slot_Skeleton(self, ImageSkeleton):
		self.ui.lb_Skeleton.setPixmap(QPixmap.fromImage(ImageSkeleton))
		
	
	def cancel(self, Image):
		self.ui.lb_Skeleton.clear()
		self.ui.lb_Emotion.clear()	
		print("Deteniendo captura de video...")
		self.Streaming.stop()
			
			



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
		if True:
			width = self.ui.Lateral_frame.width()
			normal = 0
			if width==0:
				extender = 200
			else: 
				extender= normal
			self.animacion=QPropertyAnimation(self.ui.Lateral_frame, b'minimumWidth')
			self.animacion.setDuration(300)
			self.animacion.setStartValue(width)
			self.animacion.setEndValue(extender)
			self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animacion.start()
			

 	##SizeGrip
	def resizeEvent(self, event):
		rect = self.rect()
		self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)


	##Mover ventana
	def mousePressEvent(self, event):
		self.clickPosition=event.globalPos()

	def mover_ventana(self, event):
		if self.isMaximized()==False:
			if event.buttons() == Qt.LeftButton:
				self.move(self.pos()+event.globalPos()-self.clickPosition)
				self.clickPosition =event.globalPos()
				event.accept()

		if event.globalPos().y() <=20:
			self.showMaximized()
		else:
			self.showNormal()

	'''server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	port=1
	server_socket.bind(("",port))
	server_socket.listen(1)

	print("Esperando conexion Bluetooth...")
	client_socket, addres =server_socket.accept()
	print(f"Conectado a {addres}")

	try:
		while True:
			data = client_socket.recv(1024)
			command = data.decode("utf-8").strip()

			if command == "START_VIDEO":
				start_video()
			elif command == "CANCEL":
				cancel()
			elif command == "EXIT":
				break
	finally:
		client_socket.close()
		server_socket.close()'''
			

class Streaming(QThread):
	#Señales Visuales
	ImageEmotion = pyqtSignal(QImage)
	ImageSkeleton = pyqtSignal(QImage)

	#Angulos Pa' Mandar al Arduino
	Shoulder_Right= pyqtSignal(int)
	Shoulder_Left= pyqtSignal(int)
	Elbow_Right= pyqtSignal(int)
	Elbow_Left= pyqtSignal(int)
	Wrist_Right= pyqtSignal(int)
	Wrist_Left= pyqtSignal(int)
	Cuello= pyqtSignal(int)

	#Emociones
	Expresion= pyqtSignal(int)
	
	#Games
	premio=pyqtSignal(int)

	
	def run(self):
		
		dataPath="/home/_alda-03_/Desktop/CVzone/Modelo/Data"
		imagePaths = os.listdir(dataPath)
		print('imagePaths=',imagePaths)

		method='LBPH'
		if method=='LBPH': emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

		emotion_recognizer.read("/home/_alda-03_/Desktop/CVzone/Modelo/modelito2LBPH.xml")
		
		self.hilo_corriendo = True
		cap=cv2.VideoCapture(0)
		prev_time = time.time()
		faceClassif =cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
		with mp_pose.Pose(static_image_mode=False) as pose:
			while self.hilo_corriendo:
				bd =[0,0,0]

				ret,frame = cap.read()
				if ret:
					current_time = time.time()
					fps = 1 / (current_time - prev_time)
					prev_time = current_time
					gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
					auxFrame=gray.copy() #Una copia del frame

					Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
					flip = cv2.flip(Image, 1)
					cv2.putText(flip,f"FPS: {fps:.1f}",(20, 40),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)

					
					#----------------------------------------------------PARTE DE RECONOCIMIENTO DE EMOCIONES----------------------------------------
					t_face_inicio = time.perf_counter()
					faces = faceClassif.detectMultiScale(gray,1.3,5)
					t_face_fin = time.perf_counter()
					print(f"Face detect: {(t_face_fin - t_face_inicio) * 1000:.2f} ms")

					for (x,y,w,h) in faces:
						rostro=auxFrame[y:y+h,x:x+w]
						rostro = cv2.resize(rostro,(48,48),interpolation=cv2.INTER_CUBIC)	
						t_lbph_inicio = time.perf_counter()
						result = emotion_recognizer.predict(rostro)
						t_lbph_fin = time.perf_counter()
						print(f"LBPH: {(t_lbph_fin - t_lbph_inicio) * 1000:.2f} ms")
						
						cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
								
						if method == 'LBPH':
							#LBPH
							if result[1] < 170:
								cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,0,255),5,cv2.LINE_AA)
								cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)								
								if imagePaths[result[0]]=='happy':
									bd[2]=1
								elif imagePaths[result[0]]=='angry':
									bd[2]=2
							else:
								cv2.putText(frame,"Desconocido",(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
								cv2.rectangle(frame,(x,y),(x+w,y +h),(0,255,0),2)
			
					frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
					convertir_QTEmo = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
					bd[0]=1
					
                    #--------------------------------------------------PARTE DE DIAGRAMADO DE ESQUELETO--------------------------------------------
					t_pose_inicio = time.perf_counter()
					results=pose.process(flip)
					t_pose_fin = time.perf_counter()
					print(f"Pose: {(t_pose_fin - t_pose_inicio) * 1000:.2f} ms")
					
					if results.pose_world_landmarks is not None:

						#--------------------------------------PUNTOS DEL CUERPO:

						#Nota:Estos valores son tomados del tamañno de la ventana al full size (EJECUTAR VIDEO EN FULL SIZE)
						#width=723
						#height=631
						
						#Nota:Estos valores son tomados del tamañno de la ventana al promedio de reproduccion (EJECUTAR VIDEO ASI COMO ESTA; NO AGRADAR PANTALLA)
						width=640
						height=480

						#Nota: La nt da igual Xdddd


						#1___Nariz:
						nariz_x = int(results.pose_world_landmarks.landmark[0].x * width)
						nariz_y = int(results.pose_world_landmarks.landmark[0].y * height)
						
						#2___Oido Derecho:
						R_ear_x = int(results.pose_world_landmarks.landmark[7].x * width)
						R_ear_y = int(results.pose_world_landmarks.landmark[7].y * height)

						#3___Oido Izquierdo:
						L_ear_x = int(results.pose_world_landmarks.landmark[8].x * width)
						L_ear_y = int(results.pose_world_landmarks.landmark[8].y * height)

						#4___Hombro derecho:
						R_Shou_x = int(results.pose_world_landmarks.landmark[12].x * width)
						R_Sho_y = int(results.pose_world_landmarks.landmark[12].y * height)
						
						#5___Hombro Izquierdo:
						L_Shou_x = int(results.pose_world_landmarks.landmark[11].x * width)
						L_Sho_y = int(results.pose_world_landmarks.landmark[11].y * height)
							
						#6___Codo Derecho:
						R_Elb_x = int(results.pose_world_landmarks.landmark[14].x * width)
						R_Elb_y = int(results.pose_world_landmarks.landmark[14].y * height)
						

						#7___Codo Izquierdo:
						L_Elb_x = int(results.pose_world_landmarks.landmark[13].x * width)
						L_Elb_y = int(results.pose_world_landmarks.landmark[13].y * height)
						

						#8___Muñeca Derecha:
						R_Wri_x = int(results.pose_world_landmarks.landmark[16].x * width)
						R_Wri_y = int(results.pose_world_landmarks.landmark[16].y * height)
						
						
						#9___Muñeca Izquierda:
						L_Wri_x = int(results.pose_world_landmarks.landmark[15].x * width)
						L_Wri_y = int(results.pose_world_landmarks.landmark[15].y * height)

						#10__Cadera Derecha:
						R_Hip_x = int(results.pose_world_landmarks.landmark[24].x * width)
						R_Hip_y = int(results.pose_world_landmarks.landmark[24].y * height)

						#11__Cadera Izquierda:
						L_Hip_x = int(results.pose_world_landmarks.landmark[23].x * width)
						L_Hip_y = int(results.pose_world_landmarks.landmark[23].y * height)
						

						
						try:
						
							#----------------------PENDIENTES DEL
							def calculoPendientes(y2, y1, x2, x1):
								return ((y2 - y1) / (x2 - x1))

							def calculo_codos(m1,m2):
								return math.atan(((m2 - m1) / ((1) + (m1 * m2)))) * 180 / (math.pi)


							m1=calculoPendientes(R_Wri_y, R_Elb_y, R_Wri_x, R_Elb_x)
							m2=calculoPendientes(R_Elb_y, R_Sho_y, R_Elb_x, R_Shou_x)			
							
							m3=calculoPendientes(L_Wri_y, L_Elb_y, L_Wri_x, L_Elb_x)
							m4=calculoPendientes(L_Elb_y, L_Sho_y, L_Elb_x, L_Shou_x)
							
							
							#------------------------ANGULOS CAPTURADOS DEL LADO DERECHO

							angHombroIzq = abs(((math.atan((L_Sho_y - L_Elb_y) / ( L_Shou_x - L_Elb_x ))) * 180 / (math.pi)) + 90)
							angleBrazoIzq= calculo_codos(m1,m2)
							
							angHombroDer = abs(((math.atan((R_Sho_y - R_Elb_y) / ( R_Shou_x - R_Elb_x ))) * 180 / (math.pi)) + 90)
							angleBrazoDer=calculo_codos(m3,m4)

							if (nariz_x > R_ear_x):
								Angulo_Cuello=140
							elif (nariz_x < L_ear_x): 
								Angulo_Cuello=50
							else:
								Angulo_Cuello=90


							

						except ZeroDivisionError:
							pass
						
						
						#CALCULO PARA SIMULACION DE PROFUNDIDAD EN BASE CODO-HOMBRO:

						R_Codos_Dath_Deep=results.pose_world_landmarks.landmark[14] #Capturamos todos los puntos (en este caso del codo derecho)					
						obtepcion_R=(str(R_Codos_Dath_Deep)).split('\n')#quitamos el salto de linea y los convertimos en una list 
						R_Elb_punto_Z=obtepcion_R[2]# para obtener el punto X, ubicamos la lista la posicion 0 (correspondiente a la coordenada x)
						DeteccionDeFrentizida =abs((float(R_Elb_punto_Z[3:]))*100)
						
						if (DeteccionDeFrentizida >22):
							Profundidad_Left=(90)
							angHombroDer=0
							angleBrazoIzq=0				
							
						elif (DeteccionDeFrentizida <=22  ):
							Profundidad_Left=(0)
							

						L_Codos_Dath_Deep=results.pose_world_landmarks.landmark[13] #Capturamos todos los puntos (en este caso del codo derecho)					
						obtepcion_L=(str(L_Codos_Dath_Deep)).split('\n')#quitamos el salto de linea y los convertimos en una list 
						L_Elb_punto_Z=obtepcion_L[2]# para obtener el punto X, ubicamos la lista la posicion 0 (correspondiente a la coordenada x)
						DeteccionDeFrentizida2 =abs((float(L_Elb_punto_Z[3:]))*100)
						
						if (DeteccionDeFrentizida2 >22 ):
							Profundidad_Right=(90)
							angHombroIzq=180
							angleBrazoDer=0				
							
						elif (DeteccionDeFrentizida2 <=22  ):
							Profundidad_Right=(180)
							
						
						
						#--------------------------------------------IMAGEN DE SALIDA------------------------------------------------------------
						mp_drawing.draw_landmarks(flip,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(128,0,250),thickness=5,circle_radius=3),mp_drawing.DrawingSpec(color=(255,255,0),thickness=10))   
						convertir_QTSke = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
						bd[1]=1
						

							
					

					if self.hilo_corriendo and bd[0]==1 and bd[1]==1: #Las banderas son para detectar una persona y q no crashee el programa
							self.ImageEmotion.emit(convertir_QTEmo)					
							self.ImageSkeleton.emit(convertir_QTSke)								

							#-------------------PUNTOS DEL CUERPO

							self.Elbow_Left.emit(angHombroIzq)
							self.Elbow_Right.emit(angHombroDer)

							self.Wrist_Right.emit(angleBrazoIzq)
							self.Wrist_Left.emit(angleBrazoDer)

							self.Cuello.emit(Angulo_Cuello)
							
							if(angHombroDer>150 ):
								self.premio.emit(1)
							
							if(angHombroIzq<30 ):
								self.premio.emit(2)
								

							
							#self.Shoulder_Right.emit(Profundidad_Left)
							#self.Shoulder_Left.emit(Profundidad_Right)
		
													
		time.sleep(0.5)
						
	def stop(self):
		self.hilo_corriendo = False
		self.quit()


	

if __name__ == "__main__":
	app = QApplication(sys.argv) 
	mi_app = MiApp()
	mi_app.show()
	sys.exit(app.exec_())









