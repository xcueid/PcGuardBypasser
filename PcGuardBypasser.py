
# 디스코드 : 815stone / 유튜브 : @devaandsage
import time
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 126)
        MainWindow.setMinimumSize(QtCore.QSize(336, 126))
        MainWindow.setMaximumSize(QtCore.QSize(336, 126))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 311, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickLogin)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 161, 16))
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bypasser"))
        self.pushButton.setText(_translate("MainWindow", "우회 시작"))
        self.label.setText(_translate("MainWindow", "made by DevaAndSage"))
    
    def clickLogin(self):
        def pause_processes_by_name(process_names):
            paused_processes = 0
    
            for process_name in process_names:
                for process in psutil.process_iter(attrs=['name']):
                    if process.info['name'] == process_name:
                        try:
                            p = psutil.Process(process.pid)
                            p.suspend()  # 프로세스 일시 중단
                            print(f"프로세스 '{process_name}' (PID: {process.pid})가 일시 중단되었습니다.")
                            paused_processes += 1
                        except psutil.NoSuchProcess:
                            print(f"프로세스 '{process_name}' (PID: {process.pid})를 찾을 수 없습니다.")
    
            if paused_processes == 0:
                print("일시 중단된 프로세스가 없습니다.")


        process_names_to_pause = ["iAgent.exe", "iAgent32.exe", "iWatcher.exe"] 
        pause_processes_by_name(process_names_to_pause)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())