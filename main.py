#s = input()
#print(s[2])
#print(s[-2])
#print(s[:5])
#print(s[:-2])
#print(s[::2])
#print(s[1::2])
#print(s[::-1])
#print(s[::-2])
#print(len(s))

#print(input().count(' ') + 1)

#a = input()
#print(a[(len(a) + 1) // 2:] + a[:(len(a) + 1) // 2])

#s = input()
#if s.count('f') == 1:
    #print(s.find('f'))
#elif s.count('f') >= 2:
    #print(s.find('f'), s.rfind('f'))

#s = 'ahau hau'
#s = s[:s.find('h')] + s[s.rfind('h') + 1:]
#print(s)

#c = "1 был 2 не был 1 был"
#c = c.replace('1', 'one')
#print(c)

#g = "@mail или @gmail"
#g = g.replace('@',"")
#print(g)


#s = "hay hello hanter oih hia"
#a = s[:s.find('h') + 1]
#b = s[s.find('h') + 1:s.rfind('h')]
#c = s[s.rfind('h'):]
#s = a + b.replace('h', 'H') + c
#print(s)


#a = 16
#b = 15
#if a > b:
#    print(b)
#else:
#    print(a)

#x = 0
#if x > 0:
#    print("x = 1")
#elif x < 0:
#    print("x = -1")
#elif x == 0:
#    print("x = 0")

#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if (x1 + y1 + x2 + y2) % 2 == 0:
#    print('YES')
#else:
#    print('NO')

#year = 2020
#if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#    print('YES')
#else:
#    print('NO')

#a = 1
#b = 3
#c = 2
#if a == b == c:
#    print("3")
#elif a == b or a == c or b == c:
#    print("2")
#else:
#    print("0")

#x1 = int(input())
#y1 = int(input())
#x2 = int(input())
#y2 = int(input())
#if x1 == x2 or y1 == y2:
#    print('YES')
#else:
#    print('NO')

#n = int(input())
#m = int(input())
#k = int(input())
#if k < n * m and ((k % n == 0) or (k % m == 0)):
#    print('YES')
#else:
#    print('NO')

#n = int(input())
#m = int(input())
#x = int(input())
#y = int(input())
# n, m = min(n, m), max(n, m)
#if n > m:
#    n, m = m, n
#if x >= n / 2:
#    x = n - x
#if y >= m / 2:
#    y = m - y
# print(min(x, y))
#if x < y:
#    print(x)
#else:
#    print(y)