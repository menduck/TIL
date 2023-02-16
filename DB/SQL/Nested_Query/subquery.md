# Subquery
: 단일 쿼리문에 여러 테이블의 데이터를 결합하는 방법

## Subquery의 특징
1. 조건에 따라 하나 이상의 테이블에서 데이터를 검색하는 데 사용 가능
2. SELECT,FROM,WHERE,HAVING 절 등에서 사용 가능

- 예시
  - table1에서 가장 나이가 어린 사람을 삭제해야 한다.
  1. 가장 나이가 어린 사람을 찾고
  2. 삭제를 해야 한다.

  ```SQL
  -- 1. 가장 나이가 어린 사람을 찾고
  SELECT MIN(age)
  FROM table1;
  -- 2. 삭제를 해야 한다.
  DELETE FROM table1
  WHERE age = 위에서 찾은 최소값
  ```

  - 중첩쿼리(Subquery)를 쓰면?
  
  ```SQL
  DELETE FROM table1
  WHERE age = (
    SELECT MIN(age) FROM table1
  );
  ```

## 예제1
- 결제 금액이 가장 큰 고객 번호 조회(payments 테이블 활용)

```SQL
-- 1. amount의 최대값을 찾고
-- 2. 최대값을 가진 고객 번호를 찾는다.

SELECT customerNumber,amount
FROM payments
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);
```
<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219425227-cdc483da-219c-4e93-96b9-fe549e735502.PNG'>
</p>

## 예제1 - 심화
- 결제 금액이 가장 큰 고객의 customerNumber, amount, contacFirstName을 조회
(고객 테이블은 customers, 지불 테이블은 payments를 활용)

```SQL
-- 강의 답안
SELECT customerNumber,amount,contactFirstName
FROM (
  -- '주문한 고객과 주문 정보가 모두 들어가 있는 테이블에서'라는 의미
	SELECT *
	FROM payments
	INNER JOIN customers USING(customerNumb er)
) AS sub_customers -- FROM 파생쿼리는 반드시 별칭이 있어야 함.
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);

-- 내가 쓴 코드
SELECT payments.customerNumber,amount,contactFirstName
FROM payments
INNER JOIN customers
	ON customers.customerNumber = payments.customerNumber
WHERE amount = (
	SELECT MAX(amount)
	FROM payments
);
```

- 결과는 동일하지만 내 코드보다 강의 코드가 더 좋은 이유
  - 반복된 코드를 줄일 수 있다.
  - FROM에서 서브 쿼리를 사용함으로써 직관적으로 의미를 알 수 있다.
    - '주문한 고객과 주문 정보가 모두 들어가 있는 테이블에서'라는 의미를 바로 전달 할 수 있다.


<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219425232-869b0e13-da9c-4373-a5a6-d213b602e212.PNG'>
</p>


## 예제2
- 미국에 있는 사무실에서 근무하는 직원의 이름과 성 조회
(직원 정보는 employees, 사무실 정보는 offices 테이블 조회)

```SQL
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
    
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219425252-9ae426ff-40cb-4dba-b57b-1830c30cf163.PNG'>
</p>

## 예제3
- 주문한 적이 없는 고객 목록 조회
(고객 정보는 customers, 주문 정보는 orders 테이블에 존재)

```SQL
-- orders에는 주문한 고객 번호가 있다.
-- => 주문하지 않는 고객은 NOT IN 활용
-- orders에서 고객 주문 목록을 가져온다.
-- customers의 customerNumber와 위에서 가져온 customerNumber를 비교ALTER
-- 포함되지 않는 customerNumber의 customerName을 조회

SELECT customerName 
FROM customers
WHERE customerNumber not IN
	(
		SELECT DISTINCT customerNumber -- 중복 제거
    FROM orders
	);
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219425179-525e691e-f485-4d06-a7c8-3dbda9db9a7e.PNG'>
</p>

## EXISTS operator
: 쿼리 문에서 반환된 레코드의 존재 여부를 확인

```SQL
SELECT
  select_list
FROM
  table
WHERE
  [NOT] EXISTS (subquery);
```

- subquery가 하나 이상의 행을 반환하면 EXISTS 연산자는 true를 반환/ 그렇지 않다면 false를 반환
- 주로 WHERE절에서 subquery의 반환 값 존재 여부를 확인하는데 사용


## 예제1
- 적어도 한 번 이상 주문을 한 고객들의 번호와 이름을 조회해라
(고객 테이블 customers, 주문 테이블은 orders이며 두 테이블은 customerNumber 필드를 기준으로 비교)

```SQL
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
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219425189-df7ecdc4-35b9-49b6-ae32-c76eca0e947c.PNG'>
</p>

## 예제2
- Paris에 있는 사무실에서 일하는 모든 직원의 번호, 이름, 성을 조회해라
(직원 테이블은 employees, 사무실 테이블은 offices이며 두 테이블의 officeCode 필드를 기준으로 비교)

```SQL
-- WHERE로 푼 풀이
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

-- subquery로만 푼 풀이
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
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219425217-ac0ec5a7-0a4e-4971-9c4d-51b67925b1a2.PNG'>
</p>

