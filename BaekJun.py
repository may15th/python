# a,b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)


# nick_name = input(str())
# print(nick_name+"??!")

# 18108

# year_budda = int(input())
# year_crist = year_budda - 543
# print(year_crist)

# 10430

# a,b,c = map(int, input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

# 2588

# a = int(input())
# b = int(input())
# print(b%10*a)
# print((b%100-b%10)//10*a)
# print((b-b%100)//100*a)
# print(a*b)

# a,b = map(int, input().split('\n'))
# print(b%10*a)
# print((b%100-b%10)//10*a)
# print((b-b%100)//100*a)
# print(a*b)
# 이 방법은 왜 안돼??

# A,B,C = map(int, input().split())
# print(A+B+C)

#1330

# A, B =map(int,input().split())

# if A>B:
#     print(">")
# elif A<B:
#     print("<")
# elif A==B:
#     print("==")

# 9498

# test_result = int(input())

# if test_result >= 90:
#     print('A')
# elif test_result >=80:
#     print('B')
# elif test_result >=70:
#     print('C')
# elif test_result >=60:
#     print('D')
# else:
#     print('F')

# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print(1)
# elif x<0 and y>0:
#     print(2)
# elif x<0 and y <0:
#     print(3)
# else:
#     print(4)

# W,M = map(int,input().split())


# if W < 1 and M < 45:
#     print(23, 15+M)
# elif M<45:
#     print(W-1,M+15)
# else:
#     print(W, M-45)


# 못 품. 오븐시계 문제
# A,B = map(int, input().split())
# C = int(input())

# if B+C >= 60:
#     A=A+(B+C)//60
#     B=(B+C)%60
#     if A>= 24:
#         A= A-24
#         print(A,B)
#     else:
#         print(A,B)
# else:
#     print(A,B+C)

# 주사위 시계

# x,y,z = map(int, input().split())
# if x==y==z:
#     print(10000+1000*x)
# elif x==y:
#     print(1000+x*100)
# elif y ==z:
#     print(1000+100*y)
# elif z==x:
#     print(1000+z*100)
# else:
#     if x>=y and x>=z:
#         print(x*100)
#     elif y>=x and y>=z:
#         print(y*100)
#     else:
#         print(z*100)

# N = int(input())

# for i in range(1,10):
#     print(N,"*",i,"=",N*i)

# m=0
# n = int(input())
# while m<n: 
#     m=m+1
#     A,B = map(int, input().split())
#     print(A+B)


# n = int(input())
# for i in range(n):
#     A,B = map(int, input().split())
#     print(A+B)

#합
# n = int(input())
# sum = 0
# for i in range(n+1):
#     sum = sum+i
#     i = i+1
# print(sum)

X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a,b = map(int, input().split())
    c=a*b
    sum += c
if sum == X:
    print("Yes")
else:
    print("No")

