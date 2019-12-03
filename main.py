import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from main_window import Ui_MainWindow
import logging
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.groupSize, self.imgIndex = 5, 0
        self.imgLabels = [self.ui.image1, self.ui.image2,
                          self.ui.image3, self.ui.image4, self.ui.image5]
        self.imgNumber = 0

    def showImage(self):
        self.readImages()
        for i in range(len(self.images)):
            w, h = self.imgLabels[i].width(), self.imgLabels[i].height()
            self.imgLabels[i].setPixmap(
                self.images[i].scaled(w, h, QtCore.Qt.KeepAspectRatio))

    def getPath(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Open Directory')
        logging.info('open fold Directory' + fileName)
        self.filePath = fileName
        self.getImagesName()

    def getImagesName(self):
        names = os.listdir(self.filePath)
        for item in names:
            item = item.lower()
            if not item.endswith(".png") and not item.endswith(".jpg"):
                names.remove(item)
        names.sort()
        self.names = list([])
        for i in range(0, len(names), self.groupSize):
            tmp = []
            for j in range(self.groupSize):
                if i + j < len(names):
                    tmp.append(names[i + j])
            self.names.append(tmp)
        self.imgNumber = len(self.names)

    def readImages(self):
        self.images = []
        for item in self.names[self.imgIndex]:
            self.images.append(QPixmap(self.filePath + '/' + item))


    def addIndex(self, cnt):
        self.imgIndex += cnt
        if (self.imgIndex >= self.imgNumber):
            self.imgIndex = self.imgNumber - 1
        if (self.imgIndex <= 0):
            self.imgIndex = 0

    def updateUI(self):
        self.readImages()
        self.showImage()

    def goNext(self):
        self.addIndex(1)
        self.updateUI()

    def goBefore(self):
        self.addIndex(-1)
        self.updateUI()

    def goFarNext(self):
        self.addIndex(10)
        self.updateUI()

    def goFarBefore(self):
        self.addIndex(-10)
        self.updateUI()

    def goHome(self):
        self.addIndex(-99999)
        self.updateUI()

    def goEnd(self):
        self.addIndex(99999)
        self.updateUI()

    def openFoldButton(self):
        self.getPath()
        self.getImagesName()
        self.imgIndex = 0
        self.updateUI


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                        format='%(asctime)s - %(levelname)s: %(message)s')
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
