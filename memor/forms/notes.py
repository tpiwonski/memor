from django.forms import Form, CharField, DateTimeField

# from memor.models.notes import Note

class NoteForm(Form):
    text = CharField(label='Text:', max_length=255)
    remind_on = DateTimeField(label='Reminder:')

    # class Meta:
    #     model = Note
    #     fields = ['text']
