raw_sku = "CARROT-001"
raw_regions = ("Minsk", "Warsaw", "Berlin", "Warsaw")
raw_weight_str = "2.5"
raw_stock_str = "150"

weight_kg = float(raw_weight_str)
stock_quantity = int(raw_stock_str)

sku_as_list = list(raw_sku)
regions_list = list(raw_regions)
unique_regions = set(raw_regions)
regions_tuple = tuple(unique_regions)

empty_list_1 = []
empty_list_2 = list()
empty_dict_1 = {}
empty_dict_2 = dict()
empty_tuple_1 = ()
empty_tuple_2 = tuple()
empty_set = set()

print(bool(empty_list_1), bool(empty_dict_1), bool(empty_tuple_1), bool(empty_set))
list1 = [1, 2, 3]
list2 = [4, 5, 6]
dict_1 = {1: 1, 2: 2, 3: 3}
dict_2 = {1: 4, 2: 5, 3: 6}
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
set_1 = {1, 2, 3}
print(bool(list1), bool(dict_1), bool(dict_2), bool(tuple_1), bool(tuple_2), bool(set_1))

print(weight_kg, type(weight_kg))
print(stock_quantity, type(stock_quantity))
print(sku_as_list, type(sku_as_list))
print(regions_list, type(regions_list))
print(unique_regions, type(unique_regions))
print(regions_tuple, type(regions_tuple))