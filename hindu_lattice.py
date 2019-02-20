def multi(x,y):
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
