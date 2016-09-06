#-*-coding:cp949
from sys import argv
# 시스템으로 부터 매개변수 출력
script, filename = argv
# 매개변수 2개
txt = open(filename)
# txt를 치면 파일이름 경로 실행
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

