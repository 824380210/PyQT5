#
# 这是PyQT5 第31个例子： 介绍将QTestEdit中内容生成PDF文件
## 重点要注意
##
##
##
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QTextEdit,QFileDialog
from PyQt5.QtCore import QFileInfo
from PyQt5.QtPrintSupport import QPrinter

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example # 31  PDF Exporter  "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.btn1 = QPushButton("Export PDF",self)
        self.btn1.setGeometry(50,50,400,30)
        self.btn1.clicked.connect(self.printPDF)

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(50,90,400,500)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def printPDF(self):
        fn, _  = QFileDialog.getSaveFileName(self,'Export PEF ',None,'PDF files(.pdf);;All Files()')

        if fn != '':
            if QFileInfo(fn).suffix() == "":fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textedit.document().print_(printer)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```

##
##




#
# 这是PyQT5 第32个例子： 介绍将python脚本打包成exe文件，在这里不作处理
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第33个例子： 介绍连接到数据库
## 重点要注意
##
##
##
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication, QPushButton, QMessageBox
# from
import MySQLdb as mdb

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example # 33 connect to Maria Database  "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.btn = QPushButton("Connect MariaDB Status",self)
        self.btn.setGeometry(100,100,300,50)
        self.btn.clicked.connect(self.connectDB)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def connectDB(self):
        try:
            db = mdb.connect('10.186.246.232','root','mypass','pyqt5')
            # host,username,password ,database name
            QMessageBox.about(self,'connection',"connect ot DB successfully ")
            print("connect to pyqt5 database !")
        except mdb.Error as e:
            QMessageBox.about(self,'Connection Failed',"ERROR")
            print(e)
            sys.exit(1)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())



```

##
##



#
# 这是PyQT5 第34个例子： 介绍
## 重点要注意
##
##
##
```

import sys
import traceback
from itertools import combinations

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit, QPushButton,QMessageBox
import MySQLdb as mdb

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example # 34 Insert Data to MySQL"
        # CRUD : create，retrieve， Update，Delete创建，获取，更新，删除
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.lineedit1 = QLineEdit(self)
        self.lineedit1.setPlaceholderText("Please enter your name:")
        self.lineedit1.setGeometry(50,50,300,30)

        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText("Please enter your Email:")
        self.lineedit2.setGeometry(50,90,300,30)

        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setPlaceholderText("Please enter your Phone:")
        self.lineedit3.setGeometry(50,140,300,30)

        self.btn = QPushButton("Insert Data ",self)
        self.btn.setGeometry(50,190,200,50)
        self.btn.clicked.connect(self.InsertData)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

    def InsertData(self):

        try:
            con = mdb.connect('10.186.246.232', 'root', 'mypass', 'pyqt5')
            cur = con.cursor()

        # except mdb.OperationalError as e:
        #     print(str(e))
            # cur.execute("insert into data values('2', 'peter', 'peter@125.com', 86361590)")
            #sql = '''  insert into data( name,email,phone) values("peter1","peter1@q.com",'12345abc6')  '''
            # 如果输入的不是数字，在输入数据库会提法 截断呵！
            ''' D:/pyqt5/a/34MySQL_CRUD.py:55: Warning: (1265, "Data truncated for column 'phone' at row 1")
  cur.execute(sql) '''
            print("before check")
            myname  = self.lineedit1.text()
            myemail = self.lineedit2.text()
            myphone = self.lineedit3.text()
            sql = "insert into data( name,email,phone) values('{}','{}','{}'); ".format(myname,myemail,myphone)
            print(sql)
            cur.execute(sql)
            cur.close()
            con.commit()
            con.close()
            print("Done")
        except mdb.Error as e:
            print(str(e))

# 没有对输入进行检查，不清楚是否合规 ,如果输入中文会失败呵！估计要转换一个，或者数据库不支持
"""



before check
insert into data( name,email,phone) values('宜','好人卡','1231'); 

Process finished with exit code -2147483645

"""

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```

##
##



#
# 这是PyQT5 第35个例子： 介绍手支从table中向数据库插入数据
## 重点要注意
##
##
##
```

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyqt5\a\35QtableWidgets.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb

class Ui_MainWindow(object):

    def InsertData(self):
        name  = [ self.tableWidget.item(row,0).text() for row in range(self.tableWidget.rowCount()) ]
        email = [ self.tableWidget.item(row,1).text() for row in range(self.tableWidget.rowCount()) ]
        phone = [ self.tableWidget.item(row,2).text() for row in range(self.tableWidget.rowCount()) ]
        # iy注意上面生成的是列表


        # name = "xxxx00"
        # email = "xxxx11"
        # phone = "12343"

        # name  = self.tableWidget.items(1, 0).text()
        # email = self.tableWidget.items(1, 1).text()
        # phone = self.tableWidget.items(1, 2).text()


        con = mdb.connect('10.186.246.232','root','mypass','pyqt5')
        print("Connect to DB server OK")
        try:
            cur = con.cursor()
            sql = "insert into data(name,email,phone) values('{}','{}','{}'); ".format(name[0],email[0],phone[0])
            cur.execute(sql)
            cur.close()
            con.commit()
            con.close()
            print("Done")
        except mdb.Error as e:
            print(e)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 491, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 271, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.InsertData)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        self.pushButton.setText(_translate("MainWindow", "Insert Data to mysql server "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



```

mmplementation generated from reading ui file 'd:\pyqt5\a\35QtableWidgets.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb

class Ui_MainWindow(object):

    def InsertData(self):
        name  = [ self.tableWidget.item(row,0).text() for row in range(self.tableWidget.rowCount()) ]
        email = [ self.tableWidget.item(row,1).text() for row in range(self.tableWidget.rowCount()) ]
        phone = [ self.tableWidget.item(row,2).text() for row in range(self.tableWidget.rowCount()) ]
        # iy注意上面生成的是列表


        # name = "xxxx00"
        # email = "xxxx11"
        # phone = "12343"

        # name  = self.tableWidget.items(1, 0).text()
        # email = self.tableWidget.items(1, 1).text()
        # phone = self.tableWidget.items(1, 2).text()


        con = mdb.connect('10.186.246.232','root','mypass','pyqt5')
        print("Connect to DB server OK")
        try:
            cur = con.cursor()
            sql = "insert into data(name,email,phone) values('{}','{}','{}'); ".format(name[0],email[0],phone[0])
            cur.execute(sql)
            cur.close()
            con.commit()
            con.close()
            print("Done")
        except mdb.Error as e:
            print(e)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 458)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 491, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 271, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.InsertData)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        self.pushButton.setText(_translate("MainWindow", "Insert Data to mysql server "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#
##



#
# 这是PyQT5 第36个例子： 介绍
## 重点要注意
##
##
##
```



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\pyqt5\a\36loadDatafromMysql.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
from PyQt5.QtGui import QTextCursor


class Ui_MainWindow(object):
    def LoadMysqlData(self):
        try:
            conn = mdb.connect("10.186.246.232","root","mypass","pyqt5")
            cur = conn.cursor()
            sql = "select name,email,phone from data;"
            cur.execute(sql)
            print(sql)
            # for i in range(cur.rowcount):
            #     result = cur.fetchone()
            #     #result = cur.fetchall()
            #     print(result)
            #     print("===================")
            result = cur.fetchall()
            print(result)
            print(type(result))
            cur.close()
            conn.commit()
            conn.close()
            try:
                for row in result:
                    # print(row)
                    # print('*'*50)
                    self.cursor = QTextCursor(self.textEdit.document())
                    # self.cursor.insertText(str(row[0]) + "\n")
                    self.cursor.insertText(str(row) + "\n")
            except:
                print("=ERROR=================")
                # self.cursor = QTextCursor(self.textEdit.document())
                # self.cursor.insertText(str(row))
            # cur.close()
            # con.commit()
            # con.close()
        except mdb.Error as e:
            print(e)

    def setupUi(self, MainWindow):
        # self.setWindowIcon(QtGui.QIcon(".png"))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("Icons/run.png"))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 100, 591, 251))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 541, 81))
        self.pushButton.clicked.connect(self.LoadMysqlData)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Data From Database In PyQt5"))
        self.pushButton.setText(_translate("MainWindow", "Load Data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



```

##
##



#
# 这是PyQT5 第37个例子： 介绍交python脚本打包成一个安装文件（installer ）在这里忽略
## 重点要注意

#
# 这是PyQT5 第38 个例子： 介绍painter
## 重点要注意
##
##
##
```
mport sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
from PyQt5.QtGui import QPen, QBrush,QPainter
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example # 38 Drawing Rectangle "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

    def paintEvent(self,e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red,5 ,Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.red,Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.green,Qt.DiagCrossPattern))
        painter.drawRect(100,15,400,200)
    """
    当发生一下情况时会产生绘制事件并调用paintEvent()函数:

1.在窗口部件第一次显示时，系统会自动产生一个绘图事件，从而强制绘制这个窗口部件。

2.当重新调整窗口部件的大小时，系统也会产生一个绘制事件。

3.当窗口部件被其他窗口部件遮挡，然后又再次显示出来的时候，就会对那些隐藏的区域产生一个绘制事件。

同时可以调用QWidget::update()或者QWidget::repaint()来强制产生一个绘制事件。二者的区别是:

repaint()函数会强制产生一个即时的重绘事件,而update()函数只是在Qt下一次处理事件时才调用一次绘制事件。

如果多次调用update(),Qt会把连续多次的绘制事件压缩成一个单一的绘制事件，这样可避免闪烁现象。
    """



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```

##
##


#
# 这是PyQT5 第39 个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##
#
# 这是PyQT5 第 40 个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##

