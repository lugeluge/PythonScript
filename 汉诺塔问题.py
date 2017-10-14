'''经典递归问题，汉诺塔问题
'''
global i
i=0
def move(n, a, b, c):
    if n==1:
        print('%s->%s'%(a,c))
        global i
        i=i+1
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
if __name__ == '__main__':
    move(3,'A','B','C')
    print('移动的次数为',i,'次')