a = int(input("Введите результат пробежки первого дня в км "))
b = int(input("Введите общий достигаемый результат в км "))
days = b
km = a
while km < b:
    a = a + 0.1 * a
    days += b
    km = days + a
print(f"Вы достигнете результата на %.d день" % days)

