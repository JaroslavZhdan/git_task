rows_range = range(1, 6)
rows = list(rows_range)

rows.pop(2)
rows.insert(2, 'Ремонт')

if 5 in rows:
    print('Ряд 5 доступен')

priority_rows = rows[:3]

print(rows)
print(priority_rows)
