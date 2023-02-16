-- 예제1
SELECT productCode,productName,MSRP
FROM products
WHERE MSRP > 
	(
	SELECT AVG(MSRP)
	FROM products
    )
ORDER BY
	MSRP;
    
-- 예제2
SELECT
	customerNumber,customerName
FROM
	customers
WHERE 
	customerNumber IN 
    (
    SELECT customerNumber FROM orders
    WHERE orderDate BETWEEN 20030106 AND 20030326
    )
ORDER BY
	customerNumber;
    
-- 예제3

SELECT productCode,productName,productLine,MSRP
FROM (
	SELECT *
	FROM products
    WHERE productLine = 'Classic Cars'
    ) AS classicCars_query
WHERE MSRP = (
	SELECT MAX(MSRP) FROM products
    );
    
-- 예제4
SELECT
	customerNumber,customerName,country
FROM
	customers
WHERE country = 
	(
    SELECT MAX(country)
	FROM customers
    )
ORDER BY
	customerNumber;
    
-- 예제5
SELECT * 
FROM customers;

SELECT
	customerNumber
FROM (
	SELECT *
	FROM customers
    INNER JOIN orders USING(customerNumber)
    ) AS sub_order

-- 예제6
