products = ["Яблоки", "Хлеб", "Молоко", "Печенье", "Сок", "Кефир"]
for i in range(0, len(products), 2):
    print(f'Индекс {i} Проверен товар {products[i]} (Длина названия {len(products[i])} символов)')
    if 'Бананы' in products:
        break
else:
    print('--- Выборочная проверка успешно завершена ---')