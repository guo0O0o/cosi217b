from . import db
from datetime import datetime

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='note', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Note {self.title}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)

    def __repr__(self):
        return f'<Comment {self.content[:30]}>'
