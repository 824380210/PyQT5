# 代码第一例
[视频](https://www.youtube.com/watch?v=pnpL9Sl79g8&index=1&list=PL1FgJUcJJ03uwFW8ys2ov2dffKs3ieGYk)

## 参考代码 

```
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height =500
        self.setWindowIcon(QtGui.QIcon("xx.png"))
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())

```
## 学习总结

```
1: super()__init__() 
2: 在红帽不同版本可能显示不一样

```


---
#  第二例  QDate ，QTime,QDateTime 


```
from PyQt5.QtCore import QDateTime,Qt,QDate,QTime

datetime = QDateTime.currentDateTime()
print(datetime.toString())
print(datetime.toString(Qt.ISODate))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print("Today Date and Time is :" + datetime.toString(Qt.ISODate))
print("Adding 12 days to the Date {}".format(datetime.addDays(12).toString()))
print("subtracting 25 days :{}".format(datetime.addDays(-25).toString()))
print("subtracting 25 days :{}".format(datetime.addDays(-25).toString(Qt.ISODate)))
print("Adding 50 seconds to the Date {}".format(datetime.addSecs(50).toString()))
print("Adding 3 monthes : to the date : {}".format(datetime.addMonths(3).toString()))
date = QDate.currentDate()
print(date.toString())
print(date.toString(Qt.ISODate))
print(date.toString(Qt.DefaultLocaleLongDate))
time = QTime.currentTime()
print(time.toString())
print(time.toString(Qt.ISODate))
print(time.toString(Qt.DefaultLocaleLongDate))

```

## 显示结果 ： win10版本 

```
周二 6月 5 13:47:30 2018
2018-06-05T13:47:30
2018年6月5日 13:47:30
Today Date and Time is :2018-06-05T13:47:30
Adding 12 days to the Date 周日 6月 17 13:47:30 2018
subtracting 25 days :周五 5月 11 13:47:30 2018
subtracting 25 days :2018-05-11T13:47:30
Adding 50 seconds to the Date 周二 6月 5 13:48:20 2018
Adding 3 monthes : to the date : 周三 9月 5 13:47:30 2018
周二 6月 5 2018
2018-06-05
2018年6月5日
13:47:30
13:47:30
13:47:30
```
## 显示结果： linux版本

```
[root@n04 pyqt5]#python3.6 pyqt5_2.py
Tue Jun 5 01:48:35 2018
2018-06-05T01:48:35
Tuesday, June 5, 2018 1:48:35 AM EDT
Today Date and Time is :2018-06-05T01:48:35
Adding 12 days to the Date Sun Jun 17 01:48:35 2018
subtracting 25 days :Fri May 11 01:48:35 2018
subtracting 25 days :2018-05-11T01:48:35
Adding 50 seconds to the Date Tue Jun 5 01:49:25 2018
Adding 3 monthes : to the date : Wed Sep 5 01:48:35 2018
Tue Jun 5 2018
2018-06-05
Tuesday, June 5, 2018
01:48:35
01:48:35
1:48:35 AM EDT

```
#  第三例  UTC时间与当地时间转换


```
from PyQt5.QtCore import QDateTime,Qt
datetime = QDateTime.currentDateTime()
print("the local Date and time is "+ datetime.toString(Qt.DefaultLocaleLongDate))
print("UTC time is "+datetime.toUTC().toString())
print("the offset from UTC is {}:seconds".format(datetime.offsetFromUtc()))

```
# 显示结果

```
the local Date and time is 2018年6月5日 14:01:49
UTC time is 周二 6月 5 06:01:49 2018 GMT
the offset from UTC is 28800:seconds

```
#  第四例  时间显示每月/每年有多少天

```
from PyQt5.QtCore import QDate

date = QDate.currentDate()

d = QDate(2017,12,23)

print("Days in A Month:{}".format(d.daysInMonth()))
print("Days in A Year:{}".format(d.daysInYear()))
```
# 显示结果

```
Days in A Month:31
Days in A Year:365

```
#  第五例  时间显示每月/每年有多少天

```
参考第二个例子即可
datetime.addMonths(3)

```
#  第六例  QPushButton ,QToolTips

```
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import  QMainWindow,QApplication,QPushButton,QToolTip

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self .title = "PyQT5 Push Button"
        self.left =100
        self.top=100
        self.width=680
        self.height=540
        self.setWindowIcon(QtGui.QIcon("icons/run.png"))
        button=QPushButton("Click me",self)
        button.move(200,200)
        button.setToolTip("<h3>This is a help message here for user only</h3>")
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
# 第七例 信号与槽


```
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import  QMainWindow,QApplication,QPushButton,QToolTip
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self .title = "PyQT5 Push Button"
        self.left =100
        self.top=100
        self.width=680
        self.height=540
        self.setWindowIcon(QtGui.QIcon("Icons/run.png"))
        self.button=QPushButton("Click me",self)
        self.button.move(200,200)
        self.button.setToolTip("<h3>click me to close the App </h3>")
        self.button.clicked.connect(self.Close)
        # self.button.clicked.connect(self.close)
        # mainWindow.close()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
    def Close(self):
        print("I was call here")
        QCoreApplication.instance().quit()

        # 这个是系统 专有的信号吧

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```
# 第八例 ，增强版信号与槽 ，在按下关闭按钮是弹出对话框yes/no


```
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import  QMainWindow,QApplication,QPushButton,QToolTip,QMessageBox
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self .title = "PyQT5 Push Button"
        self.left =100
        self.top=100
        self.width=680
        self.height=540
        self.setWindowIcon(QtGui.QIcon("Icons/run.png"))
        self.button=QPushButton("Click me",self)
        self.button.move(200,200)
        self.button.setToolTip("<h3>click me to close the App </h3>")
        self.button.clicked.connect(self.CloseApp)
        # self.button.clicked.connect(self.close)
        # mainWindow.close()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
    def Close(self):
        print("I was call here")
        QCoreApplication.instance().quit()
    def CloseApp(self):
        reply = QMessageBox.question(self,"CLose Message","Are you sure to close Windows",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            # 在这里可以添加其他动作，如保存文件，注意要在self.close前做呵！



        # 这个是系统 专有的信号吧

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```

# 第九例 ，更多关于QMessagebox的用法 

```
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import  QMainWindow,QApplication,QPushButton,QToolTip,QMessageBox
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self .title = "PyQT5 Push Button"
        self.left =100
        self.top=100
        self.width=680
        self.height=540
        self.setWindowIcon(QtGui.QIcon("Icons/run.png"))
        self.button=QPushButton("Click me",self)
        self.button.move(100,100)
        self.button.setToolTip("<h3>click me to close the App </h3>")
        self.button.clicked.connect(self.CloseApp)
        self.button1=QPushButton("about message",self)
        self.button1.move(100,150)
        self.button1.clicked.connect(self.AboutMessage)
        self.button2=QPushButton("Question",self)
        self.button2.move(100,200)
        self.button2.clicked.connect(self.QuestionMessage)
        # self.button.clicked.connect(self.close)
        # mainWindow.close()
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
    def AboutMessage(self):
        QMessageBox.about(self,"About Message","this is infor mations about the about message ")
    def Close(self):
        print("I was call here")
        QCoreApplication.instance().quit()
    def CloseApp(self):
        reply = QMessageBox.question(self,"CLose Message","Are you sure to close Windows",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    def QuestionMessage(self):
        message = QMessageBox.question(self,"my question is ","pay for this video ",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if message == QMessageBox.Yes:
            print("Yes ,good luck")
        else:
            print ("no good luck to me ")


        # 这个是系统 专有的信号吧

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
```

### 定义的时候要严格按照首字母大写的形式来写函数名称


### 

# 


```

```
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QStatusBar,QPushButton

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "QStatus Bar"
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
        self.statusBar().showMessage("This is a simple status bar")
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
### 注意初始化前要加入所有控件 
```

