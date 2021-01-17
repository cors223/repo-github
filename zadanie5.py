profit = float(input(f"Введите выручку фирмы: "))
costs = float(input(f"Введите издержки фирмы: "))
if profit > costs:
print(f"Фирма работает с прибылью. Рентабельность выручки составила: {profit / costs:.2f}")
workers = int(input("Введите количество сотрудников фирмы: "))
print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == costs:
print(f"Фирма работает в ноль")
else:
print(f"Фирма работает в убыток")
