from PyQt5.QtCore import QCoreApplication
from matrix import Matrix
from matrix import number
from communicator import TCommunicator
from PyQt5.QtCore import pyqtSignal


class TApplication(QCoreApplication):
    def __init__(self, *args):
        super().__init__(args[0])
        self.__matrix = Matrix()
        self.__communicator = TCommunicator()
        self.__communicator.receive_signal.connect(self.__receive_message)

    def __receive_message(self, message):
        matrix_str = message.split('#')[1]
        # size = int(len(matrix_str.split(' ')) ** 1/2)
        # new_matrix = [[0 for j in range(size)] for i in range(size)]
        new_matrix = []
        for i in matrix_str.split('|'):
            new_row = []
            for j in i.split(' '):
                new_row.append(number(j))
            new_matrix.append(new_row)
        self.__matrix.set_data(new_matrix)
        operation = message.split('#')[0]
        if operation == 'trans':
            self.__matrix.transpose()
            str_matrix = ""
            for i in range(self.__matrix.get_number_of_rows()):
                for j in range(self.__matrix.get_number_of_columns()):
                    # new_matrix[i][j] = self.__interface.tableWidget.item(i, j).text()
                    str_matrix = str_matrix + str(self.__matrix[i][j])
                    if j != self.__matrix.get_number_of_rows() - 1:
                        str_matrix = str_matrix + ' '
                if i != self.__matrix.get_number_of_rows() - 1:
                    str_matrix = str_matrix + "|"
            result = str_matrix
        elif operation == 'det':
            result = str(self.__matrix.det())
        else:
            result = str(self.__matrix.rank())
        self.__send_answer(operation + '#' + result)

    def __send_answer(self, message):
        self.__communicator._TCommunicator__send_message(message)
