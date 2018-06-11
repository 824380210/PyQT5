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

# PyQT5 Example #22 of Image
##
```




```



