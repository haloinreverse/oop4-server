import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtCore import pyqtSignal


class TCommunicator(QUdpSocket):
    receive_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.__my_port = 12345
        self.__client_port = 12344
        self.bind(self.__my_port)  # Привязываемся к порту 12345
        self.__host = QHostAddress("127.0.0.1")
        self.readyRead.connect(self.__receive_message)


    def __receive_message(self):
        while self.hasPendingDatagrams():
            datagram, host, port = self.readDatagram(self.pendingDatagramSize())
            message = datagram.decode()
            print(f"Received message: {message} from {host.toString()}:{port}")
            self.receive_signal.emit(message)

    def __send_message(self, message):
        # Отправляем ответ
        self.writeDatagram(message.encode(), self.__host, self.__client_port)
