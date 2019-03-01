import time
start = time.time()

def ori_mul(x,y):
    return x*y
    
def hindu_lattice(x,y):
    x = str(x)
    y = str(y)
    mul = 0
    z = ''
    for k in range(len(x)+len(y)-1):
        for i in range(len(x)):
            for j in range(len(y)):
                if i+j == k:
                    mul += int(x[::-1][i])*int(y[::-1][j])
        z += str(mul%10)
        mul = mul // 10
    z += str(mul%10)
    return int(z[::-1])

def peasant_multi(x,y):
    ans = 0
    while x > 0:
        if x % 2 == 1:
            ans += y
        x = int(x/2)
        y += y
    return ans
     
if __name__ == '__main__':
    print(hindu_lattice(99999999,9999999))
    print(peasant_multi(99999999,9999999))
    print(time.time()-start)
    
