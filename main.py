import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from app import TApplication

if __name__ == '__main__':
    app = TApplication(sys.argv)

    sys.exit(app.exec_())
