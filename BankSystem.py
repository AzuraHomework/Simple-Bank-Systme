import pickle
import random
import time
from user import user

class Bank(object):
    def __init__(self,alluser):
        self.alluser=alluser

    def CardNumber(self):#得到一个随机的卡号
        while 1:
            str=''
            for i in range(7):
                str+=chr(random.randrange(ord('0'),ord('9')))
            if not self.alluser.get(str):
                return str

    def SignUp(self):#输入姓名，密码（6位数字），确认密码，随机生成卡号（7位数字），输入预存金额（预存金额小于100开户失败）
        use=user()
        use.name=input("请输入您的姓名：")
        use.id=input("请输入您的身份证号：")
        while 1:
            use.pwd=input("请输入您的密码：")
            tmp=input("请确认您的密码：")
            if tmp==use.pwd:
                break
            else:
                print("请两次输入密码保持一致")
        while 1:
            use.money=int(input("请输入您的预存金额："))
            if use.money>=100:
                break
            else:
                print("预存金额应不少于100元")
        use.cardnum=self.CardNumber()
        self.alluser[use.cardnum]=use
        time.sleep(1)
        print('开户成功，请牢记您的卡号({})和密码'.format(use.cardnum))

    def Login(self):#输入卡号（不存在继续输入卡号），输入密码，密码错误，错误超过三次被冻结
        while 1:
            num=input('请输入您的卡号：')
            if self.alluser.get(num):
                break
            else:
                print("您输入的卡号不存在，请重新输入您的卡号：")
        flag=False
        for i in range(1,4):
            pwd=input('请输入您的密码：')
            if pwd==self.alluser[num].pwd:
                flag=True
                break
            else:
                print("您的密码输入错误，请重新输入：")
        if not flag:
            print("您的账户已被冻结，请先解锁")
        return num

    def Info(self):#查询信息
        num=self.Login()
        print('您的账户为：%s'%self.alluser[num].name)
        print('您的卡号为：%s'%self.alluser[num].cardnum)
        print('您的身份证号为：%s'%self.alluser[num].id)
        print('您的余额为：%d'%self.alluser[num].money)

    def Add(self):#存钱
        num=self.Login()
        while 1:
            AddMon=int(input('请输入存款金额：'))
            if AddMon<=0:
                print('请输入有效存款金额：')
            else:
                break
        self.alluser[num].money+=AddMon
        print('存款成功，您卡内余额为：%d'%self.alluser[num].money)

    def Minus(self):#取钱
        num=self.Login()
        while 1:
            MinusMon=int(input('请输入取款金额：'))
            if MinusMon<=0:
                print('请输入有效取款金额：')
            elif MinusMon>self.alluser[num].money:
                print('余额不足')
                print('您卡内余额为：%d'%self.alluser[num].money)
            else:
                break
        self.alluser[num].money-=MinusMon
        print('取款成功，您卡内余额为：%d' % self.alluser[num].money)

    def ModifyName(self,num):#修改账户名称
        str=input('请输入您的新账户名称：')
        self.alluser[num].name=str
        print("账户名称修改成功")

    def ModifyPwd(self,num):#修改密码
        flag=False
        for i in range(3):
            OldPwd=input('请输入密码：')
            if OldPwd==self.alluser[num].pwd:
                flag=True
                break
            print("密码错误，请重新输入")
        if flag==False:
            print("密码输入超过三次，请重新登录")
            return
        pwd=input('请输入新密码：')
        while 1:
            repwd=input('请确认您的新密码：')
            if repwd==pwd:
                break
            print('请两次输入密码保持一致')
        self.alluser[num].pwd=pwd
        print('密码修改成功')


    def ModifyId(self,num):#修改身份证号
        str=input('请输入您的新身份证号：')
        self.alluser[num].id=str
        print('身份证号修改成功')

    def Modify(self):#修改账户信息
        num=self.Login()
        print('您的账户为：%s' % self.alluser[num].name)
        print('您的卡号为：%s' % self.alluser[num].cardnum)
        print('您的身份证号为：%s' % self.alluser[num].id)
        print('您的余额为：%d' % self.alluser[num].money)
        print('1.账户   2.密码   3.身份证号')
        cnt=input('请选择您所要修改的信息：')
        if cnt=='1':
            self.ModifyName(num)
        elif cnt=='2':
            self.ModifyPwd(num)
        elif cnt=='3':
            self.ModifyId(num)

    def Delet(self):#清除账号
        num=self.Login()
        flag=False
        for i in range(1,4):
            cardnum=input('请输入您所要销毁的卡号：')
            if self.alluser[num].cardnum==cardnum:
                flag=True
                break
            print('卡号输入不正确，请重新输入')
        if flag==False:
            print("三次卡号输入不正确，请重新登录")
            return
        flag=True
        for i in range(1,4):
            pwd=input('请输入密码：')
            if pwd==self.alluser[num].pwd:
                flag=True
                break
            print("密码输入不正确，请重新输入")
        if flag==False:
            print("三次密码输入不正确，请重新登录")
            return
        print('您的账户为：%s' % self.alluser[num].name)
        print('您的卡号为：%s' % self.alluser[num].cardnum)
        print('您的身份证号为：%s' % self.alluser[num].id)
        print('您的余额为：%d' % self.alluser[num].money)
        print("请确认是否销毁账户：")
        print('1.确认销毁   2.返回')
        tmp=input()
        if tmp=='1':
            del self.alluser[num]
            print('销毁成功')
        else:
            return

    def register(self):#主页面
        print("****************************************")
        print("******This is a simple Bank System******")
        print("                        --by Azura******")
        print("****************************************")
        print("请输入您所需要的服务：")
        print("****************************************")
        print("1.注册新的账户            2.查询账户信息")
        print("3.存款                    4.取款")
        print("5.修改账户信息            6.删除账号   ")
        print("                7.退出                ")
        print("****************************************")
        while 1:
            tmp=input()
            if tmp=='1':
                self.SignUp()
            elif tmp=='2':
                self.Info()
            elif tmp=='3':
                self.Add()
            elif tmp=='4':
                self.Minus()
            elif tmp=='5':
                self.Modify()
            elif tmp=='6':
                self.Delet()
            elif tmp=='7':
                return
            else:
                print("请重新输入你所需要选择的服务...")

def pickle_load(filename):#如果文件为空返回字典
    dic={}
    with open(filename,'rb') as input_file:
        try:
            a=pickle.load(input_file)
            input_file.close()
            return a
        except EOFError:
            return dic

alluser=pickle_load('UserInfo.txt')
User=Bank(alluser)
User.register()
print("欢迎下次使用！")
fw=open('UserInfo.txt','wb')
pickle.dump(alluser,fw)
fw.close()