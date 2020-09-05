# ORGANOID MICROINJECTION SYSTEM - APP

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from microinjection.graphics.util import *

def main():

    app = QApplication(sys.argv)
    win = QMainWindow()
    win_title = 'ATFL Microinjection System'
    win_origin_x, win_origin_y, win_width, win_height = win_center_coords(QApplication.desktop().width(),
                                                                          QApplication.desktop().height())

    win.setGeometry(win_origin_x, win_origin_y, win_width, win_height)
    win.setWindowTitle(win_title)

    win.show()
    sys.exit(app.exec())




if __name__ == "__main__":
    main()
