from django.utils import timezone

from injector import inject

from memor.models.notes import Note
from memor.repositories.notes import NotesRepository


class NotesService(object):

    @inject
    def __init__(self, notes_repository: NotesRepository):
        self.notes_repository = notes_repository

    def create_note(self, text):
        note = Note(text=text, added_on=timezone.now())
        self.notes_repository.add_note(note)

    def get_note_by_id(self, note_id):
        return self.notes_repository.get_note(note_id)

    def add_note_reminder(self, note_id, reminder):
        self.notes_repository.add_note_reminder(note_id, reminder)
    
    def get_all_notes(self):
        return self.notes_repository.get_all()

    def delete_note_by_id(self, note_id):
        self.notes_repository.remove_note_by_id(note_id)
