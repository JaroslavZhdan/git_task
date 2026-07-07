"""
Модуль для быстрого расчета геометрических параметров новых квадратных зон хранения
Автор: Jaroslav Zhdan
Версия: 1.0.0
"""

import math

identification_zone = input('Введите идентификатор зоны: ')
area_total = 225
side_length = math.sqrt(area_total)
print(f'Расчет для объекта {identification_zone}')
print(f'Длина стены зоны: {side_length}')
