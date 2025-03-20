from . import db
from .model import Note, Comment

def create_note(title, content):
    note = Note(title=title, content=content)
    db.session.add(note)
    db.session.commit()

def list_notes():
    return Note.query.all()

def search_notes(term):
    return Note.query.filter((Note.title.ilike(f"%{term}%")) | (Note.content.ilike(f"%{term}%"))).all()

def get_note(note_id):
    return Note.query.get(note_id)

def add_comment(note_id, content):
    comment = Comment(note_id=note_id, content=content)
    db.session.add(comment)
    db.session.commit()

def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
