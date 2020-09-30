
import sys

from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        # 添加一个按钮
        self.button1 = QPushButton('退出程序')
        self.button1.clicked.connect(self.onClick_Button)# 把按钮的单击信号绑定到槽函数上

        # 设置一个布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # 创建一个主框架,就是一个应用程序(一个程序可以有多个窗口,也可以没有窗口)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)


    # 定义一个槽,其实就是按钮单击事件的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        app.quit()

# 这个基本是固定的
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # app.setWindowIcon(QIcon('./'))# 窗口图标路径
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())






