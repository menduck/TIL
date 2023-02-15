-- 문제 1
SELECT
	employeeNumber,lastName,firstName,city
FROM
	employees
INNER JOIN offices
	ON	employees.officeCode = offices.officeCode;
    
-- 문제 2
SELECT
	customerNumber,officeCode,customers.city,offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 3
SELECT
	customerNumber,officeCode,customers.city,offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;
    
-- 문제 4
SELECT
	customerNumber,officeCode,customers.city,offices.city
FROM
	customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제 5
-- 문제2는 LEFT JOIN으로 왼쪽 테이블인 customers 모든 필드와 오른쪽과 왼쪽 테이블의 겹치는 부분만 조회 한다.
-- 문제3은 RIGHT JOIN으로 외른쪽 테이블인 offices의 모든 레코드와 왼쪽 테이블의 일치하는 레코드를 반환한다.
-- 문제4는 INNER JOIN으로 두 테이블이 겹치는 레코드만 조회한다.

-- 문제6
SELECT
	customerNumber,officeCode,customers.city,offices.city
FROM
	customers
LEFT JOIN offices
	ON customers.city = offices.city

union

SELECT
	customerNumber,officeCode,customers.city,offices.city
FROM
	customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY
	customerNumber DESC;

-- 문제7

SELECT
	orderdetails.orderNumber,orderDate
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY
	orderNumber;
    
-- 문제8

SELECT
	orderdetails.orderNumber,products.productCode,productName
FROM
	orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;
    
-- 문제9
SELECT
	orderdetails.orderNumber,
    products.productCode,
    orderDate,
    productName
FROM
	orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY
	orderNumber;
    
