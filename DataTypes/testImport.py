'''
from PIL import ImageFilter,Image
import requests
r = requests.get('https://www.baidu.com')
print(r.status_code)





im = Image.open('soee.png')
w,h = im.size
print('Original image size: %sx%s' % (w, h))

# 缩放50%
# im.thumbnail((w//2, h//2))
# im.save('thumbnail.jpg', 'jpeg')


im = Image.open('soee.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.png', 'png')
'''

# chardet
'''
import chardet
print(chardet.detect(b'Hello,world!'))
'''
# psutil 运维用 获取电脑信息

'''
virtualenv
在开发Python应用程序的时候，
系统安装的Python3只有一个版本：3.4。
所有第三方的包都会被pip安装到Python3的site-packages目录下。
如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，
就是安装在系统的Python 3。如果应用A需要jinja 2.7，
而应用B需要jinja 2.6怎么办？
这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。
virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

'''

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()


    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, %s' % name)
    # def createWidgets(self):
    #     self.helloLabel = Label(self, text='Hello,world!')
    #     self.helloLabel.pack()
    #     self.quitButton = Button(self, text='Quit', command=self.quit)
    #     self.quitButton.pack()




app = Application()
# 设置窗口标题:
app.master.title('Hello World')
#主消息循环
app.mainloop()