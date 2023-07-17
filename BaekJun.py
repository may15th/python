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

test_result = int(input())

if test_result >= 90:
    print('A')
elif test_result >=80:
    print('B')
elif test_result >=70:
    print('C')
elif test_result >=60:
    print('D')
else:
    print('F')