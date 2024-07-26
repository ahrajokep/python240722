# taxExcel.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path
import pandas as pd
import numpy as np

#디자인 파일을 로딩
form_class = uic.loadUiType(r"C:\Work2\taxExcel.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        # 초기값 셋팅 
        self.filename = "" # 경로표시용 텍스트
        self.downloadFolder = "" # 경로표시용 텍스트
        self.setupUi(self)
        self.textBrowser_upload = "파일을 upload 해주세요." # 텍스트 브라우저
        self.textBrowser_download = "다운로드 폴더를 지정해주세요." # 텍스트 브라우저
      
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if self.fileName:
            self.textBrowser_upload.setText(f"Selected File: {self.fileName}")
            QMessageBox.information(self, "File Selected", f"Selected File: {self.fileName}")

    

#인스턴스를 생성한다. 
app = QApplication(sys.argv)
myWindow = Window()
myWindow.show()
app.exec_()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     demoWindow = DemoForm()
#     demoWindow.show()
#     app.exec_()

