from flask import Blueprint, render_template, request, redirect, url_for
from .notes import create_note, list_notes, search_notes, delete_note, add_comment
from .model import Note, Comment

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    search_query = request.args.get('search', '')
    notes = search_notes(search_query) if search_query else list_notes()
    return render_template('index.html', notes=notes)

@bp.route('/note/<int:note_id>')
def note(note_id):
    note = Note.query.get_or_404(note_id)
    return render_template('note.html', note=note)

@bp.route('/add_note', methods=['POST'])
def add_note():
    title = request.form['title']
    content = request.form['content']
    create_note(title, content)
    return redirect(url_for('main.index'))

@bp.route('/add_comment/<int:note_id>', methods=['POST'])
def add_note_comment(note_id):
    content = request.form['content']
    add_comment(note_id, content)
    return redirect(url_for('main.note', note_id=note_id))

@bp.route('/delete_note/<int:note_id>', methods=['POST'])
def delete(note_id):
    delete_note(note_id)
    return redirect(url_for('main.index'))
