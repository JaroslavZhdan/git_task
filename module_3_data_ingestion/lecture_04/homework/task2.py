# Список списков
daily_logs = [
    [500, 0, 1200],       # Касса 1 (Нормальная)
    [300, -999, 800],     # Касса 2 (Сломалась посередине, 800 не должно посчитаться)
    [1500, 200]           # Касса 3 (Нормальная)
]

total_revenue = 0

for index, cash_register in enumerate(daily_logs, start=1):
    print(f'--- Обработка Кассы №{index} ---')
    for j in cash_register:
        if j == -999:
            print('Аварийная остановка кассы!')
            break
        elif j ==0:
            print("Пропуск сбоя")
            continue
        else:
            total_revenue += j
            print(f'Добавлено: {j}')

print('=== ИТОГ ДНЯ ===')
print(f'Итог дня: {total_revenue}')
