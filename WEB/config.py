# 파이썬 기본 제공 모듈
# 컴퓨터 환경(Windows, Mac, Linux)에 접근할 수 있게 해주는 최상위 도구 상자입니다.

import os

# 1. Docker 가상 오라클 서버 접속 정보
ORACLE_USER = 'SYSTEM'             # 오라클 관리자 계정
ORACLE_PASSWORD = '1234'   # 설정한 비밀번호 (gvenzl 이미지 기본 비밀번호 또는 설정값)
ORACLE_HOST = 'localhost'          # 내 컴퓨터 안의 가상화 서버이므로 localhost
ORACLE_PORT = '1521'               # 기본 오라클 포트
ORACLE_SERVICE = 'FREEPDB1'        # Docker 오라클 서비스명

# 2. SQLAlchemy 접속 URI 설정 (oracle+oracledb 사용)
# 1. 포트 뒤에 슬래시(/)를 붙이고 서비스 이름을 바로 연결하는 오라클 표준 URI 사용
SQLALCHEMY_DATABASE_URI = fSQLALCHEMY_DATABASE_URI = f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASSWORD}@{ORACLE_HOST}:{ORACLE_PORT}/?service_name={ORACLE_SERVICE}"
# 3. 객체 변경 추적 비활성화
SQLALCHEMY_TRACK_MODIFICATIONS = False


# ---오라클 버전---
# pip install oracledb

# 프로젝트 내에 마이그레이션 이력을 관리할 migrations 폴더를 생성합니다.
# python -m flask --app pybo db init  # 마이그레이션 환경 최초 설정 (1회성)

# models.py에 정의된 클래스(예: Question)와 실제 오라클 DB의 상태를 비교하여, 
# 변경된 내용을 바탕으로 migrations/versions/ 폴더 안에 자동으로 실행용 파이썬 스크립트(예: a1b2c3d4_add_question.py)를 생성합니다.
# python -m flask --app pybo db migrate  # DB 변경 사항 추적 및 마이그레이션 스크립트(파일) 생성

# db migrate로 생성된 스크립트를 읽어서, 
# 오라클 DB에 실제 DDL 문(CREATE TABLE ... 등)을 수행하여 
# 테이블을 진짜로 생성하거나 수정합니다.
# python -m flask --app pybo db upgrade  # 생성된 마이그레이션 스크립트를 실제 DB에 적용