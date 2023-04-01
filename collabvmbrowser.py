from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5 import QtGui
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://computernewb.com/collab-vm/")) #Main WebPage For The Browser
        #self.browser.urlChanged.connect(self.update_urlbar) # Does Not Work Due To No URLBar 
        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        
        self.setWindowIcon(QtGui.QIcon('logo.png'))

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back To Previous Page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward To Next Page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload Webpage")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.setStatusTip("VMs Page")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        madeby_btn = QLabel("Created By: CaliforniaX | CollabVM Browser 1.0")
        navtb.addWidget(madeby_btn)

        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("% s - CollabVM Browser" % title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://computernewb.com/collab-vm/"))

app = QApplication(sys.argv)
app.setApplicationName("CollabVM Browser")
window = MainWindow()
app.exec_()
