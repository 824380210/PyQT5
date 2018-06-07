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
