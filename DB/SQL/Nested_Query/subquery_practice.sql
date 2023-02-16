-- subquery
-- 예제1
-- 1. amount의 최대값을 찾고
-- 2. 최대값을 가진 고객 번호를 찾는다.

SELECT customerNumber,amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

-- 예제1 - 심화
SELECT customerNumber,amount,contactFirstName
FROM (
	SELECT *
	FROM payments
	INNER JOIN customers USING(customerNumber)
) AS sub_customers -- FROM 파생쿼리는 반드시 별칭이 있어야 함.
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);


-- 예제2
-- 1. 미국 사무실 코드를 가지고 있는 목록 
--  => offices테이블을 통해 officeCode가 1,2,3이면 미국 사무실인 것을 확인함.
-- 2. employees 테이블에서 officeCode가 1,2,3인지 확인

SELECT lastName,firstName
FROM employees
WHERE officeCode IN
	(
    SELECT officeCode
	FROM offices
	WHERE country = 'USA'
    );

-- 예제3
-- orders에는 주문한 고객 번호가 있다.
-- => 주문하지 않는 고객은 NOT IN 활용
-- orders에서 고객 주문 목록을 가져온다.
-- customers의 customerNumber와 위에서 가져온 customerNumber를 비교ALTER
-- 포함되지 않는 customerNumber의 customerName을 조회

SELECT customerName 
FROM customers
WHERE customerNumber not IN
	(
		SELECT customerNumber FROM orders
	);

-- exists
-- 예제1
SELECT 
	customerNumber,
    customerName
FROM
	customers
WHERE EXISTS ( -- TRUE인 레코드만 조회됨/만약 아무것도 조회되지 않는다면 아무것도 반환되지 않는다.
	SELECT *
    FROM orders
    WHERE customers.customerNumber = orders.customerNumber
);

-- 예제2
SELECT 
	employeeNumber,firstName,lastName
FROM
	employees
WHERE EXISTS (
    SELECT * FROM offices
    WHERE
		city = 'Paris' -- 여기까지만 작성하면 전체 유저가 다 나옴 / '파리에 사무실이 있다면'이 조건이 아니라 '파리에 있는 사무실에서 일하는 직원'이 조건이기 때문에
        AND employees.officeCode = offices.officeCode
    );

SELECT 
	employeeNumber,firstName,lastName
FROM
	employees
WHERE 
	officeCode IN 
    (
    SELECT officeCode FROM offices
    WHERE city = 'Paris'
    );
    
    