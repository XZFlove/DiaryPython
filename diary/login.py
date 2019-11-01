
# # -*- coding: utf-8 -*-

import tkinter

class Login(object):
	def __init__(self, arg):
		super(Login, self).__init__()
		self.root = arg
		self.create_widgets()

		pass

	def create_widgets(self):
		self.phoneNumStr = tkinter.Variable()
		phoneNumTxt = tkinter.Entry(self.root, textvariable=self.phoneNumStr)
		phoneNumTxt.grid(row=0, column=0, pady=10, padx=10)
		self.phoneNumStr.set("Phone Number")

		VerifyCodeStr = tkinter.Variable()
		VerifyCodeTxt = tkinter.Entry(self.root, textvariable=VerifyCodeStr)
		VerifyCodeTxt.grid(row=1, column=0)
		VerifyCodeStr.set("Verify Code")

		GetCode = tkinter.Button(self.root, text="get", command=lambda: print("code:123456"))
		GetCode.grid(row=1,column=1)
		# button2.pack()

		LoginBtn = tkinter.Button(self.root, text="Login", command=self.login)
		LoginBtn.grid(row=2,column=0,pady = 10)
		pass

	def login(object):

		pass

	pass


root = tkinter.Tk()
# 设置标题
root.title("Jerry's Diary")
# 设置大小和位置
root.geometry("300x400+200+50")
# 进制拉升
root.resizable(width=False, height=False)

Login = Login(root)
root.mainloop()