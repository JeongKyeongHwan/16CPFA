#-*-coding:cp949
people = 30
cars = 40
trucks = 15


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."
# if 구문이 거짓일 경우 elif 구문 판별 거짓일 경우 else구문 출력
if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."
# if 구문이 거짓일 경우 elif 구문 판별 거짓일 경우 else구문 출력
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
# if 구문이 거짓일 경우 else 구문 출력