from tkinter import * #导入init all里的方法
from tkinter import messagebox
import urllib.request
import requests
def weather():
    #获取用户输入城市
    city=entry.get()
    if city=='':
        messagebox.showinfo('提示','请输入要查询的城市')
    else:
        city=urllib.request.quote(city)#编码
        host='https://jisutqybmf.market.alicloudapi.com/weather/query'
        method='GET'
        appcode='8c42c716b4484ee3a01e2d3fdcf1c7bf'
        querys='city='+city
        header={'Authorization':'APPCODE ' + appcode}#添加头部信息
        url=host+'?'+querys
        request=requests.get(url,headers=header).json()
        info=request['result']
        citys = urllib.request.unquote(city)
        list.delete()#清除上次查询结果
        list.insert(0,citys)
        list.insert(1,"星期:%s"%info['week'])
        list.insert(2,"天气%s"%info['weather'])
        list.insert(3,"温度%s"%info['temp'])
        list.insert(4,"风向%s"%info['winddirect'])
        print(info)


    print(city)

root=Tk()#创建窗口
root.title('天气查询')#窗口标题
root.geometry('500x400')#窗口大小设置里面是小写x
root.geometry('+500+300')#窗口显示位置设置前面是左右后面是上下
#root.geometry('500x400+500+300')
lable=Label(root,text='输入要查询的城市名字',font=('微软雅黑',10))#标签控件
lable.grid()#将控件显示出来  网格式的布局
entry=Entry(root,font=('微软雅黑',20))#输入框
entry.grid(row=0,column=1)#显示并定好位置
list=Listbox(root,font=('楷体',15),width=46,height=15)#列表框控件
list.grid(row=1,columnspan=2)#显示列表框 跨列合并
button1=Button(root,text='查询',command=weather)
button1.grid(row=2,column=0,sticky=W)#sticky 对齐方式
button2=Button(root,text='退出',command=root.quit)#command 点击触发的方法
button2.grid(row=2,column=1,sticky=E)
root.mainloop()#显示窗口
