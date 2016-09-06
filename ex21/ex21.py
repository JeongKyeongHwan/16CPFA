#-*-coding:cp949
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
# 덧셈함수
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
# 뺄셈함수
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
# 곱셈함수
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
# 나눗셈 함수

print "Let's do some math with just functions!"
# 문자열 출력
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# 지정된 변수에 의한 함수값을 문자열로 지정
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# 위에서 지정된 문자열을 각기 자리에 집어넣는다.

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 제일 안쪽 괄호부터 풀이한다.
print "That becomes: ", what, "Can you do it by hand?"