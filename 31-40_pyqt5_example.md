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
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##



#
# 这是PyQT5 第31个例子： 介绍
## 重点要注意
##
##
##
```



```

##
##





