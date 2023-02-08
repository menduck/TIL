# 관계형 데이터 베이스
- 테이블화 구조화 되어 있고 테이블 간의 관계는 외래 키로 참조하여 만든다.
- 테이블을 조인하여 정보 간 관계를 설정하는 기능이 있어,여러 데이터 간의 관계를 쉽게 이해하고 정보를 얻을 수 있다.
## 관계형 데이터 베이스의 용어 정리

### Table(aka. Relation)
- 데이터를 기록하는 공간

### Field(aka. Column,Attribute)
- 테이블의 열을 필드라고 함
- 각 필드에는 고유한 데이터 타입이 지정됨.

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/217449037-f363c0f1-3ed7-4e43-82d5-3de8563b3ee9.PNG'>
</p>

### Recode(aka. Row,Tuple)
- 테이블의 행을 레코드라고 함
- 각 레코드에는 데이터 값을 저장함
** 여기서의 Tuple은 python의 Tuple을 지칭하는 것이 아님.

### Database(aka. Schema)
- 테이블의 집합

### Primary key(기본 키, PK)
- 각 레코드의 고유한 값
- 관계형 데이터베이스에서 레코드의 식별자로 활용
- ex) id, 주민등록번호
- 이름, 주소와 같이 중복된 값이 있을지 모르는 데이터는 기본 키로 사용하지 않음.

### Foreign key(외래 키, FK)
- 테이블의 필드(열) 중 다른 테이블의 레코드(행)를 식별할 수 있는 키
- 각 레코드에서 서로 다른 테이블 간의 ***관계*** 를 만드는데 사용

## RDBMS(Relational Database Management System)
: ***관계형***  데이터 베이스를 관리하는 소프트웨어 프로그램

- 데이터 저장 및 관리를 용이하게 하는 시스템
- 데이터와 사용자 간의 인터페이스 역할
  - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움을 줌

- RDBMS의 종류
  - MySQL
  - PostgreSQL
  - Oracle DataBase
  - MS SQL Server

### MySQL
- 오픈 소스 RDBMS
- 다양한 운영체제에서 실행 가능
- 여러 프로그래밍 언어를 위한 다양한 API 제공
- 그래픽 인터페이스 제공(GUI) => MySQL Workbench Tool

#### MySQL 구조
- table < DB < DB server(MySQL)

