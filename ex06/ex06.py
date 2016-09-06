x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# x, y 값 지정
print x
print y
# x, y 를 출력
print "I said: %r." % x
print "I also said: '%s'." % y
# 특정 지정에 x, y로 지정된 문자열 삽입
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# 특정 문자에 문자열 지정
print joke_evaluation % hilarious
# 지정된 값으로 문자열 안에 문자 삽입
w = "This is the left side of..."
e = "a string with a right side."
# w, e 를 일정한 문자열로 지정
print w + e
# 두가지 더한 것의 출력