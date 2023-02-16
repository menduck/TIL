-- 예제1
SELECT 
	contactFirstName,
    creditLimit,
    CASE -- CASE로 grade 필드를 만드는 거임
		WHEN creditLimit > 100000 THEN 'VIP'
		WHEN creditLimit > 70000 THEN 'Platinum'
		ELSE 'Bronze'
    END AS grade
FROM 
	customers;

-- 예제2
SELECT 
	orderNumber,
    status,
    CASE
		WHEN status = 'In Process' THEN '주문중'
		WHEN status = 'Shipped' THEN '발주완료'
		WHEN status = 'Cancelled' THEN '주문취소'
        ELSE '기타사유'
    END AS 'details'
FROM
	orders;
    