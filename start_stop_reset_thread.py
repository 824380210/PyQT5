mplementation generated from reading ui file 'multiple_thread_start_stop_reset.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import traceback
import time
class Ui_Form(object):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.stop_progress = True

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 219)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 181, 131))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(40, 30, 91, 62))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton__start = QtWidgets.QRadioButton(self.widget)
        self.radioButton__start.setObjectName("radioButton__start")
        self.verticalLayout.addWidget(self.radioButton__start)
        self.radioButton__stop = QtWidgets.QRadioButton(self.widget)
        self.radioButton__stop.setObjectName("radioButton__stop")
        self.verticalLayout.addWidget(self.radioButton__stop)
        self.radioButton__reset = QtWidgets.QRadioButton(self.widget)
        self.radioButton__reset.setObjectName("radioButton__reset")
        self.verticalLayout.addWidget(self.radioButton__reset)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(0, 170, 581, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #
        #
        self.radioButton__start.clicked.connect(self.start_progressbar)
        self.radioButton__stop.clicked.connect(self.stop_progressbar)
        self.radioButton__reset.clicked.connect(self.reset_progressbar)
    def progressbar_counter(self,start_value=0):
        print("call subprocess .... ")
        self.rthread = run_thread(parent=None,counter_start=start_value)
        self.rthread.start()
        self.rthread.counter_value.connect(self.set_progress)
    def set_progress(self,counter):
        if not self.stop_progress:
            print(counter)
            self.progressBar.setValue(counter)

    def start_progressbar(self):
        self.stop_progress = False
        self.progressbar_value = self.progressBar.value()
        print("the start value is {}".format(self.progressbar_value))
        self.progressbar_counter(self.progressbar_value)



    def stop_progressbar(self):
        self.stop_progress = True
        try:
            self.rthread.stop()
        except:
            pass

    def reset_progressbar(self):
        self.stop_progressbar()
        #
        self.progressbar_value = 0
        self.progressBar.reset()
        self.stop_progress = True

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.radioButton__start.setText(_translate("Form", "start"))
        self.radioButton__stop.setText(_translate("Form", "stop"))
        self.radioButton__reset.setText(_translate("Form", "reset"))

class run_thread(QtCore.QThread):
    counter_value  = QtCore.pyqtSignal(int)

    def __init__(self,parent=None,counter_start=0):
        super(run_thread,self).__init__(parent)
        print("the begin value is {} from the main thread".format(counter_start))
        self.counter = counter_start
        self.is_running = True

    def run(self):
        print("Hi,Im here start to run ...")
        while self.counter <100 and self.is_running == True:
            time.sleep(0.4)
            self.counter += 1
            print(self.counter)
            self.counter_value.emit(self.counter)
    def stop(self):
        self.is_running = False
        print("Stopping threading...")
        self.terminate()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

