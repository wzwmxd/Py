#!/usr/bin/python
# -*- coding:utf-8-*-
import sys
from PyQt4.QtGui import QApplication, QWidget

a = QApplication(sys.argv)
w = QWidget()
w.resize(320, 240)
w.setWindowTitle('Hello!')
w.show()
sys.exit(a.exec_())
