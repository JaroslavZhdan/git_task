-- 1. Вставить два новых Продукта (Products).
INSERT INTO products (product_id, product_name, price, category_id, class, resistant, is_allergic, vitality_days, modify_timestamp)
VALUES (506, 'Bananas Family Pack', 30, 1, 'C', false, false, 123, now());

INSERT INTO products (product_id, product_name, price, category_id, class, resistant, is_allergic, vitality_days, modify_timestamp)
VALUES (507, 'Pear Family Pack', 35, 1, 'B', false, true, 101, now());

-- 2. Выбрать только Продукты (Products) у которых is_allergic и resistant = 'Yes'.
SELECT
	*
FROM
	products
WHERE
	is_allergic=true and resistant=true;

-- 3. Обновить is_allergic для Продукта (Products) Bananas Family Pack на 'Yes'.
UPDATE
	products
SET
	is_allergic = true
WHERE
	product_name = 'Bananas Family Pack';

-- 4. Удалить один из двух добавленных продуктов.
DELETE
FROM
	products
WHERE
	product_id = 506;

-- 5. Проверить все изменения, используя SELECT * FROM Products;.
SELECT
	*
FROM
	products;