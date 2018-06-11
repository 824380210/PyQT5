# 示例11 菜单，及菜单及联actions
#
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QStatusBar,QPushButton,QWidget,QAction

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "QMenuBar"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()
        self.button = QPushButton("click me",self)
        self.button.move(200,200)
        self.button.clicked.connect(self.AddMessage)
        self.InitUI()
    def InitUI(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        serachMenu = mainMenu.addMenu("Search")
        toolMenu = mainMenu.addMenu("Tool")
        helpMenu = mainMenu.addMenu("Help")
     #   上面生成了主菜单
        exitButton = QAction(QIcon("Icons/run.png"),'Exit',self)
        exitButton.setShortcut("Ctrl+E")
        exitButton.setStatusTip("Exit Application")
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        # 上面的showMessage并不会自动显示出来，要手动输入呵！
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
    def AddMessage(self):
        self.statusBar().showMessage("the button is clicked")
App =QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

```

## 上面的例子中可以看到菜单可以6个菜单，且File菜单中有一个关联的actions
##  上面的例子中没有看到setStatusTip的作用，mouse在菜单上没有看到提示信息
##  update on 2016-06-06
## 
# 右键弹出式菜单，你可以定义菜单中不同的键执行不同的动作
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QMenu,QMenuBar,QAction,QStatusBar

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
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def contextMenuEvent(self, event):

        contextMenu = QMenu(self)

        newAct  = contextMenu.addAction("New")
        openAct = contextMenu.addAction("Open")
        quitAct = contextMenu.addAction("Quit")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            print("Start to quit due to quit actions ")
            self.close()
            # 实际上是按右键显示这些弹出式菜单

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

```
#
####  last update on the ContextMenu  2018-06-07
#
#   QCheckMenu example 
```

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QStatusBar,QPushButton,QWidget,QAction, QMenu, QMenuBar

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "QCheckBar"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Message is Ready")
        # 可以看到状态栏更新上面的消息
        menubar = self.menuBar()
        viewMemu = menubar.addMenu("View")

        viewAction = QAction("View Status",self,checkable = True)
        viewAction.setChecked(True)
        viewAction.setStatusTip("View StatusBar11111111")
        viewAction.triggered.connect(self.toggleMenu)

        viewMemu.addAction(viewAction)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
    def toggleMenu(self,state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    def AddMessage(self):
        self.statusBar().showMessage("the button is clicked")
App =QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
##  菜单下面的可以check或者uncheck 
### last update on 2018-06-07
## 
# 工具条实例
# 注意工具条中槽函数的实现
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QAction
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 ToolBars "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):

        exitAct = QAction(QIcon("Icons/quit.gif"),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.ClossApp)
        # triggered.connect连接到槽函数 ，让槽函数实现要做的功能


        copyAct =  QAction(QIcon("Icons/copy.gif"),'Copy',self)
        copyAct.setShortcut('Ctrl+C')

        pasteAct = QAction(QIcon("Icons/paste.gif"), 'Paste', self)
        pasteAct.setShortcut('Ctrl+V')

        deleteAct = QAction(QIcon("Icons/delete.gif"), 'Delete', self)
        deleteAct.setShortcut('Ctrl+D')

        self.toolbar = self.addToolBar("ToolBar")
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)
        self.toolbar.addAction(deleteAct)




        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def ClossApp(self):
        self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
##
#### last update on 2018-06-07 15:35


# QLineEdit Example 
## 

# QLineEdit Example 
## 要注意中文切换后会导致一些标点符后有问题，因此尽量不要左右切换中英，最好先用英文调试好后再修改！
```

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QMessageBox,QLineEdit,QPushButton

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "QLineEdit Example "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.lineedit = QLineEdit(self)
        self.lineedit.move(200,200)
        self.lineedit.resize(280,40)
        # resize 用于定制尺寸的大小

        self.button = QPushButton("show Text",self)
        self.button.move(270,250)
        self.button.clicked.connect(self.onClick)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def onClick(self):
        textValue = self.lineedit.text()
        QMessageBox.question(self,"Line Edit","you have input with message : "+ textValue,QMessageBox.Ok,QMessageBox.Ok)
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```
##
##
##
#  PyQT5 Example 16  with position ,move functions 
```
import sys
from PyQt5 import QtGui,QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QFrame

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Widgets Positions"
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.label1 = QLabel("<font color=red>定值2</font>",self)
        self.label1.move(50,50)
        self.label1.resize(50,50)
        # self.label1.setStyleSheet("color:red")
        self.label1.setFrameStyle( QtWidgets.QFrame.Panel|QtWidgets.QFrame.WinPanel)
        self.label1.setFrameShape(QtWidgets.QFrame.Box)

        self.label2 = QLabel("Please2 ", self)
        self.label2.move(100, 100)
        self.label2.resize(50, 50)
        self.label2.setFrameShape(QtWidgets.QFrame.Box)
        # some help on the link https://www.jianshu.com/p/70c0fb2e5fc4


        self.label3 = QLabel("Please3 ", self)
        self.label3.move(150, 150)
        self.label3.resize(50, 50)
        self.label3.setFrameStyle( QtWidgets.QFrame.Panel|QtWidgets.QFrame.Sunken )

        self.label4 = QLabel("Please 4", self)
        self.label4.move(200, 200)
        self.label4.resize(50, 50)
        self.label4.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Raised)



        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```
##
##
##
# PyQT5 Example 17  with Layout and GroupBox 
```

import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QPushButton,QMessageBox,QVBoxLayout,QHBoxLayout,QGroupBox

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 Layout Example "
        self.top =200
        self.left =200
        self.width = 300
        self.height =200
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.HorizontalLayout()
        vBox =QVBoxLayout()
        vBox.addWidget(self.gbx)
        self.setLayout(vBox)
        self.show()
    def HorizontalLayout(self):
        self.gbx = QGroupBox("What is your Favorite Sport?")
        hbxLayout = QHBoxLayout()
        btn1 = QPushButton("Football")
        btn2 = QPushButton("Cricket")
        btn3 = QPushButton("Tennis")

        hbxLayout.addWidget(btn1)
        hbxLayout.addWidget(btn2)
        hbxLayout.addWidget(btn3)
        self.gbx.setLayout(hbxLayout)

        btn1.clicked.connect(self.btn1Clicked)

    def btn1Clicked(self):
        QMessageBox.information(self,"Football","Yes, I Like Football")




App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

```
###
###
# PyQT5 Example 18  Grid Layout 
## 注意容器间的 包含关系，这个要特别注意的地方
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog,QGridLayout,QGroupBox,QPushButton,QVBoxLayout

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 GridLayout Example "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)

        self.gridlayoutcreateion()
        vboxlayout =QVBoxLayout()
        vboxlayout.addWidget(self.gbx)
        self.setLayout(vboxlayout)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def gridlayoutcreateion(self):
        self.gbx = QGroupBox("Grid Layout Example")
        gridlayout = QGridLayout()
        gridlayout.addWidget(QPushButton('1'),0,0)
        gridlayout.addWidget(QPushButton('2'), 0, 1)
        gridlayout.addWidget(QPushButton('3'), 0, 2)

        gridlayout.addWidget(QPushButton('4'), 1, 0)
        gridlayout.addWidget(QPushButton('5'), 1, 1)
        gridlayout.addWidget(QPushButton('6'), 1, 2)

        gridlayout.addWidget(QPushButton('7'), 2, 0)
        gridlayout.addWidget(QPushButton('8'), 2, 1)
        gridlayout.addWidget(QPushButton('9'), 2, 2)

        self.gbx.setLayout(gridlayout)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


```
#
#
# Example of PyQT5 19 QcheckBox 
### 让QLable和QCheckBox的文本显示全的一个函数 self.label1.adjustSize()
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QCheckBox
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT 5  QCheckBox Example "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        self.checkbox = QCheckBox("Do you like Football? ",self)
        self.checkbox.move(100,100)
        # self.checkbox.
        self.checkbox.toggle()
        self.checkbox.adjustSize()
        self.checkbox.stateChanged.connect(self.checkBoxChange)

        self.label1 = QLabel("Hello",self)
        self.label1.adjustSize()
        self.label1.move(120,150)
        self.label1.showNormal()
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def checkBoxChange(self,state):
        if state == Qt.Checked:
            self.label1.setText("Yes ,I like FootBall")
            self.label1.adjustSize()
        else:
            self.label1.setText("NO ,I dont like FootBall")
            self.label1.adjustSize()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

```
### 在修改了文本后要设置 adjustSize才能会显示全文本内容，否则会有显示问题
##
# PyQT5 20 Example SpinBox 
```
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QSpinBox,QLabel,QVBoxLayout
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQT5 QSpinBox Example "
        self.top =200
        self.left =200
        self.width = 600
        self.height =500
        # self.InitUI()

        self.InitUI()
    def InitUI(self):
        VBoxLayout = QVBoxLayout()
        self.label1 = QLabel("Current Value",self)
        self.label1.adjustSize()
        #self.label1.setWordWrap(True)

        self.label1.move(60,60)
        VBoxLayout.addWidget(self.label1)

        self.spinbox = QSpinBox(self)
        self.spinbox.move(60,10)
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(20)
        # 设置最大值，最小值，可以是负数呵！
        # 如果要设置浮点数，可以用QDoubleSpinBox
        VBoxLayout.addWidget(self.spinbox)
        self.spinbox.valueChanged.connect(self.changespinvalue)

        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
    def changespinvalue(self):
        self.label1.setText("Current Vaule:" +str(self.spinbox.value()))
        self.label1.adjustSize()
        # 解决label文本变更后内容显示不全的问题

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


``` 

