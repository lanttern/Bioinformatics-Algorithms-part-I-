
with open ('6_1test1.txt') as r:
    money = int((r.readline()).translate(None, '\n'))
    c = (r.readline()).translate(None, '\n')
    c = c.replace(',', ' ')
    c = c.split()
    coins = [int(coin) for coin in c]

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

def DPChange(money):
    MinNum = [0]*(money + 1)
    #print MinNum
    for m in range(1, money + 1):
        MinNum[m] = money
        for i in range (0, len(coins)):
            if m >= coins[i]:
                if MinNum[m-coins[i]] + 1 < MinNum[m]:
                    MinNum[m] = MinNum[m-coins[i]] + 1
                    print coins[i]
                    
    return MinNum[money], MinNum
        
print money, coins
print DPChange(money)