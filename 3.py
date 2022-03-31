a=True
num=[0]
for i in range(5):
    number=int(input('введите число '))
    if number<=num[-1]: a=False
    num.append(number)
print (('Нет','Да')[a])
