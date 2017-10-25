'''
普通的递归调用可能会导致栈溢出，函数调用
是通过栈的方式来实现的
尾递归调用就没有这个问题了
'''

#普通递归调用
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
#尾递归调用

def optimizeFact(n):
    return
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
if __name__ == '__main__':
    print(fact(5))
    print(fact_iter(5,1))