import uuid

from django.db import models


class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    remind_on = models.DateTimeField()
