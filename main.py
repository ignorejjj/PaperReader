import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6.QtGui import * 
from PySide6 import QtCore,QtGui
from spider import Spider
from my_windows.main_window import Ui_MainWindow
import qdarkstyle    
from utils import split_list
from selenium import webdriver
import pdfplumber

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.m_flag = False

        """Initialize each label"""
        for i in range(4):
            self.__dict__['title{}'.format(i+1)].setText("")
            self.__dict__['author{}'.format(i+1)].setText("")
            self.__dict__['conf{}'.format(i+1)].setText("")
        self.currentPage = 0
        self.pagedata = None

        self.pushButton_6.clicked.connect(self.to_page1)
        self.pushButton_4.clicked.connect(self.to_page3)

        """Correspondence function of document retrieval function"""
        self.pushButton.clicked.connect(self.search_paper)
        self.paperButton1.clicked.connect(lambda: self.to_paperurl(1))
        self.paperButton2.clicked.connect(lambda: self.to_paperurl(2))
        self.paperButton3.clicked.connect(lambda: self.to_paperurl(3))
        self.paperButton4.clicked.connect(lambda: self.to_paperurl(4))
        self.pushButton_2.clicked.connect(self.to_nextpage)
        self.pushButton_3.clicked.connect(self.to_lastpage)

        """Corresponding function of reference retrieval function"""
        self.pushButton_7.clicked.connect(self.search_bib)
        self.pushButton_8.clicked.connect(self.get_file_title)

        """Beautify the interface"""
        self.setWindowOpacity(0.9) 
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint) 
        self.pushButton_4.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
        QPushButton:hover{background:red;}''')
        self.pushButton_6.setStyleSheet('''QPushButton{background:#F76677;border-radius:15px;}
        QPushButton:hover{background:red;}''') 


    def mousePressEvent(self, event):
        if event.button()==QtCore.Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() 
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  

    def mouseMoveEvent(self, QMouseEvent):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor)) 


    def to_page1(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def to_page2(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def to_page3(self):
        self.stackedWidget.setCurrentIndex(2)
        

    # Query papers according to keywords
    def search_paper(self):
        keyword = self.lineEdit.text()
        res = self.spider.search_paper(keyword)
        res = split_list(res, n = 4)
        self.pagedata = res
        self.currentPage = 0
        # display page
        self.set_searchpage(res[self.currentPage])

    # Display the page according to the incoming data
    def set_searchpage(self, data):
        """
        Args:
            data: [paper1,paper2,paper3,paper4]
        """
        for i in range(4):
            item = data[i]
            self.__dict__['title{}'.format(i+1)].setText(item['title'])
            authors = "".join([name for name in item['author']])
            self.__dict__['author{}'.format(i+1)].setText(authors)
            self.__dict__['conf{}'.format(i+1)].setText(item['journal_name'])
         
    # Jump to the corresponding paper home page
    def to_paperurl(self, n):
        data = self.pagedata[self.currentPage][n-1]
        url = data['paper_url']
        # 检验地址是否有效
        if url[:4] != "http":
            print("地址无效!")
            return 
        driver = webdriver.Chrome()
        driver.get(url)

    # Jump to the next page on the search page (literature search page)
    def to_nextpage(self):
        page_num = len(self.pagedata)
        if self.currentPage+1 == page_num:
            print("已经到最后一页")
            return
        self.currentPage += 1
        self.set_searchpage(data = self.pagedata[self.currentPage])

    # Jump to the last page on the search page (literature search page)
    def to_lastpage(self):    
        if self.currentPage < 1:
            print("已经到第一页")
            return          
        self.currentPage -= 1
        self.set_searchpage(data = self.pagedata[self.currentPage])
    
    # Search references and download bib files
    def search_bib(self):
        search_name = self.lineEdit_2.text()
        ref_names = self.spider.get_ref(search_name)
        # Set presentation table
        self.tableWidget.setRowCount(len(ref_names))
        for i,name in enumerate(ref_names):
            new = QTableWidgetItem(name)
            self.tableWidget.setItem(i,0,new)

    # Obtain the title of the paper from the PDF file and fill it in the input box
    def get_file_title(self):
        pdfPath, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", "./", "*.*")
        with pdfplumber.open(pdfPath) as pdf:
            page01 = pdf.pages[0] 
            text = page01.extract_text()
            title = text.split("\n")[0]
        self.lineEdit_2.setText(title)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    spider = Spider()
    my_win = MyWindow()
    my_win.spider = spider
    my_win.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    my_win.show()
    sys.exit(app.exec_())