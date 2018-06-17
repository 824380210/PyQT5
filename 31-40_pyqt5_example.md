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

# 没有对输入进行检查，不清楚是否合规

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```

##
##



#
# 这是PyQT5 第35个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第36个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第37个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第38 个例子： 介绍
## 重点要注意
##
##
##
```



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

