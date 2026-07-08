from typing import Union, Optional


def calculate_total_delivery_cost(
        product_name: str,
        weights: Union[list, tuple],
        prices: Union[list, tuple],
        discount: Optional[float],
        currency_rate: Union[float, int],
        *extra_costs: float,
) -> dict[str, float]:
    """
    :param product_name:
    :param weights:
    :param prices:
    :param discount:
    :param currency_rate:
    :param extra_costs:
    :return:
    """

    total_sum: list = []
    if len(weights) == len(prices):
        for i in range(len(weights)):
            total_sum.append(weights[i] * prices[i])
            if discount is not None:
                total_sum[i] *= (1 - discount)
    for i in extra_costs:
        total_sum.append(i)

    final_sum = sum(total_sum) * currency_rate
    print(f'Товар: {product_name}, итоговая стоимость: {final_sum}')

calculate_total_delivery_cost(
    'Овощная партия',
    [100, 50],
    [4, 6],
    0.1,
    1,
    20, 15
)

calculate_total_delivery_cost(
    'Фруктовая партия',
    (30, 20, 10),
    (15, 12, 18),
    None,
    1.2,
    25
)
