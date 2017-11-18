class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    diary = db.relationship('Diary', kackref='user')

class Diary(db.model):
    __tablename__ = 'diarys'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    data = db.Column(db.Text)
    rate = db.Column(db.Integer)
    tag = db.Column(db.Integer)
    question = db.Column(db.Integer)
    answer = db.Column(db.Text)
    diary_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
