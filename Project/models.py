from Project import db

class Component(db.Model):
    __tablename__='Components'
    id=db.Column(db.Integer,primary_key = True)
    name=db.Column(db.Text)

    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name