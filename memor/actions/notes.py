from django.db import transaction
from memor.models.notes import Note
from memor.models.reminders import Reminder
from injector import inject
from memor.repositories.notes import NotesRepository

class AddNote(object):

    @inject
    def __init__(self, notes_repository: NotesRepository):
        self.notes_repository = notes_repository

    @transaction.atomic
    def execute(self, text, added_on):
        note = Note(text=text, added_on=added_on)
        self.notes_repository.add_note(note)
        return note.id


class AddNoteReminder(object):

    @inject
    def __init__(self, notes_repository: NotesRepository):
        self.notes_repository = notes_repository

    @transaction.atomic
    def execute(self, note_id, remind_on):
        reminder = Reminder(remind_on=remind_on)
        self.notes_repository.add_note_reminder(note_id, reminder)


class ListNotes(object):

    @inject
    def __init__(self, notes_repository: NotesRepository):
        self.notes_repository = notes_repository

    def execute(self):
        return self.notes_repository.get_all()
