#-*-coding:cp949
i = 0
numbers = []
# i�� numbers�� �� ����
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
# i�� 6���� ������ ���� �ؿ� ���� ����
    i = i + 1
# I�� �缳�� �� �����δ� �缳�� ������ i���
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
# []�� ����Ʈ numbers�� ����Ʈ�� ���� ���

print "The numbers: "
for num in numbers:
    print num

else:
    print "end"

