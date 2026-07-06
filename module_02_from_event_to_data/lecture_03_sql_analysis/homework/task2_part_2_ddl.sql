-- 1. Создать новую таблицу с именем Data_Layers необходимую для описания слоев со столбцами: LayerID (SERIAL, PRIMARY KEY), LayerName (VARCHAR(50), UNIQUE, NOT NULL), Description (TEXT).
CREATE TABLE Data_Layers (
	LayerID SERIAL PRIMARY KEY,
	LayerName VARCHAR(50) UNIQUE NOT NULL,
	Description TEXT
	);

-- 2. Заполнить колонку LayerName тремя значениями 'Bronze', 'Silver', 'Gold', которые обозначают слои в медальонной архитектуре.
INSERT INTO
    Data_Layers (LayerName)
VALUES
	('Bronze'),
	('Silver'),
	('Gold');

-- 3. Добавить колонку manager_email в таблицу Data_Layers (VARCHAR(100)).
ALTER TABLE
    Data_Layers
ADD COLUMN
    manager_email VARCHAR(100);

-- 4. Добавить ограничение UNIQUE к столбцу manager_email в таблице Data_Layers (предварительно заполнив столбец любыми значениями, чтобы избежать ошибки).
ALTER TABLE
    Data_Layers
ADD UNIQUE(manager_email);

-- 5. Переименовать столбец address в таблице Shops в shop_address.
ALTER TABLE
	shops
RENAME address TO shop_address;