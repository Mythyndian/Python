import sys
from datetime import datetime


class Note:
    ID: int = 0

    def __init__(self, text, tag):
        Note.ID += 1
        self.id = Note.ID
        self.text = text
        self.tag = tag
        self.date = datetime.now().time()

    def match(self, some_text):
        if self.text in some_text | self.tag in some_text:
            return True
        else:
            return False

    def __str__(self):
        return f"""
                {self.text}
                Note id: {self.id}
                Tag: {self.tag}
                Creation Date: {self.date}
                """


class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, text, tag):
        self.notes.append(Note(text, tag))

    def modify_text(self, identity, modified_text):
        for i in self.notes:
            if i.id == identity:
                i.text = modified_text

    def modify_tag(self, identity, modified_tag):
        for i in self.notes:
            if i.id == identity:
                i.tag = modified_tag

    def search(self, phrase):
        results = []
        for i in self.notes:
            if phrase in i.text or phrase in i.tag:
                results.append(i)
        return results


def show_menu():
    print("""
    1.Show notes
    2.Search notes
    3.Add note
    4.Modify note
    5.Quit
    """)


class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.options = {"1": self.show_notes, "2": self.search_notes,
                        "3": self.add_note, "4": self.modify_note,
                        "5": self.quit}

    def run(self, option):
        self.options[option]()

    def show_notes(self):
        for note in self.notebook.notes:
            print(note)

    def search_notes(self):
        print('Initialising searching sequence...')
        searching_phrase = input('Input phrase to search: ')
        results = self.notebook.search(searching_phrase)
        for i in results:
            print(i)

    def add_note(self):
        print('Creating new note...')
        new_tag = input('Input tag: ')
        new_text = input('Input note: ')
        self.notebook.new_note(new_text, new_tag)
        print('Note created successfully!')

    def modify_note(self):
        print("""Modifying note...
                 Showing notes available for modification
              """)
        self.show_notes()
        note_id = str(input('Input id of note that you want to modify: '))
        modify_target = input('What you want to change: (input text or tag) ')
        if modify_target == 'tag':
            modified_tag = input('Input new tag: ')
            self.notebook.modify_tag(note_id, modified_tag)
        if modify_target == 'text':
            modified_text = input('Input new text: ')
            self.notebook.modify_text(note_id, modified_text)

    def quit(self):
        print('Thanks for using my note organising program :)')
        sys.exit(0)


if __name__ == '__main__':
    Menu = Menu()
    print('Note organiser ver. 1.0')
    while True:
        show_menu()
        choice = input('Your choice (1-5):')
        Menu.run(choice)
