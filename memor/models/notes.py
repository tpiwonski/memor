from django.db import models
from memor.models import reminders


class Note(models.Model):
    added_on = models.DateTimeField()
    text = models.CharField(max_length=4000)


class NoteReminder(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    reminder = models.ForeignKey(reminders.Reminder, on_delete=models.CASCADE)
