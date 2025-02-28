from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory storage for notes
notes: Dict[str, str] = {}

class Note(BaseModel):
    name: str
    content: str

@app.get("/")
def directions():
    return {
        "message": "Notebook API. See ",
        "list_notes": "GET /list",
        "find_notes": "GET /find?term={term}",
        "get_note": "GET /note/{name}",
        "add_note": "POST /add"
    }

@app.get("/list")
def list_notes():
    return {"notes": list(notes.keys())}

@app.get("/find")
def search_notes(term: str):
    matching_notes = {name: content for name,content in notes.items() if term.lower() in name.lower() or term.lower() in notes[name].lower()}
    return matching_notes

@app.get("/note/{name}")
def get_note(name: str):
    return notes[name]

@app.post("/add")
def create_note(note: Note):
    notes[note.name] = note.content
    return {"message": "Note added successfully"}
