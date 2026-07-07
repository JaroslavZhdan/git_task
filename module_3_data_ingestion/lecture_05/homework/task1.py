raw_log = "ORDER-2025-01-15|FRT-APPLE-PL|+111 (23) 456-78-90| мИНсК "
order_id, product_code, raw_phone, raw_city = raw_log.split("|")
category = product_code[:3]
region = product_code[-2:]

print(f'Позиция первого дефиса в коде товара: {product_code.find('-')}')
if product_code.startswith('FRT'):
    print("Код товара начинается с 'FRT'")
else:
    print("Код товара не начинается с 'FRT'")

clean_phone = ''
for i in raw_phone:
    if i.isdigit():
        clean_phone += i
print(f'Длина номера телефона: {len(clean_phone)}')

clean_city = raw_city.strip().lower().title()
print(f'Город: {clean_city}')
print(f'Заказ: {order_id}\nКатегория: {category} | Регион: {region}\nТелефон: {clean_phone}\nГород: {clean_city}')