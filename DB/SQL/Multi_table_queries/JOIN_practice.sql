-- INNER JOIN
DROP TABLE IF EXISTS users; -- users 필드가 있다면 삭제한다.
DROP TABLE IF EXISTS articles; -- users 필드가 있다면 삭제한다.

CREATE TABLE users (
	id INT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE articles (
	id INT AUTO_INCREMENT,
    title VARCHAR(50) NOT NULL,
    content VARCHAR(100) NOT NULL,
    userId INT NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO
	users (name)
VALUES
	('권미자'),
	('류준하'),
	('정영식');

    
INSERT INTO
	articles (title, content, userId)
VALUES
	('제목1','내용1',1),
	('제목2','내용2',2),
	('제목3','내용3',4);

SELECT * FROM users;
SELECT * FROM articles;

-- INNER JOIN 예시 1
SELECT
  articles.id, title, content, name -- 겹치는 필드이면 테이블.필드 형식으로 작성
FROM
  articles -- 메인 테이블 지정
INNER JOIN users -- 메인 테이블과 결합할 서브 테이블 지정
  ON articles.userId = users.id; -- 교집합인 조건

-- 예시2
SELECT
	productCode,productName,textDescription
FROM
	products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;
    
-- 예시3
SELECT
	orders.orderNumber,status,priceEach*quantityOrdered AS '총액' 
    -- 겹치는 필드이면 테이블.필드 형식으로 작성
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
    
-- 예시4
SELECT
	orders.orderNumber,
    status,
    SUM(priceEach*quantityOrdered) AS 'totalSales' 
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber
GROUP BY
	orderNumber;

-- LEFT JOIN    
-- 예시 1
SELECT
	contactFirstName,orderNumber,status
FROM
	customers -- 왼쪽테이블
LEFT JOIN orders -- 오른쪽테이블
	ON customers.customerNumber = orders.customerNumber;
-- 만약 inner join이면 주문이 없는 사람은 빠진다.(left join이기 때문에 주문이 없으면 Null값으로 표시)

-- 예시2
SELECT
	contactFirstName,orderNumber,status
FROM
	customers -- 왼쪽테이블
LEFT JOIN orders -- 오른쪽테이블
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber is NULL;

-- rigth join
-- 예시1
SELECT
	employeeNumber,firstName,customerNumber,contactFirstName
FROM customers
RIGHT JOIN employees
	ON  employeeNumber = salesRepEmployeeNumber;
    
-- 예시2
SELECT
	employeeNumber,firstName,customerNumber,contactFirstName
FROM customers
RIGHT JOIN employees
	ON  employeeNumber = salesRepEmployeeNumber
WHERE customerNumber IS NULL;