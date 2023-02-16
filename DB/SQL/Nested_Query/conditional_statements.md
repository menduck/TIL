# conditional statements

> CASE statement

: SQL 문에서 조건문을 구성

```SQL
CASE case_value
  WHEN when_value1 THEN staements
  WHEN when_value2 THEN staements
  -- some code...
  [ELSE else-statements] -- 선택사항이지만 쓰는 것을 권장
END CASE;
```

- case_value가 when_value와 동일한 것을 찾을 때까지 순차적으로 비교
- 만약 찾는다면 THEN 절 코드를 실행하고 찾지 못하면 ELSE 절 코드 실행
  - ELSE 절이 없을 때 동일한 값을 찾지 못한다면 에러 발생

## 예제1
- 고객들의 creditLimit에 따라 VIP, Platinum, Bronze 등급을 매겨 조회해라 (VIP 는 100000 초과, Platinum은 70000 초과 그 외는 Bronze로 지정)

```SQL
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
```
<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219424957-59bc766b-255f-44d5-bd8d-78f11fdd7765.PNG'>
</p>

## 예제2
- orders 테이블의 status에 따라 상세 정보를 매겨 조회해라
('In Process'는 '주문중', 'Shipped'는 '발주완료', 'Cancelled'는 '주문취소' 그 외는 '기타사유'로 지정)

```SQL
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
```

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/219424984-7d5bd483-4468-4534-afdc-920d9eaeccf1.PNG'>
</p>