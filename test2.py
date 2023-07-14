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
