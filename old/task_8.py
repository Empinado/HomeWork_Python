# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите значение стороны n: "))

m = int(input("Введите значение стороны m: "))

k = int(input("Введите количество долек, которые хотите надломить: "))

if k % n == 0 or k % m ==0 and k<n*m:
    print("Yes")
else:
    print("No")