import streamlit as st
from notebook import NoteBook

if "notes" not in st.session_state:
    st.session_state.notes = NoteBook("notes")

st.title("Notebook")

st.sidebar.header("Add note")
name = st.sidebar.text_input("Note name")
content = st.sidebar.text_area("Note content")

if st.sidebar.button("Create note"):
    if name and content:
        st.session_state.notes.create_note(name, content)
        st.sidebar.success("Note saved")
    else:
        st.sidebar.error("Both name and content are required")

search_term = st.text_input("Search notes", "")

if search_term:
    filtered_notes = st.session_state.notes.search_notes(search_term).keys()
else:
    filtered_notes = st.session_state.notes.list_notes()

st.subheader("Notes list")
if filtered_notes:
    for note in filtered_notes:
        if st.button(note, key=note):
            st.session_state["selected_note"] = note
else:
    st.info("No notes found")

if "selected_note" in st.session_state:
    selected_note = st.session_state["selected_note"]
    content = st.session_state.notes.get_note(selected_note)

    st.subheader(f"{selected_note}")
    st.write(content)
