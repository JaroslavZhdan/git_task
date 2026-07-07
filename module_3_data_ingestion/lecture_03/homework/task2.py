product_name = "Морковь мытая"
price = 2.5
stock_quantity = 150
is_local_farm = True
supplier = None

has_coupon = True
has_card = False
total = 10

if price < 3 and is_local_farm == True:
    is_hit = True
else:
    is_hit = False
print(f'Является ли товар хитом? {is_hit}')

if supplier is not None:
    has_supplier = True
else:
    has_supplier = False

print(f'{has_supplier=}')

if supplier is not None and stock_quantity > 1:
    can_show_in_app = True
else:
    can_show_in_app = False
print(f'{can_show_in_app=}')

if stock_quantity <= 20 or is_hit == True:
    needs_restock = True
else:
    needs_restock = False
print(f'{needs_restock=}')

if not(is_local_farm):
    is_blocked = True
else:
    is_blocked = False
print(f'{is_blocked=}')

discount_without_brackets = has_coupon or has_card and total > 50
print(f'{discount_without_brackets=}')
discount_with_brackets = (has_coupon or has_card) and total > 50
print(f'{discount_with_brackets=}')

price += 1.0
stock_quantity *= 2
boxes = stock_quantity
boxes //= 10
if price < 3 and is_local_farm == True:
    is_hit = True
else:
    is_hit = False
print(f'Является ли товар хитом? {is_hit}')
if stock_quantity <= 20 or is_hit == True:
    needs_restock = True
else:
    needs_restock = False
print(f'{needs_restock=}')

