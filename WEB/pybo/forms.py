from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('성수씨 제목 입력하세요')])
    content = TextAreaField('내용', validators=[DataRequired('성수씨 내용도 빠뜨렸어요')])
    
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('한빈씨 답변해주세요.')])