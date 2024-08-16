# 
class MyException(Exception):
    pass

def devide(a, b):
    if b == 0 :
        raise MyException('0では割り切れません')
    else:
        return a/b
    
try:
    c = devide(1,0)
except Exception as e:
    print(e, type(e))
    
    
a = 10 / 10