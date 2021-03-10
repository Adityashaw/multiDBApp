from . import db


class Faculty(db.Model):
    __tablename__ = 'faculty'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    isAdmin = db.Column(db.Boolean, server_default="0")


class Student(db.Model):
    __tablename__ = 'student'
    __bind_key__ = 'students'

    id = db.Column(db.SmallInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.SmallInteger, nullable=False)
    roll_number = db.Column(db.String(15), nullable=False, unique=True)
