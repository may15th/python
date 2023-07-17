print("i eat %s" % 'apple')
print("i eat %d apples" % 3)
a= 'pithon'
print(a[0] + 'y' + a[2:])
print(a[:1] + 'y' + a[2:])
print("%10s" % "hi")
print("%-10sjane." % 'hi')
print("%0.4f" % 3.412345)
print("i eat {0} apples" .format(3))
print("i eat {0} apples." .format('five'))
number = 10
day = 'three'
print("i ate {0} apples. so i was sick for {1} days." .format(number, day))
print("i ate {number} apples. so i was sick for {day} days" .format(number=10, day='three'))
print("i ate {0} apples. so i was sick for {day} days." .format(10, day=3))
print("{0:>10}" .format("hi"))
print("{0:<10}" .format("hi"))
print("{0:^10}" .format("hi"))
print("{0:=^10}" .format("hi"))
print("{0:!<10}" .format("hi"))
y=3.42131452
print("{0:0.4f}" .format(y))
print("{0:10.4f}" .format(y))
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
age = 30
print(f'나이는 내년에 {age+1}이 됩니다.')
d = {'name' : '홍길동', 'age' : 30}
print(f'나의 이름은 {d["name"]}입니다. 나이는{d["age"]}입니다.')
print(f'{"h1":<10}')
print(f'{"hi":>10}')
print(f'{"hi":-^10}')
print(f'{"hi":!<10}')
y = 3.4121223
print(f'{y:0.4f}')
print(f'{y:10.4f}')
print(f'{{y}}')
a='hobby'
print(a.count('b'))
a = "Python is the best choice"
a.find('b')
a.find('k')

a = "Life is too short"
print(a.index('t'))

print(",".join('abcd'))
a = "hi"
print(a.upper())

a="HI"
print(a.lower())

a="    hi    "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
a = "life is too short"
print(a.replace("life", "your leg"))

a= "life is too short"
b = a.split()
print(b)
b= "a,b,c,d"
print(b.split(','))
odd = [1,3,5,7,9]

a = [1,2,3]
print(a)
print(a[0])

a = [1,2,['a','b',['life','is']]]
print(a[2][2][0])
print(a[-1][-1][-2])

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

# 2-3 리스트 자료형

# 2-5 딕셔너리 자료형
a = {'김연아':'피겨스케이팅', '박찬호':'야구', '고유한':'코딩'}
b=a['고유한']
print(b)

grade = {'pey': 10, 'juliet': 90}
print(grade['pey'])
print(grade['juliet'])

dic = {'name':'pey', 'phone': '010-9999-1234', 'birth': '118'}
b= dic['name']
c= dic['phone']
d= dic['birth']
print(b,c,d)

a ={'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
b = list(a.keys())
print(b)

s1 = set([1,2,3])
li = list(s1)
print(li)

t1 = list(s1)
print(t1, t1[0])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1&s2)
print(s1.intersection(s2))

print(s1|s2)

print(s1-s2)
print(s1.difference(s2))

s1 = set([1,2,3])
s1.add(4)
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

s1.remove(2)
print(s1)

print(s1.remove(3))
# 왜 안되지?

# 3. 프로그램 구조를 쌓아보자! 제어문


# a = [1,2,3,4]
# while a:
#     print(a.pop())

# if [1,2,3]:
#     print("참")
# else:
#     print("거짓")

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print("택치를 타고 가라")
# else:
#     print("걸어가라")

# if 'money' in pocket:
#     pass
# else:
#     print("카드를 꺼내라")

# if 'money' in pocket: print(("코딩왕"))
# else: print("카드를 꺼내라")

# pocket = 'paper', 'cellphone', 'money'
# if 'money' in pocket: print("찐천재")
# else: print("바보")

# treeHit= 0
# while treeHit < 10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다." % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")
# prompt = """
#     1. Add
#     2. Del
#     3. List
#     4. Quit

#     Enter number: """
# # number = 0
# # while number != 4:
# #     print(prompt)
# #     number = int(input())

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee -1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break

# happy = int(input("얼마나 행복하신가요? 0~10: "))
# notice = "그만 두고 싶으시면 11입력 하세요"

# if happy > 10:
#     print("10 이하의 값을 입력해 주세요")
# elif 7 <= happy <=10:
#     print("당신이 행복하니 저도 행복해요.")
# elif 4 <= happy <7:
#     print("힘내세요")
# elif 0 <= happy <4:
#     print('ㅠㅠ같이 울어줄게요.')

# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money-300))
#         coffee = coffee -1
#     else:
#         print("돈을 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break


# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee - 1
#     print("남은 커피의 양은 %d개입니다" %coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판맬르 중지합니다.")
#         break


#coffee.py
# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다. ")
#         coffee = coffee - 1
#     # 아래 구문 money-300이 정수형으로 안불려오는 이유 확인.
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %개 입니다." %coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break

a = 0
while a < 10:
    a = a+1
    if a % 2 ==0:
        continue
    print(a)
        
# while True:
#     print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")
#     try:
#         input()
#     except KeyboardInterrupt:
#         break
    
#전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first+last)


marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)

marks = [90,25,67,45,80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

a= range(10)

#range 함수의 예시

add = 0
add2 = 0
for i in range(1,11):
    add = add +i
for i in range(11):
    add2 = add2 + i
print(add)
print(add2)

marks = [90,25,67,45,80]
for number in range(len(marks)):
    if marks