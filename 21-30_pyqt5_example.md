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



