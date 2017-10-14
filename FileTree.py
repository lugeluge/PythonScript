__author__ = "陆驰"
import os
def P(path,depth1,depth2):
    print('|',end="")
    print(" "*depth1,end="")
    if depth1!=0:
        print('|',end="")
    print('-'*depth2,end="")
    print(path)
    path = os.path.abspath(path) #返回path规范化的绝对路径。 C:\Users\Administrator\Pictures
    if(not os.path.isdir(path)):
        return
    try:
        os.chdir(path) #方法用于改变当前工作目录到指定的路径

    except:
        return
    for x in os.listdir(path):
        P(x,depth1+depth2,5)
    os.chdir("..")

if __name__ == '__main__':
    #path=input("enter path")
    path='C:/Users/Administrator/Pictures'
    P(path,0,0)