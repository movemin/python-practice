from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'hi'

@bp.route('second/')
def second():
    return 'hello'