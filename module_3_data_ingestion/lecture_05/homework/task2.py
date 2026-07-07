product = " фермерский ТВОРОГ "
price = 4.567
qty = 3
csv_row = "milk,bread,cheese"
review = "Это лучший ТВОРОГ в городе!"
# Используем r для того, чтобы не пришлось экранировать символы
file_path = r"C:\EcoMarket\data\2025\january\sales.csv"

clean_product = product.strip().lower().title()
print(clean_product)
total = price * qty
print(f'Чек "EcoMarket"Товар:\t{clean_product}\nКол-во:\t{qty}\nИтого:\t {total} руб.')

print(' | '.join(csv_row.split(",")))

if 'творог' in review.lower():
    print('Отзыв относится к категории: Dairy')
print(file_path)