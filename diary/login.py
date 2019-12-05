
# # -*- coding: utf-8 -*-

import tkinter
import tkinter.messagebox
from tkinter import ttk 

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
		self.verifyCodeTxt = tkinter.Entry(self.root, textvariable=VerifyCodeStr)
		self.verifyCodeTxt.grid(row=1, column=0)
		VerifyCodeStr.set("Verify Code")

		GetCodeBtn = tkinter.Button(self.root, text="get", command=self.getCode)
		GetCodeBtn.grid(row=1,column=1)
		
		LoginBtn = tkinter.Button(self.root, text="Login", command=self.login)
		LoginBtn.grid(row=2,column=0,pady = 10)

		# 创建下拉菜单
		self.cmb = ttk.Combobox(self.root,state='readonly')
		self.cmb['value'] = ('上海','北京','天津','广州')
		self.cmb.current(0)
		self.cmb.grid(row=3,column=0,pady=10)
		self.cmb.bind("<<ComboboxSelected>>",self.comboboxSelected)
		pass

	def login(self):
		print("+++++++++++Login",self.phoneNumStr.get())
		pass

	def getCode(self):
		tkinter.messagebox.showinfo(title='VerifyCode', message='your VerifyCode is 123456') 
		print("+++++++++++getCode")
		pass
	def comboboxSelected(self,*args):
		print("+++++:",self.cmb.get())
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
