from memor.models.notes import Note as NoteModel
from memor.entities.notes import NoteEntity

class AddNoteRepository(object):
    
    def add_note(self, note):
        note._data.save()


class ShowNotesRepository(object):
    
    def get_notes(self):
        return [NoteEntity(data) for data in NoteModel.objects.all()]


class AddNoteReminderRepository(object):
    
    def get_note(self, note_id):
        return NoteEntity(NoteModel.objects.get(id=note_id))

    def save_note_reminder(self, reminder):
        reminder._data.reminder.save()
        reminder._data.save()

class DeleteNoteRepository(object):
    
    def remove_note(self, note_id):
        note = NoteModel.objects.get(id=note_id)
        for r in note.reminders.all():
            r.delete()
        
        note.delete()


class NotesRepository(object):

    def add_note(self, note):
        note.save()

    def get_note(self, note_id):
        return Note.objects.get(id=note_id)

    def add_note_reminder(self, note_id, reminder):
        reminder.save()
        note = Note.objects.get(id=note_id)
        note.notereminder_set.create(reminder=reminder)
        note.save()

    def get_all(self):
        return NoteModel.objects.all()

    def remove_note_by_id(self, note_id):
        note = NoteModel.objects.get(id=note_id)
        for r in note.reminders.all():
            r.delete()
        
        note.delete()
