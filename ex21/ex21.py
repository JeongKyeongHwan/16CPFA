#-*-coding:cp949
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
# �����Լ�
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
# �����Լ�
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
# �����Լ�
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
# ������ �Լ�

print "Let's do some math with just functions!"
# ���ڿ� ���
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# ������ ������ ���� �Լ����� ���ڿ��� ����
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# ������ ������ ���ڿ��� ���� �ڸ��� ����ִ´�.

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# ���� ���� ��ȣ���� Ǯ���Ѵ�.
print "That becomes: ", what, "Can you do it by hand?"