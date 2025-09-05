from app import db
from flask_login import UserMixin

class Users_Data(db.Model, UserMixin):
    __tablename__ = "User_data"
    
    uid = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    created_on = db.Column(db.Text, nullable=False)
    
    
    notes = db.relationship('Notes', backref='owner', lazy=True)

    def __repr__(self):
        return self.username
    
    def get_id(self):
        return self.uid


class Notes(db.Model, UserMixin):
    __tablename__ = "Users_Notes"
    
    nid = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_on = db.Column(db.Text, nullable=False)
    
    # fixed foreign key to match Users_Data
    user_id = db.Column(db.Integer, db.ForeignKey('User_data.uid'), nullable=False)

    def __repr__(self):
        return f"{self.nid}. {self.title}"
