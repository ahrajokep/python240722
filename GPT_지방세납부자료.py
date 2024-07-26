import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
import pandas as pd

class ExcelConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('지방세 납부자료 만들기')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.openButton = QPushButton('Open Excel File', self)
        self.openButton.clicked.connect(self.openFileNameDialog)
        layout.addWidget(self.openButton)

        self.filePathLabel = QLabel('파일이 선택되지 않았습니다.', self)
        layout.addWidget(self.filePathLabel)

        self.saveButton = QPushButton('Download Folder Path', self)
        self.saveButton.clicked.connect(self.saveFileDialog)
        layout.addWidget(self.saveButton)

        self.savePathLabel = QLabel('저장될 폴더 경로가 지정되지 않았습니다.', self)
        layout.addWidget(self.savePathLabel)

        self.makeButton = QPushButton('실행', self)
        # self.makeButton.clicked.connect(self.makeExcelfile)
        layout.addWidget(self.makeButton)

        self.savePathLabel = QLabel('저장될 폴더 경로가 지정되지 않았습니다.', self)
        layout.addWidget(self.savePathLabel)

        self.setLayout(layout)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if self.fileName:
            self.filePathLabel.setText(f"Selected File: {self.fileName}")
            QMessageBox.information(self, "File Selected", f"Selected File: {self.fileName}")

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        self.savePath = QFileDialog.getExistingDirectory(self, "Select Directory to Save Files", options=options)
        if self.savePath:
            self.savePathLabel.setText(f"Save Directory: {self.savePath}")
            try:
                self.convertExcelFile(self.savePath)
                QMessageBox.information(self, "Success", "Files have been saved successfully.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def convertExcelFile(self, savePath):
        df = pd.read_excel(self.fileName)
        df['전자납부번호'] = df['전자납부번호'].astype(str)

        csv_file = f"{savePath}/수정된_납부대상확인.csv"
        excel_file = f"{savePath}/수정된_납부대상확인.xlsx"

        df.to_csv(csv_file, index=False)
        df.to_excel(excel_file, index=False, engine='xlsxwriter')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExcelConverter()
    ex.show()
    sys.exit(app.exec_())
