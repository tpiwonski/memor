import uuid

from django.db import models
from memor.models import reminders


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField()
    text = models.CharField(max_length=4000)
    reminders = models.ManyToManyField(reminders.Reminder, through='NoteReminder')


class NoteReminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    reminder = models.ForeignKey(reminders.Reminder, on_delete=models.CASCADE)
