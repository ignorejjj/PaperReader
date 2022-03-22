import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6 import QtCore,QtGui
from spider import Spider
from my_windows.main_window import Ui_MainWindow
import qdarkstyle    
from utils import split_list,simplify
from selenium import webdriver

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        """"初始化各个标签"""
        for i in range(4):
            self.__dict__['title{}'.format(i+1)].setText("")
            self.__dict__['author{}'.format(i+1)].setText("")
            self.__dict__['conf{}'.format(i+1)].setText("")
        self.currentPage = 0
        self.pagedata = None

        """跳转菜单"""
        self.pushButton_6.clicked.connect(self.to_page1)
        self.pushButton_4.clicked.connect(self.to_page3)

        """文献检索下载功能对应函数"""
        self.pushButton.clicked.connect(self.search_paper)
        # 绑定下载按钮对应函数,i代表第i个按钮
        for i in range(1,5):
            self.__dict__['downloadButton{}'.format(i)].clicked.connect(lambda: self.to_downurl(i))   
            self.__dict__['paperButton{}'.format(i)].clicked.connect(lambda: self.to_paperurl(i))
        # 跳转搜索页面
        self.pushButton_2.clicked.connect(self.to_nextpage)
        self.pushButton_3.clicked.connect(self.to_lastpage)

        """参考文献检索功能对应函数"""
        # 绑定参考文献检索函数
        self.pushButton_7.clicked.connect(self.search_bib)

        """美化界面"""
        self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) # 隐藏边框
        self.pushButton_4.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
        QPushButton:hover{background:red;}''')
        self.pushButton_6.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
        QPushButton:hover{background:red;}''') 
        #self.pushButton_14.clicked.connect(MainWindow.exit)

    ''' def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  #更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)#更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) '''


    def to_page1(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def to_page2(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def to_page3(self):
        self.stackedWidget.setCurrentIndex(2)
        

    # 根据关键词查询论文
    def search_paper(self):
        keyword = self.lineEdit.text()
        res = self.spider.search_paper(keyword)
        # 未查询到结果,进行弹窗
        if len(res) == 0:
            print("暂时空着")
            #self.Child_window =  
        # 将数据拆成每四个一个list:[[p1,p2,p3,p4],[p5,p6,p7,p8],..]，便于每页展示
        res = split_list(res, n = 4)
        self.pagedata = res
        self.currentPage = 0
        # 对显示页面进行展示
        self.set_searchpage(res[self.currentPage])

    # 根据传入data对页面进行展示
    # data: [p1,p2,p3,p4]
    def set_searchpage(self, data):
        for i in range(4):
            item = data[i]
            self.__dict__['title{}'.format(i+1)].setText(item['title'])
            authors = "".join([name for name in item['author']])
            self.__dict__['author{}'.format(i+1)].setText(authors)
            self.__dict__['conf{}'.format(i+1)].setText(item['journal_name'])
     
    
    # 点击下载按钮后跳转到对应链接(文献检索页面)
    # n为点击的按钮序号
    def to_downurl(self, n):
        data = self.pagedata[self.currentPage][n-1]
        url = data['pdf_url']
        # 检验地址是否有效
        if url[:4] != "http":
            print("暂时空着")
            return 
            # 后续补充下载源scihub
            #self.Child_window =
        driver = webdriver.Chrome()
        driver.get(url)
    
    # 点击文章链接按钮后跳转到对应链接(文献检索页面)
    def to_paperurl(self, n):
        data = self.pagedata[self.currentPage][n-1]
        url = data['paper_url']
        # 检验地址是否有效
        if url[:4] != "http":
            print("暂时空着")
            return 
            #self.Child_window =
        driver = webdriver.Chrome()
        driver.get(url)

    # 在搜索页面跳转到下一页(文献检索页面)
    def to_nextpage(self):
        page_num = len(self.pagedata)
        # 已经是最后一页
        if self.currentPage+1 == page_num:
            print("已经到最后一页")
            return
            # 加入弹窗
        self.currentPage += 1
        self.set_searchpage(data = self.pagedata[self.currentPage])

    # 在搜索页面跳转到上一页(文献检索页面)
    def to_lastpage(self):    
        # 已经是最后一页
        if self.currentPage < 1:
            print("已经到第一页")
            return
            # 加入弹窗
        self.currentPage -= 1
        self.set_searchpage(data = self.pagedata[self.currentPage])

    
    # 参考文献检索并下载bib
    def search_bib(self):
        search_name = self.lineEdit_2.text()
        # 对search_name 进行简化
        #search_name = simplify(search_name)
        ref_names = self.spider.get_ref(search_name)
        # 设置展示表格
        self.tableWidget.setRowCount(len(ref_names))
        for i,name in enumerate(ref_names):
            new = QTableWidgetItem(name)
            self.tableWidget.setItem(i,0,new)

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    spider = Spider()
    my_win = MyWindow()
    my_win.spider = spider
    my_win.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    my_win.show()
    sys.exit(app.exec_())