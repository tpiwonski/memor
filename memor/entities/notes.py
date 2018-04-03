# from memor.models.notes import Note, NoteReminder

class NoteEntity(object):
    # class Meta:
    #     proxy = True

    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data.id

    @property
    def text(self):
        return self._data.text

    @property
    def created_on(self):
        return self._data.created_on

    # def add_reminder(self, reminder):
    #     reminder.note = self 


class NoteReminderEntity(object):
    # class Meta:
    #     proxy = True

    def __init__(self, data):
        self._data = data

    # def should_remind(self):
    #     pass
