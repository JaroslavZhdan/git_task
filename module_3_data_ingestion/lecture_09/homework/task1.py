def calculate_purchase(product_name, weight, price):
    """
    :param product_name:
    :param weight:
    :param price:
    :return:
    """

    try:
        numeric_weight = float(weight)
        total_cost = numeric_weight * price
        technical_index = 100 / numeric_weight
        print(f'Товар: {product_name}. Итоговая стоимость: {total_cost}$')
    except TypeError as e:
        print(type(e), e)
    except ValueError as e:
        print(type(e), e)
    except ZeroDivisionError as e:
        print(type(e), e)
    finally:
        print("--- Проверка партии завершена ---")

calculate_purchase('Томаты', 100, 2.5)
calculate_purchase('Огурцы', 'Пятьдесят', 1.8)
calculate_purchase('Перец', 0, 4)
calculate_purchase('Зелень', [10], 5)
