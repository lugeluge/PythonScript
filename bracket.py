#coding:utf-8
#python2
"""
括号匹配算法。
"""
SYMBOLS = {'}':'{', ']':'[', ')':'('}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.values(), SYMBOLS.keys()

def check(s):
    arr = []
    for c in s:
        if c in SYMBOLS_L:
            # 左符号入栈
            arr.append(c)
        elif c in SYMBOLS_R:
            # 右符号要么出栈，要么匹配失败
            if arr and arr[-1] == SYMBOLS[c]:
                arr.pop()
            else:
                return False

    return not arr
def check1(s,idx):
    arr=[]
    if abs(idx)>len(s):
        return None
    if (s[idx] not in SYMBOLS_L) and (s[idx] not in SYMBOLS_R):
        return None
    for index,item in enumerate(s):
        if item in SYMBOLS_L:
            arr.append((index,item))
        if item in SYMBOLS_R:
            if arr and arr[-1][1]==SYMBOLS[item]:
                temp=arr.pop()
                if idx==temp[0]:
                    return index
                if idx==index:
                    return temp[0]
    return None
def check3(s, idx):
    """这里以{、}为例，注意也要适用于'[]', '()'
    >>> 括号匹配位置('{123}', 0)
    4
    >>> 括号匹配位置('0{23{5}}89', 1)
    7
    >>> 括号匹配位置('0{23{5}}89', 7)
    1
    >>> 括号匹配位置('0{23{5}78', 1)
    None
    >>> 括号匹配位置('0{23{5}78', 20)
    None
    >>> 括号匹配位置('0[2[4]{7}]01', 9)
    1
    >>> 括号匹配位置('0{[34{6}89}', -4)
    5
    """
    key = '{[()]}'
    try:
        if idx < 0:
            idx += len(s)
        ch1 = s[idx]
        print 'ch1',ch1
        idx1 = key.index(ch1)
        print 'idx1',idx1
    except:
        return None
    idx2 = len(key) - idx1 - 1
    print 'idx2',idx2
    ch2 = key[idx2]
    print 'ch2',ch2
    step = 1 if idx2 > idx else -1
    cnt = 1; i = idx + step
    if i < 0:
        i += len(s)
    while i >= 0 and i < len(s):
        if s[i] == ch1:
            cnt += 1
        elif s[i] == ch2:
            cnt -= 1
        if cnt == 0:
            return i
        i += step
    return None
# print(check("3 * {3 +[(2 -3) * (4+5)]}"))
# print(check("3 * {3+ [4 - 6}]"))
print check3('0{34{6}89}', 1)
arr=[1]