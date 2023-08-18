from note.noteApp import NotesApp

if __name__ == "__main__":
    notes_app = NotesApp("C://Repo//Test_work//data//notes.json")

    while True:
        print("1. Добавить заметку")
        print("2. Список заметок")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            notes_app.add_note(title, body)
        elif choice == "2":
            notes_app.list_notes()
        elif choice == "3":
            print("Выход из приложения.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
