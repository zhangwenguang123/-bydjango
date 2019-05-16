from func.view import View
from func.operation import Operation
if __name__ == "__main__":
    opera = Operation()
    while View.view():
        choise = int(input())
        #注册
        if choise == 1:
            opera.register()
        #查询
        elif choise == 2:
            opera.query()
        #存钱
        elif choise == 3:
            opera.save_money()
        #取钱
        elif choise == 4:
            opera.get_money()
        #转账
        elif choise == 5:
            opera.trans_money()
        #改密
        elif choise == 6:
            opera.change_pwd()
        #锁卡
        elif choise == 7:
            opera.lock()
        #解卡
        elif choise == 8:
            opera.unlock()
        #补卡
        elif choise == 9:
            opera.register()
        #退出
        elif choise == 0:
            opera.save()
            break
        