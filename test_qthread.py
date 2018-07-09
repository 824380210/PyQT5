import sys
import time
import logging
import subprocess
from PyQt5.QtGui import  QPixmap,QTextCursor
from PyQt5.QtCore import Qt,QThread,pyqtSignal,QTimer
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel, QPushButton,QTextEdit,QGroupBox, QWidget,QVBoxLayout, QHBoxLayout

class x86_main(QWidget):
    """
    define the UI

    """
    def __init__(self):
        super(x86_main, self).__init__()
        self.setWindowTitle("X86 服务器测试系统 v0.1 版")
        self.check_warnning_text = """ 
        注意：
        检查检测的配置与实际是否相符
        注意机器前后的LED灯是否正常（正常通常为蓝色或者绿色）
               
        """
        self.check_basic_info = True
        self.SetupUI()
        self.showMaximized()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()
        self.updatemsg( "现在开始AVT 测试")
        result = self.get_basic_info()
        print(result)
        self.brand_text.setText(result[0])
        self.updatemsg(result[0])
        self.mt_text.setText(result[1])
        self.updatemsg(result[1])
        self.sn_text.setText(result[2])
        self.updatemsg(result[2])
        # self.paintEvent11("abc")
    def get_basic_info(self):
        info = []
        cmd1 = ' dmidecode -s   system-manufacturer '
        cmd2 = ' dmidecode -s   system-product-name | cut -d[ -f2|cut -d ] -f1'
        cmd3 = ' dmidecode -s   system-serial-number '
        a = subprocess.check_output(cmd1,shell=True)
        b = subprocess.check_output(cmd2, shell=True)
        c = subprocess.check_output(cmd3, shell=True)
        new_a = a.decode('utf-8').strip()
        new_b = b.decode('utf-8').strip()
        new_c = c.decode('utf-8').strip()

        #print(a,b,c)
        return [new_a,new_b,new_c]






    def SetupUI(self):
        self.basic_info()
        self.fw_version()
        self.main_info()
        self.final_buttons()
        layout = QVBoxLayout()
        title_text = '<center><H1>X86 服务器测试系统 </H1></center>'
        self.my_title = QLabel(title_text)
        layout.addWidget(self.my_title)
        layout.addWidget(self.basic_info_groupbox)
        layout.addWidget(self.fw_version_groupbox)
        layout.addWidget(self.main_info_groupbox)
        layout.addWidget(self.final_button_groupbox)
        self.setLayout(layout)

        # basic_info_groupbox = QGroupBox(" 基本信息：")
        # fw_version_info_groupbox = QGroupBox("版本信息：")
        # general_info_groupbox = QGroupBox()
        # hw_info_groupbox =QGroupBox("发现的硬件基本信息（可能不全呵！")
        # log_groupbox = QGroupBox("日志信息:")
        # layout =QH

    def basic_info(self):
        self.basic_info_groupbox = QGroupBox(" 基本信息：")
        layout = QHBoxLayout()
        my_brand = QLabel("品牌：")
        self.brand_text  = QLabel()
        my_mt = QLabel("机型：")
        self.mt_text = QLabel()
        my_sn = QLabel("流水号：")
        self.sn_text = QLabel()
        my_time = QLabel("当前时间： ")
        self.time_text = QLabel()
        layout.addWidget(my_brand)
        layout.addWidget(self.brand_text)
        layout.addWidget(my_mt)
        layout.addWidget(self.mt_text)
        layout.addWidget(my_sn)
        layout.addWidget(self.sn_text)
        layout.addWidget(my_time)
        layout.addWidget(self.time_text)
        self.basic_info_groupbox.setLayout(layout)
    def fw_version(self):
        self.fw_version_groupbox = QGroupBox("版本信息")
        self.uefi_version = QLabel("UEFI Version")
        self.bmc_version = QLabel("BMC version ")
        layout = QHBoxLayout()
        layout.addWidget(self.uefi_version)
        layout.addWidget(self.bmc_version)
        self.fw_version_groupbox.setLayout(layout)
    def main_info(self):
        self.hw_configure()
        self.log_show()
        self.main_info_groupbox = QGroupBox()
        layout= QHBoxLayout()
        layout.addWidget(self.hw_configure_group)
        layout.addWidget(self.log_show_groupbox)
        self.main_info_groupbox.setLayout(layout)

    def hw_configure(self):
        self.hw_configure_group = QGroupBox("已发现的硬件有：")
        self.my_cpu = QLabel("CPU xxxxx")
        self.my_mem = QLabel("MEM xxxxx")
        self.my_raid_controller = QLabel("RAID controller ")
        self.other_HW = QLabel("other HW")
        self.hw_config_info = QTextEdit()

        self.check_warnning = QLabel()
        self.check_warnning.setText(self.check_warnning_text)
        layout = QVBoxLayout()
        layout.addWidget(self.hw_config_info)
        layout.addWidget(self.my_cpu)
        layout.addWidget(self.my_mem)
        layout.addWidget(self.my_raid_controller)
        layout.addWidget(self.other_HW)
        # layout.addWidget(self.hw_config_info)
        layout.addWidget(self.check_warnning)
        self.hw_configure_group.setLayout(layout)
    def log_show(self):
        self.log_show_groupbox = QGroupBox("测试日志")
        self.log_text = QTextEdit()
        layout = QHBoxLayout()
        layout.addWidget(self.log_text)
        self.log_show_groupbox.setLayout(layout)
    def final_buttons(self):
        self.final_button_groupbox = QGroupBox()
        layout = QHBoxLayout()
        self.avt_config_save = QPushButton("保存AVT测试结果")
        self.do_next_preload = QPushButton("进行下一步灌软")
        self.quit_with_save = QPushButton("退出")
        layout.addWidget(self.avt_config_save)
        layout.addWidget(self.do_next_preload)
        layout.addWidget(self.quit_with_save)
        self.final_button_groupbox.setLayout(layout)

    def update_time(self):
        time_info = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.time_text.setText(time_info)

    def updatemsg(self,msg ):
        time_info = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.msg =  time_info + "\t" + msg
        self.log_text.moveCursor(QTextCursor.End)
        self.log_text.append(self.msg)
        #self.testlog.update()
        return
    def paintEvent(self,event):
        if self.check_basic_info:
            # self.updatemsg("开始读取BIOS信息")
            # time.sleep(5)
            # self.updatemsg("确认品牌")
            # time.sleep(0.5)
            # self.updatemsg("发现机型")
            # time.sleep(0.5)
            # self.updatemsg("得到流水号")
            # time.sleep(0.5)
            msg = "进入后台数据处理模式 "
            #logging.info(msg)
            self.updatemsg(msg)
            self.subthread = mythread()
            self.subthread.mysignal_str.connect(self.updatemsg, type=Qt.QueuedConnection)
            # self.subthread.mysignal_int.connect(self.enable_button, type=Qt.QueuedConnection)
            # self.subthread.mysignal_list.connect(self.data_process, type=Qt.QueuedConnection)
            self.sub2thread = my2thread()
            self.sub2thread.mysignal_str.connect(self.updatemsg, type=Qt.QueuedConnection)
            self.subthread.start()
            self.sub2thread.start()
            self.check_basic_info = False


class mythread(QThread):
    #list  = list
    #mysignal = pyqtSignal(list)
    mysignal_str  = pyqtSignal(str)
    mysignal_int  = pyqtSignal(int)
    mysignal_list = pyqtSignal(list)
    #
    def __init__(self):
        super(mythread,self).__init__()
        # self.args = args
    #
    def run(self):
        # 0 for cable link  check
        # 1 for Link speed check
        # 2 for the interface self test check
        # 3 for the ping test
        # 4 for the interface bandwidth test
        self.mysignal_int.emit(0)
        msg = "1后台数据处理中..."
        self.mysignal_str.emit(msg)
        #print(self.args)
        #
        #

        for a in range(50):
            msg = "1数据处理中，在处理数据项第{}项".format(a)
            self.mysignal_str.emit(msg)
            time.sleep(1)
class my2thread(QThread):
    #list  = list
    #mysignal = pyqtSignal(list)
    mysignal_str  = pyqtSignal(str)
    mysignal_int  = pyqtSignal(int)
    mysignal_list = pyqtSignal(list)
    #
    def __init__(self):
        super(my2thread,self).__init__()
        # self.args = args
    #
    def run(self):
        # 0 for cable link  check
        # 1 for Link speed check
        # 2 for the interface self test check
        # 3 for the ping test
        # 4 for the interface bandwidth test
        self.mysignal_int.emit(0)
        msg = "2后台数据处理中..."
        self.mysignal_str.emit(msg)
        #print(self.args)
        #
        #

        for a in range(50):
            msg = "2数据处理中，在处理数据项第{}项".format(a)
            self.mysignal_str.emit(msg)
            time.sleep(1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Icons/run.png"))
    form = x86_main()
    form.show()
    sys.exit(app.exec_())





