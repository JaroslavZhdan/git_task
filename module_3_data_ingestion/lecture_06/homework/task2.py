prices = [100, -50, 300, 40, 800]

prices.remove(-50)

prices.append(150)

prices.sort()

tax_prices = [i * 1.2 for i in prices if i * 1.2 > 100]

print(f'Базовый прайс (очищенный): [40, 100, 150, 300, 800]')
print(f'Цены с НДС (>100): {tax_prices}')
print(f'Общая выручка: {sum(tax_prices)}')
print(f'Минимум: {min(tax_prices)}')
print(f'Максимум: {max(tax_prices)}')
