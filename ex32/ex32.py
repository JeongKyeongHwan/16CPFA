#-*-coding:cp949

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# 항목별로 변수값 설정

for number in the_count:
    print "This is count %d" % number
# the_count 값을 number로 설정

for fruit in fruits:
    print "A fruit of type: %s" % fruit
# frutis값을 fruit로 설정

for i in change:
    print "I got %r" % i
# change값을 변수 i에 대입

elements = []
# []안의 값을 elements의 변수로 설정

for i in range(0, 6):
    print "Adding %d to the list." % i
# range(0, 6) = [0, 1, 2, 3, 4, 5]를 i로 설정
    elements.append(i)
# elements의 리스트 마지막에 append(i)값을 추가

for i in elements:
    print "Element was: %d" % i

# elements의 값을 i에 대입
