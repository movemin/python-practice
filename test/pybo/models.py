from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(4000), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, ForeginKey('question.id', ondelete='CASCADE'))
    question = 
    content = db.Column(db.String(4000), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)