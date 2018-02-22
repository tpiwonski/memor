from django.forms import ModelForm

from memor.models.notes import Note

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['text']

