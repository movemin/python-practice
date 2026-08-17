from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# 데이터베이스 조종기
# 파이썬 코드로 DB 데이터를 조작할 수 있게 해주는 조종기
db = SQLAlchemy()

# DB 테이블 구조가 바뀔 때(컬럼 추가 등)
# 기존 데이터를 잃지 않고 안전하게 DB를 업데이트(버전 관리)해 주는 관리자입니다.
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    # from_object()는 파이썬 모듈/클래스 객체(config)를 읽어서, 
    # 그 안에 대문자로 적힌 변수들을 Flask 앱의 설정으로 등록해 줍니다.
    app.config.from_object(config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    
    from . import models # 작성 후: python -m flask --app pybo db migrate
    
    return app