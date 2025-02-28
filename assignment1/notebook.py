class NoteBook:
    def __init__(self, notebook_name: str):
        self.notebook_name = notebook_name
        self.notes = {}

    def create_note(self, name: str, content: str):
        self.notes[name] = content

    def list_notes(self):
        return list(self.notes)

    def search_notes(self, term: str):
        return {name: content for name, content in self.notes.items() if term.lower() in name.lower() or term.lower() in self.notes[name].lower()}

    def get_note(self, name: str):
        return self.notes.get(name, None)
