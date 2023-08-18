import json
import os
from datetime import datetime
from note.note import Note


class NotesApp:
    def __init__(self, notes_file):
        self.notes_file = notes_file
        if not os.path.exists(self.notes_file):
            with open(self.notes_file, "w") as f:
                json.dump([], f)
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as f:
                notes_data = json.load(f)
                notes = [Note(**note_data) for note_data in notes_data]
                return notes
        else:
            return []

    def add_note(self, title, body):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_note = Note(len(self.notes) + 1, title, body, timestamp)
        self.notes.append(new_note)
        self.save_notes()
        print("Заметка добавлена.")

    def save_notes(self):
        notes_data = [note.to_dict() for note in self.notes]
        with open(self.notes_file, "w") as f:
            json.dump(notes_data, f, indent=4)

    def list_notes(self):
        for note in self.notes:
            print(note)
