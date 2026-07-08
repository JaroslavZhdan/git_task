SMALL_BATCH_LIMIT = 500

def calculate_batch(weight, price, discount = 0.0):
    """
    :param weight:
    :param price:
    :param discount:
    :return: final_sum
    """
    final_sum = weight * price * (1 - discount)
    is_limit_exceeded = final_sum >= SMALL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

carrot = calculate_batch(100, 4)
apples = calculate_batch(50, 20, 0.10)
print(f'Партия 1 (Морковь): {carrot[0]}. Превышение лимита: {carrot[1]}')
print(f'Партия 2 (Яблоки): {apples[0]}. Превышение лимита: {apples[1]}')
