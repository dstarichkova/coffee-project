import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
import sqlite3


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        sorts = self.cur.execute('SELECT sort FROM coffee').fetchall()
        for i in sorts:
            self.choose_coffee.addItem(i[0])
        self.btn.clicked.connect(self.run)

    def run(self):
        info = self.cur.execute(
            f"SELECT * FROM coffee WHERE sort = '{self.choose_coffee.currentText()}"
            f"'").fetchall()[0]
        self.id.setText(str(info[0]))
        self.sort.setText(info[1])
        self.roast.setText(info[2])
        self.beans.setText(info[3])
        self.taste.setText(info[4])
        self.price.setText(str(info[5]))
        self.bag_size.setText(str(info[6]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
