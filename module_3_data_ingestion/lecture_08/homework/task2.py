branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000}
]

def audit_logger(func):
    def wrapper(*args, **kwargs):
        print('[AUDIT] Запуск анализа...')
        result = func(*args, **kwargs)
        print('[AUDIT] Анализ завершен.')
        return result
    return wrapper

@audit_logger
def get_sorted_report(data_filials):
    return sorted(data_filials, key=lambda x: x['revenue'], reverse=True)

result = get_sorted_report(branches)
print('Топ филиалов:')
for index, item in enumerate(result, start=1):
    print(f'{index}. {item["city"]} ({item["revenue"]})')