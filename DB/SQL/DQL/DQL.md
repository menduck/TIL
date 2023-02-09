# DQL(Data Query Language)
- 데이터 검색
- SQL 키워드: SELECT

## 1. Querying data

> SELECT statements
- 테이블에서 테이터를 조회

```SQL
SELECT
  select_list --조회할 필드를 하나 이상 지정
FROM
  table_name; -- 조회할 데이블 지정
```

### 예제1 - 하나의 필드 조회
  - 테이블 employees에서 lastName 필드의 모든 데이터를 조회해보자

```SQL
SELECT lastName FROM employees;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217733235-4d8f21e3-8c26-4fd8-b31c-786298bb4ffe.PNG'>
</p>

### 예제2 - 두개의 필드 조회
  - 테이블 employees에서 lastName, firstName 필드의 모든 데이터를 조회해보자

```SQL
SELECT
	lastName, firstName 
FROM 
	employees;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217733896-f250f345-7434-4fb3-9191-99041379a39f.PNG'>
</p>

### 예제3 - 모든 필드 *
  - 테이블 employees에서 모든 필드를 조회해보자

```SQL
SELECT
	* -- asterisk는 모든 필드를 의미함
FROM 
	employees;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217828869-5aeac723-b7ba-4d0e-9d2c-ab7c44407129.PNG'>
</p>


### 예제4 - 별칭 AS
  - 테이블 employees에서 firstName 필드의 모든 데이터 조회해보자 (단, 조회 시 firstName이 아닌 '이름'으로 출력명 변경)

```SQL
SELECT
	firstName AS '이름'
FROM 
	employees;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217829152-fe6dbaac-4368-4107-b089-584014a4d87a.PNG'>
</p>

### 예제5 - 사칙연산/별칭
  - 테이블 orderdetails에서 productCode 주문 총액 필드의 모든 데이터 조회해보자 (단, 주문 총액 필드는 quantityOrdered와 priceEach 필드를 곱한 결과값)

```SQL
SELECT
	productCode,
    quantityOrdered * priceEach as '주문 총액'
FROM 
	orderdetails;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217837678-aafabd89-3381-4be9-8bbd-518bc004476e.PNG'>
</p>


## 2. Sorting data

>ORDER BY clause

: 코드 결과의 레코드를 정렬

```SQL
SELECT
  select_list
FROM
  table_name
ORDER BY 
  col1 ASC -- 오름차순(기본값,생략가능)
  col2 DESC -- 내림차순
```

### 예제1. - 오름차순
- 테이블 employees에서 firstName 필드의 모든 데이터를 오름차순으로 순회하자

```SQL
SELECT
    firstName
FROM 
	employees
ORDER BY
	firstName;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217837695-96c80d92-acfc-483e-ba96-cbc29429669d.PNG'>
</p>

### 예제2. - 내림차순
- 테이블 employees에서 firstName 필드의 모든 데이터를 내림차순으로 순회하자

```SQL
SELECT
    firstName
FROM 
	employees
ORDER BY
	firstName DESC;
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217837711-40208695-cde4-47f4-aca9-1d2c0701d863.PNG'>
</p>

### 예제3 - 다중조건으로 정렬
- 테이블 employees에서 lastName 필드 기준 내림차순 정렬 후 firstName 필드 기준으로 오름차순 정렬하여 조회하자

```SQL
SELECT
	lastName,
  firstName
FROM 
	employees
ORDER BY
	lastName DESC,
	firstName; -- 오름차순은 생략가능
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217837747-100f8663-a628-4d53-b8bf-e8768574336c.PNG'>
</p>

### 예제4 - 사칙연산 후 이름을 바꾼 필드(별칭) 정렬
- 테이블 orderdetails에서 totalSales 필드 기준 내림차순 정렬 후 productCode,totalSales 필드 모든 데이터 조회하자.(단, totalSales 필드는 quantityOrdered와 priceEach 필드를 곱한 결과 값)

```SQL
SELECT
	productCode,
    quantityOrdered * priceEach AS 'totalSales'
FROM 
	orderdetails
ORDER BY
	totalSales DESC -- 별칭 실행도 됨
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217837756-6f44ed16-b940-4111-94b3-8c5504edaad5.PNG'>
</p>

## 3. Filtering data
## 4. Grouping data
