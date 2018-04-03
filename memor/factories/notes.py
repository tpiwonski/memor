from uuid import uuid4

from memor.models.notes import Note as NoteModel, NoteReminder as NoteReminderModel
from memor.models.reminders import Reminder as ReminderModel
from memor.entities.notes import NoteEntity, NoteReminderEntity

class NotesFactory(object):

    def new_note(self, **data):
        data = NoteModel(id=str(uuid4()), **data)
        note = NoteEntity(data)
        return note

    def new_note_reminder(self, **data):
        data = NoteReminderModel(id=str(uuid4()), note=data['note']._data, 
            reminder=ReminderModel(id=str(uuid4()), remind_on=data['remind_on']))
        reminder = NoteReminderEntity(data)
        return reminder
