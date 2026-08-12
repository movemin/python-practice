from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def first():
    return 'first'

@bp.route('second/')
def second():
    return 'second'