import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Coffee(QMainWindow):
    def __init__(self):
        super(Coffee, self).__init__()
        uic.loadUi('main.ui', self)
        self.pod = sqlite3.connect('coffee.sqlite3')
        self.cu = self.pod.cursor()
        data = self.cu.execute("select * from coffee").fetchall()
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                t = QTableWidgetItem(str(elem))
                self.tableWidget.setItem(
                    i, j, t)


print('dsjds')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    co = Coffee()
    co.show()
    sys.exit(app.exec())
