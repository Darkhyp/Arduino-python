# python -m PyQt5.uic.pyuic -x main.ui -o design.py
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtTest, QtSvg,QtGui
import design
from port import serial_ports,speeds
import serial

from mathTex_to_QPixmap import mathTex_to_QPixmap

# python -m pip install pyqtgraph
from pyqtgraph import PlotWidget, plot

from threading import Thread
import time

class LedApp(QtWidgets.QMainWindow, design.Ui_Form):
	seconds = [0]
	voltage = [0]
	stop = False
	timer = QtCore.QTimer()
	isLED = True
	def __init__(self):

		super().__init__()
		self.setupUi(self)
		self.Port.addItems(serial_ports())
		self.Speed.addItems(speeds)
		self.Speed.setCurrentIndex(3)
		self.realport = None
		self.ConnectButton.clicked.connect(self.connect)
		self.BaudDetectButton.clicked.connect(self.detectspeed)
		self.OnBtn.clicked.connect(self.setLED_onoff)
		self.GetVBtn.clicked.connect(self.read_V)
		self.GetVcontBtn.clicked.connect(self.read_Vcont)
		self.blinkBtn.clicked.connect(self.setLED_Blinc)
#		self.graphWidget.plot(self.seconds, self.voltage)
		self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:20px\">Voltage (V)</span>")
		self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:20px\">Iteration</span>")

#		fontsize = 12
#		math_exp = r'$\frac{1}{\sqrt{2}}\sqrt{X^\dag}$'
#		qpixmap = mathTex_to_QPixmap(math_exp, fontsize)
#		self.label.setPixmap(qpixmap)
#		self.label.setGeometry(QtCore.QRect(30, 30, 80, 40))


		self.setBtns(False)




	def detectspeed(self):
		for i in range(self.Speed.count()):
			print('check speed: '+self.Speed.itemText(i)+' at '+self.Port.currentText())
			if self.Speed.itemText(i)=='undefined':
				self.Speed.setCurrentIndex(i)
				break
			self.realport = serial.Serial(self.Port.currentText(),int(self.Speed.itemText(i)))
			self.realport.timeout = 0.5
			if self.realport:
				QtTest.QTest.qWait(2000)
				# port check
				self.realport.write(b't')
				getData = self.realport.readline().decode('utf-8').rstrip()
				if getData=='T':
					self.Speed.setCurrentIndex(i)
					self.connected()
					break
			self.realport.close()

	def connected(self):
		self.ConnectButton.setStyleSheet("background-color: green")
		self.ConnectButton.setText('Connected')
		self.setBtns(True)
		if self.realport:
			QtTest.QTest.qWait(2000)
			self.realport.write(b'c')

	def connect(self):
		if self.ConnectButton.text()=='Connected':
			self.timer.stop()
			self.GetVcontBtn.setText('Get Voltage every 1s')
			self.realport.close()
			self.realport = []
			self.ConnectButton.setStyleSheet("background-color: #e3e3e3")
			self.ConnectButton.setText('Connect')
			self.setBtns(False)
		elif not self.Speed.currentText()=='undefined':
			try:
				self.realport = serial.Serial(self.Port.currentText(),int(self.Speed.currentText()))
				self.realport.timeout = 0.5
				self.connected()
			except Exception as e:
				print(e)

	def setBtns(self,state):
		self.OnBtn.setEnabled(state)
		self.GetVBtn.setEnabled(state)
		self.GetVcontBtn.setEnabled(state)
		self.blinkBtn.setEnabled(state)

	def get_V(self):
		if self.realport:
			self.realport.write(b'v')
			getData = self.realport.readline().decode('utf-8').rstrip()
			return int(getData)/(2**10-1)*5
		return 0

	def read_V(self):
		self.label_Vtext.setText(str(self.get_V())+'V')

	def read_Vcont(self):
		self.stop = not self.stop
		if self.stop:
			self.GetVcontBtn.setText('Stop Voltage every 1s')
			self.timer.setInterval(1000)
			self.timer.timeout.connect(self.update_plot_data)
			self.timer.start()

#			print('add para thread')
#			thread = Thread(target=self.para)
#			thread.start()
		else:
			self.timer.stop()
			self.GetVcontBtn.setText('Get Voltage every 1s')
	def update_plot_data(self):
			self.voltage.append(self.get_V())
			self.seconds.append(self.seconds[-1]+1)
#			N = len(self.seconds)-1
#			N0 = N-10 if N>10 else 0
#			print('N0=',N0)
#			self.seconds = self.seconds[N0:]
#			self.voltage = self.voltage[N0:]
			if len(self.seconds)>=10:
				self.seconds = self.seconds[1:]
				self.voltage = self.voltage[1:]

			# plot data: x, y values
			self.graphWidget.clear()
			self.graphWidget.plot(self.seconds, self.voltage, symbol='o', symbolSize=10)
	def para(self):
		print('para start')
		while self.stop:
			self.update_plot_data()
			time.sleep(1);
		print('para stop')


	def setLED_onoff(self):
		if self.realport:
			if self.isLED:
				self.realport.write(b'e')
				self.OnBtn.setText('LED off')
			else:
				self.realport.write(b'd')
				self.OnBtn.setText('LED on')
		self.isLED = not self.isLED
	def setLED_Blinc(self):
		if self.realport:
			self.realport.write(b'b')



def main():
	app = QtWidgets.QApplication(sys.argv)
	window = LedApp()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()