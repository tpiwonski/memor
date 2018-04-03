from memor.entities.notes import NoteEntity as Note, NoteReminderEntity as NoteReminder

from datetime import datetime
from uuid import uuid4

class AddNoteInteractor(object):

    def __init__(self, factory, repository, presenter):
        self.factory = factory
        self.repository = repository
        self.presenter = presenter

    def execute(self, **request):
        note = self.factory.new_note(text=request['note_text'], created_on=datetime.now())
        self.repository.add_note(note)
        self.presenter.present_note(note=note)

        ######################################3
        self.note_id = note.id
        ######################################


class ShowNotesInteractor(object):  
    
    def __init__(self, repository, presenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self):
        notes = self.repository.get_notes()
        self.presenter.present_notes(notes=notes)


class AddNoteReminderInteractor(object):

    def __init__(self, factory, repository, presenter):
        self.factory = factory
        self.repository = repository
        self.presenter = presenter

    def execute(self, **request):
        note = self.repository.get_note(request['note_id'])
        reminder = self.factory.new_note_reminder(note=note, remind_on=request['note_remind_on'])
        self.repository.save_note_reminder(reminder)


class DeleteNoteInteractor(object):

    def __init__(self, repository, presenter):
        self.repository = repository
        self.presenter = presenter

    def execute(self, **request):
        self.repository.remove_note(request['note_id'])
