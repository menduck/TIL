# 왜 join 키워드를 사용하는가?
- DB에서 하나의 테이블이 아닌 여러 테이블로 나누어 저장하고 결합하여 출력한다.
  - 왜? 데이터 관리의 편이를 위해서
- 독립적인 테이블에 관계를 만들어내기 위해서 외래키 필드를 작성한다.
- 하지만 출력 시 테이블 한 개만 출력가능하기 때문에 다른 테이블과 연결지어 출력하는 것이 필요!하다. => ***JOIN***

# Joining table

> JOIN clause

- 둘 이상의 테이블에서 데이터를 검색하는 방법

# JOIN의 종류
## INNER JOIN

> INNER JOIN clause

- 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환



```SQL
SELECT
  select_list
FROM
  main_table -- 메인 테이블 지정
INNER JOIN sub_table -- 메인 테이블과 결합할 서브 테이블 지정
  ON main_table.fk = sub_table.pk; -- 조인 조건 작성(메인테이블과 서브테이블 간의 레코드를 일치시키는 규칙을 설정)
```

### 예시 1 - articles의 userID를 기준으로 user의 id필드 조인하기

```SQL
SELECT
  articles.id, title, content, name -- 겹치는 필드이면 테이블.필드 형식으로 작성
FROM
  articles -- 메인 테이블 지정
INNER JOIN users -- 메인 테이블과 결합할 서브 테이블 지정
  ON articles.userId = users.id; -- 교집합인 조건
```
<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025371-ea6a5252-c5d0-46db-bac2-4a0d4aedc0b2.PNG'>
</p>

### 예시 2 

- productLine 값이 같은 레코드의 productCode, productName, textDescription 필드를 조회

```SQL
SELECT
	productCode,productName,textDescription
FROM
	products
INNER JOIN productlines
	ON products.productLine = productlines.productLine;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025380-4073fe4a-68eb-4b10-bfa0-f27b27ec699d.PNG'>
</p>

### 예시 3 

- orderNumber 값이 같은 레코드의 orders 테이블 orderNumber, status, 총액 필드를 조회

```SQL
SELECT
	orders.orderNumber,status,priceEach*quantityOrdered AS '총액' 
    -- 겹치는 필드이면 테이블.필드 형식으로 작성
FROM
	orders
INNER JOIN orderdetails
	ON orders.orderNumber = orderdetails.orderNumber;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025392-3d4ae36d-7cd3-4398-8999-65037a8fc10a.PNG'>
</p>



### 예시 4
- 예시 3번 조회에 각 주문번호 별 주문 상태와 총 판매액을 요약(주문번호는 orderNumber 필드, 총 판매액은 quantityOrdered와 priceEach필드의 곱셈 결과)

```SQL
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
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025413-977df133-1a31-4091-9ed7-2cb77f95bc39.PNG'>
</p>


## OUTER JOIN
### LEFT JOIN
- 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
- 일치하지 않는 레코드는 NULL로 채워진다.


```SQL
SELECT
  select_list
FROM
  left_table -- 왼쪽 테이블 지정
LEFT [OUTER] JOIN rigth_table -- 왼쪽 테이블과 결합할 오른쪽 테이블 지정
  ON main_table.fk = sub_table.pk; -- 조인 조건 작성(왼쪽테이블과 오른쪽테이블 간의 레코드를 일치시키는 규칙을 설정)
```

#### 예시 1
  - customers를 기준으로 customerNumber필드가 일치하는 레코드와 함께 customers 테이블 contactFirstName와 order테이블의 orderNumber, status 필드 조회 (왼쪽 테이블은 customers, 오른쪽 테이블은 orders, 일치하지 않는 경우 NULL)

```SQL
  SELECT
	contactFirstName,orderNumber,status
FROM
	customers -- 왼쪽테이블
LEFT JOIN orders -- 오른쪽테이블
	ON customers.customerNumber = orders.customerNumber;
-- 만약 inner join이면 주문이 없는 사람은 빠진다.(left join이기 때문에 주문이 없으면 Null값으로 표시)
```
<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025637-8e00cc0c-283d-488c-8456-8f97bf1b142c.PNG'>
</p>


#### 예시 2
  - 예시1 조회 결과에서 주문 내역이 없는 고객의 이름과 주문번호 및 배송상태를 조회

```SQL
SELECT
	contactFirstName,orderNumber,status
FROM
	customers -- 왼쪽테이블
LEFT JOIN orders -- 오른쪽테이블
	ON customers.customerNumber = orders.customerNumber
WHERE orderNumber is NULL;
```
<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025646-64b87690-cd7f-441b-b4bf-4c6ccda6b043.PNG'>
<img src = 'https://user-images.githubusercontent.com/39366835/219025643-2f48e4b9-61b6-4d18-a0eb-bb00cdcfa9cc.PNG'>
</p>

### RIGHT JOIN
: 왼쪽 테이블의 일치하는 레코드와 함께 오른쪽 테이블의 모든 레코드 반환
- 왼쪽 테이블에 일치하는 레코드가 없으면 NULL

```SQL
SELECT
  select_list
FROM
  left_table -- 왼쪽 테이블 지정
RIGHT [OUTER] JOIN rigth_table -- 왼쪽 테이블과 결합할 오른쪽 테이블 지정
  ON main_table.fk = sub_table.pk; -- 조인 조건 작성(왼쪽테이블과 오른쪽테이블 간의 레코드를 일치시키는 규칙을 설정)
```

#### 예시 1
- employeNumber 필드와 salesRepEmployeeNumber 필드가 일치하는 레코드와 함께 employeeNumber,firstName,customerNumber,contactFirstName 필드를 조회해라.

```SQL
SELECT
	employeeNumber,firstName,customerNumber,contactFirstName
FROM customers
RIGHT JOIN employees
	ON  employeeNumber = salesRepEmployeeNumber;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025906-b72b8d93-05b9-4b24-856b-a3cd84d7a728.PNG'>
</p>

#### 예시2
- 위 예시1 조회 결과에서 고객에게 판매한 내역이 없는 직원 목록 조회해라.

```SQL
SELECT
	employeeNumber,firstName,customerNumber,contactFirstName
FROM customers
RIGHT JOIN employees
	ON  employeeNumber = salesRepEmployeeNumber
WHERE customerNumber IS NULL;
```
<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219025902-6e83461a-e586-490e-bbef-040eb7588914.PNG'>
<img src = 'https://user-images.githubusercontent.com/39366835/219025913-ed6c5b97-0b4a-4763-80a9-935b374b4309.PNG'>
</p>

## CROSS JOIN
