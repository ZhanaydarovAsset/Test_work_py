from note.noteApp import NotesApp

if __name__ == "__main__":
    notes_app = NotesApp("C://Repo//Test_work//data//notes.json")

    while True:
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Редактировать заметку")
        print("4. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes_app.add_note(title, body)
        elif choice == "2":
            notes_app.list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            new_title = input("Введите новый заголовок (или нажмите Enter для пропуска): ")
            new_body = input("Введите новый текст (или нажмите Enter для пропуска): ")
            notes_app.edit_note(note_id, new_title, new_body)
        elif choice == "4":
            print("Выход из приложения.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
