import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog

class TaxExcelApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('지방세 납부자료 조건별 다운로드 프로그램')

        self.titleLabel = QLabel('지방세 납부자료 조건별 다운로드 프로그램', self)
        self.titleLabel.setGeometry(150, 30, 300, 30)

        self.uploadLabel = QLabel('납부전체자료 Upload', self)
        self.uploadLabel.setGeometry(50, 100, 150, 20)

        self.uploadLineEdit = QLineEdit(self)
        self.uploadLineEdit.setGeometry(50, 130, 400, 20)

        self.uploadButton = QPushButton('파일찾기', self)
        self.uploadButton.setGeometry(470, 130, 80, 20)
        self.uploadButton.clicked.connect(self.openFileNameDialog)

        self.saveLabel = QLabel('결과파일 저장경로 지정', self)
        self.saveLabel.setGeometry(50, 180, 200, 20)

        self.saveLineEdit = QLineEdit(self)
        self.saveLineEdit.setGeometry(50, 210, 400, 20)

        self.saveButton = QPushButton('경로찾기', self)
        self.saveButton.setGeometry(470, 210, 80, 20)
        self.saveButton.clicked.connect(self.openDirectoryDialog)

        self.infoLabel = QLabel('세금조건: 재산세(건축물), 재산세(토지), 재산세(주택)\n지역조건: 과천시, ... (30개)', self)
        self.infoLabel.setGeometry(50, 260, 500, 40)

        self.executeButton = QPushButton('실행', self)
        self.executeButton.setGeometry(250, 320, 100, 30)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "파일 선택", "", "All Files (*);;Excel Files (*.xls *.xlsx)", options=options)
        if fileName:
            self.uploadLineEdit.setText(fileName)

    def openDirectoryDialog(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "경로 선택", options=options)
        if directory:
            self.saveLineEdit.setText(directory)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TaxExcelApp()
    ex.show()
    sys.exit(app.exec_())
