
with open ('6_2.txt') as r:
    n = int((r.readline()).translate(None, '\n'))
    m = int((r.readline()).translate(None, '\n'))
    down, right = [], []
    for line in r:
        line = line.translate(None, '\n')
        if line == '-':
            break
        line = line.split()
        temp = [int(item) for item in line]
        down.append(temp)
    for line in r:
        line = line.translate(None, '\n')
        line = line.split()
        temp = [int(item) for item in line]
        right.append(temp)

def memoize(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function

@memoize

def Tourist(n, m):
    s = [[0]*(m + 1) for i in range(n + 1)]
    #print s
    for i in range(1, n + 1):
        s[i][0] = s[i-1][0] + down[i-1][0]

    for j in range(1, m + 1):
        s[0][j] = s[0][j-1] + right[0][j-1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            #print down[i-1][j], right[i][j-1]
            s[i][j] =max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
    return s[n][m]
          
#print n, m, down, right
print Tourist(n, m)