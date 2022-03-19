# '다코로그' 프로젝트
- 나만의 개인 블로그를 개발하고 있습니다.
- TDD를 적용하여 개발하고 있습니다.
- SQL 학습을 위해 ORM 라리브러리는 사용하지 않습니다.

<br>
<br>

## 사용기술
- FastAPI, MySQL

<br>
<br>


## 진행상황(최신순)
- api/blog - log가져오기 api 구현
- api/blog - log작성 api 구현
- api/blog - test code 작성

<br>
<br>

## Coverage

<br>

```
3월 19일 커버리지

Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
apps/__init__.py                  0      0   100%
apps/api/__init__.py              0      0   100%
apps/api/blog.py                 19      0   100%
apps/config.py                    2      0   100%
apps/main.py                     13      2    85%   17, 22
apps/model/__init__.py           21      4    81%   16, 20-22
apps/service/__init__.py          0      0   100%
apps/service/logs.py             23      0   100%
apps/tests/__init__.py            0      0   100%
apps/tests/api/test_blog.py      29      0   100%
apps/tests/test_main.py           7      0   100%
-----------------------------------------------------------
TOTAL                           114      6    95%
```