from flask import Flask, render_template, request, redirect, url_for
from notebook import NoteBook

app = Flask(__name__)
notes = NoteBook("notes")

@app.route("/", methods=["GET", "POST"])
def index():
    search_term = request.args.get("search", "")
    if search_term:
        searched_notes = notes.search_notes(search_term).keys()
    else:
        searched_notes = notes.list_notes()

    if request.method == "POST":
        name = request.form["name"]
        content = request.form["content"]
        notes.create_note(name, content)
        return redirect(url_for("index"))

    return render_template("index.html", notes=searched_notes, search_term=search_term)

@app.route("/note/<name>")
def view_note(name):
    content = notes.get_note(name)
    if content is None:
        return "Note not found", 404
    return render_template("note.html", name=name, content=content)

if __name__ == "__main__":
    app.run(debug=True)
