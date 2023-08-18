import json
import os
from datetime import datetime
from note.note import Note


class NotesApp:
    def __init__(self, notes_file):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            if os.path.exists(self.notes_file):
                with open(self.notes_file, "r") as f:
                    notes_data = json.load(f)
                    notes = [Note(**note_data) for note_data in notes_data]
                    return notes
            else:
                return []
        except json.JSONDecodeError:
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
        sorted_notes = sorted(self.notes, key=lambda note: note.timestamp, reverse=True)
        for note in self.notes:
            print("ID:", note.id)
            print("Заголовок:", note.title)
            print("Тело:", note.body)
            print("Дата/время:", note.timestamp)
            print("=" * 30)

    def edit_note(self, note_id, new_title=None, new_body=None):
        for note in self.notes:
            if note.id == note_id:
                if new_title is not None:
                    note.title = new_title
                if new_body is not None:
                    note.body = new_body
                self.save_notes()
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")