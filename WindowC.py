from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_window import Ui_MainWindow
import os
import easyocr
import configparser

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.config = configparser.ConfigParser()
        self.config.read(".\\Langs.ini")
        ini = self.config
        lst_str = ini['BASIC_SETTING']['langs']
        self.item = ""
        self.langs = []
        for char in lst_str.replace(" ", ""):
            if char != ",":
                self.item += char
            else:
                self.langs.append(self.item)
                self.item = ""
        if self.item != "":
            self.langs.append(self.item)
        self.reader = easyocr.Reader(["en", "ch_sim"])
        

    def choose(self):
        try:
            self.name, self.type = QtWidgets.QFileDialog.getOpenFileName(self, "Open a picture:", os.getcwd(), "All files(*)")
            self.label.setPixmap(QtGui.QPixmap(self.name))
            self.label.setScaledContents(True)
            self.results = self.reader.readtext(self.name)
            self.result = ""
            for line in self.results:
                self.result += (line[1] + "\n")
            self.textBrowser.setText(self.result)
        except:
            pass
