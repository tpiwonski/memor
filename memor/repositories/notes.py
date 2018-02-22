from memor.models.notes import Note

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
        return Note.objects.all()

    def remove_note_by_id(self, note_id):
        Note.objects.filter(id=note_id).delete()
