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
