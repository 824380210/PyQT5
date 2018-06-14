# PyQT5 Example #21 of Image 
## 例子中要添加如何设置图象的位置的信息会更好   
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel
from PyQt5.QtGui import  QPixmap

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PYQT5 Imange Example 21  "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap('Icons/pengcz_msft.jpg'))
        self.label1.setGeometry(10,10,1800,1400)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())







```

# PyQT5 Example #22 of QSlider
## QSlider  QSlider  
```

import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QLineEdit,QSlider,QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example #22 QSlider"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        vboxlayout =QVBoxLayout()
        self.lineEdit =QLineEdit(self)
        vboxlayout.addWidget(self.lineEdit)
        self.lineEdit.move(100,50)

        self.slider = QSlider(Qt.Horizontal,self)
        self.slider.move(100,20)
        # self.slider = QSlider(Qt.Vertical,self)
        # l有水平的滑块和径直的滑块
        self.slider.setMinimum(1)
        self.slider.setMaximum(99)
        # self.slider.setValue(50)
        self.slider.setTickPosition(QSlider.TicksAbove)
        # self.slider.setTickPosition(QSlider.TicksBelow)
        #self.slider.setTickPosition(QSlider.TicksBothSides)
        # TickBothSides是默认值
        self.slider.setTickInterval(5)
        vboxlayout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.changeValue)

        # 设置滑块位置setTickPosition


        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def changeValue(self):
        size = self.slider.value()

        self.lineEdit.setText(str(size))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())




```


# PyQT5 Example of QSlider 
# 使用滑块，当滑块值 变化的时候，切换QLabel不同的图象功能
```

import sys
from PyQt5 import QtGui
from  PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QSlider,QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 QSlider Image Example #23 "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.slider = QSlider(Qt.Horizontal,self)
        self.slider.setGeometry(60,60,100,20)
        #self.slider.valueChanged.connect(self.changeValue)
        self.slider.valueChanged[int].connect(self.changeValue)
        # [int] 代表是什么呢 ？效果同上面的例子是一样的呵！
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Icons/save.gif'))
        self.label.move(100,100)


        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def changeValue(self,value):
        if value == 0:
            self.label.setPixmap(QPixmap('Icons/save.gif'))
        elif value < 50:
            self.label.setPixmap(QPixmap('Icons/copy.gif'))
        else:
            self.label.setPixmap(QPixmap('Icons/delete.gif'))


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
# PyQT5 Example 24 : QTables
###
###
 
```

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QTableWidget,QTableWidgetItem,QVBoxLayout

class Window(QWidget):
    """ 如果window不是继承QWidget，而是来自QMainWindow，实际测试的时候会不会显示QTable呵！"""
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Tables Example #24 "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.createTables()
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tablewidget)
        self.setLayout(self.vBoxLayout)
        self.show()

    def createTables(self):
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(5)
        #ROW 行
        self.tablewidget.setColumnCount(3)
        # column 列

        self.tablewidget.setItem(0,0,QTableWidgetItem("Name"))
        self.tablewidget.setItem(0, 1, QTableWidgetItem("Email"))
        self.tablewidget.setItem(0, 2, QTableWidgetItem("Phone Number"))
        #
        self.tablewidget.setItem(1,0,QTableWidgetItem("Peter "))
        self.tablewidget.setItem(1, 1, QTableWidgetItem("Peter@test.com "))
        self.tablewidget.setItem(1, 2, QTableWidgetItem("086-123456789"))
        #
        self.tablewidget.setColumnWidth(1,200)
        self.tablewidget.setColumnWidth(2, 150)
        #
        self.tablewidget.setItem(2,0,QTableWidgetItem("haohao"))
        self.tablewidget.setItem(2, 1, QTableWidgetItem("haohao@test.com "))
        self.tablewidget.setItem(2, 2, QTableWidgetItem("086-123489123"))
        #
        self.tablewidget.setItem(3,0,QTableWidgetItem("Paul"))
        self.tablewidget.setItem(3, 1, QTableWidgetItem("paul@test.com "))
        self.tablewidget.setItem(3, 2, QTableWidgetItem("086-456456456"))
        #
        self.tablewidget.setItem(4,0,QTableWidgetItem("John"))
        self.tablewidget.setItem(4, 1, QTableWidgetItem("john@test.com "))
        self.tablewidget.setItem(4, 2, QTableWidgetItem("086-123123123"))
        # 超出的行不会显示 ，如下面的信息
        self.tablewidget.setItem(5,0,QTableWidgetItem("Tony"))
        self.tablewidget.setItem(5, 1, QTableWidgetItem("Tony@test.com "))
        self.tablewidget.setItem(5, 2, QTableWidgetItem("086-234234234"))





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

```
##
#  PyQT5 example　#25  of DInputDialog
#
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QInputDialog,QLabel,QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example 25 : InputDialog"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.button1 = QPushButton("Open Dialog",self)
        self.button1.move(100,100)
        self.button1.clicked.connect(self.createInputDialog)

        self.label1 = QLabel("Hello",self)
        self.label1.setGeometry(100,150,300,50)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def createInputDialog(self):
        mytext,ok = QInputDialog.getText(self,"Inputdialog","Enter your name")
        if ok:
            self.label1.setText(str(mytext))
    # 注意QInputDialog的返回值 要转换

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
##   
# PyQT5 Example 26 : QFontDialog
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QFontDialog,QPushButton,QTextEdit

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example 26 # Font Dialog"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.button1 = QPushButton("Open FontDialog",self)
        self.button1.setGeometry(100,100,400,30)
        self.button1.clicked.connect(self.creatFontDialog)

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(100,150,400,300)



        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def creatFontDialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.textedit.setFont(font)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
#
# PyQT5 Example #27 QColorDialog 
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QFontDialog,QPushButton,QTextEdit,QColorDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Example 27 # Color Dialog"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.button1 = QPushButton("Open FontDialog",self)
        self.button1.setGeometry(100,100,400,30)
        self.button1.clicked.connect(self.createFontDialog)

        self.button2 = QPushButton("Open ColorDialog",self)
        self.button2.setGeometry(100,140,400,30)

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(100,180,400,300)
        self.button2.clicked.connect(self.createColorDialog)



        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def createFontDialog(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.textedit.setFont(font)
    def  createColorDialog(self):
        color = QColorDialog.getColor()
        self.textedit.setTextColor(color)
        #  注意要选中文本才能修改文本的色彩呵！



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
#
#
# PyQT5 Example 28 print Dialog 
```

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QTextEdit
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "xxxx "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.button1 = QPushButton("Print",self)
        self.button1.setGeometry(50,50,400,30)
        self.button1.clicked.connect(self.createPrintDialog)
        # setGeometry 左，上，长，高
        # 左代表离左边的距离
        # 上代表离上边的距离
        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(50,90,400,300)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def createPrintDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textedit.print_(printer)



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
# 实测在win 10  没有问题,这个示例只打印TextEdit中的文本呵！

```
#
# PyQT5 Example # 29 with printe preview functions
```

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QTextEdit
from PyQt5.QtPrintSupport import QPrintDialog,QPrinter,QPrintPreviewDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Printer with Preview functions  #29 "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        self.button1 = QPushButton("Print",self)
        self.button1.setGeometry(50,50,400,30)
        self.button1.clicked.connect(self.createPrintDialog)
        # setGeometry 左，上，长，高
        # 左代表离左边的距离
        # 上代表离上边的距离
        self.button2 = QPushButton("Print Preview",self)
        self.button2.setGeometry(50,90,400,30)
        self.button2.clicked.connect(self.createprintpreview)

        self.textedit = QTextEdit(self)
        self.textedit.setGeometry(50,130,400,300)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def createPrintDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textedit.print_(printer)
    def createprintpreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog  = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()
    def printPreview(self,printer):
        self.textedit.print_(printer)
        #这个函数需要提供打印机这个参数



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
# 实测在win 10  没有问题,这个示例只打印TextEdit中的文本呵！

```



