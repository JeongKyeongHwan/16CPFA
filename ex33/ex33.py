#-*-coding:cp949
i = 0
numbers = []
# i와 numbers의 값 설정
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
# i가 6보다 작을때 까지 밑에 구문 실행
    i = i + 1
# I갑 재설정 이 밑으로는 재설정 값으로 i출력
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
# []는 리스트 numbers에 리스트된 값들 출력

print "The numbers: "
for num in numbers:
    print num

else:
    print "end"

