from PyQt5 import QtWidgets, QtGui, QtCore

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)


class PushBut1(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        super(PushBut1, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("margin: 1px; padding: 7px; background - color: rgba(1, 255, 0, 100); "
                           "color: rgba(1, 140, 0, 100); border-style: solid; border-radius: 3px; border-width: 0.5px; "
                           "border-color: rgba(1, 140, 0, 100);")

    def enterEvent(self, event):
        self.setStyleSheet("margin: 1px; padding: 7px; background - color: rgba(1, 140, 040, 100); "
                           "color: rgba(1, 140, 255, 100); border-style: solid; border-radius: 3px; "
                           "border-width: 0.5px; border-color: rgba(1, 140, 140, 100);")

    def leaveEvent(self, event):
        self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1, 255, 0, 100); "
                           "color: rgba(1, 140, 0, 100); border-style: solid; border-radius: 3px; border-width: 0.5px; "
                           "border-color: rgba(1, 140, 0, 100);")

    def on_but1(self):
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1, 140, 0, 100); "
                                 "color: rgba(1, 255, 255, 100); border-style: solid; border-radius: 3px; "
                                 "border-width: 0.5px; border-color: rgba(1, 140, 0, 100);")


class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("PyQt Application")
        # self.setWindowIcon(QtGui.QIcon("Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 1.5)
        self.setStyleSheet("QWidget {background - color: rgba(0, 0, 0, 1);} "
                           "QScrollBar: horizontal {width: 1px; height: 1px; background-color: rgba(0, 140, 0, 255);} "
                           "QScrollBar: vertical {width: 1px; height: 1px; background-color: rgba(0, 140, 0, 255);}")
        self.textf = QtWidgets.QTextEdit(self)
        self.textf.setPlaceholderText("Results...")
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(0, 0, 0, 1); "
                                 "color: rgba(255, 255, 255, 1); border-style: solid; border-radius: 3px; "
                                 "border-width: 0.5px; border - color: rgba(1, 140, 0, 100); ")
        self.but1 = PushBut1(self)
        self.but1.setText("")
        self.but1.setFixedWidth(72)
        self.but1.setFont(font_but)
        self.but2 = PushBut1(self)
        self.but2.setText("")
        self.but2.setFixedWidth(72)
        self.but2.setFont(font_but)
        self.but3 = PushBut1(self)
        self.but3.setText("")
        self.but3.setFixedWidth(72)
        self.but3.setFont(font_but)
        self.but4 = PushBut1(self)
        self.but4.setText("")
        self.but4.setFixedWidth(72)
        self.but4.setFont(font_but)
        self.but5 = PushBut1(self)
        self.but5.setText("")
        self.but5.setFixedWidth(72)
        self.but5.setFont(font_but)
        self.but6 = PushBut1(self)
        self.but6.setText("")
        self.but6.setFixedWidth(72)
        self.but6.setFont(font_but)
        self.but7 = PushBut1(self)
        self.but7.setText("")
        self.but7.setFixedWidth(72)
        self.but7.setFont(font_but)
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.textf, 0, 0, 14, 13)
        self.grid1.addWidget(self.but1, 0, 14, 1, 1)
        self.grid1.addWidget(self.but2, 1, 14, 1, 1)
        self.grid1.addWidget(self.but3, 2, 14, 1, 1)
        self.grid1.addWidget(self.but4, 3, 14, 1, 1)
        self.grid1.addWidget(self.but5, 4, 14, 1, 1)
        self.grid1.addWidget(self.but6, 5, 14, 1, 1)
        self.grid1.addWidget(self.but7, 6, 14, 1, 1)
        self.grid1.setContentsMargins(7, 7, 7, 7)
        self.setLayout(self.grid1)
        self.but1.clicked.connect(self.on_but1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(0.95)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()