import json

from django.views.generic.edit import CreateView
from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse

from memor.apps import injector

from memor.models.notes import Note, NoteReminder
from memor.forms.notes import NoteForm
from memor.services.notes import NotesService
from memor.serializers.notes import NoteSerializer


class AddNoteView(FormView):
    template_name = 'notes/add.html'
    success_url = reverse_lazy('list_notes')
    form_class = NoteForm

    def __init__(self):
        self.notes_service = injector.get(NotesService)

    def form_valid(self, form):
        self.notes_service.create_note(text=form.cleaned_data['text'])
        return super().form_valid(form)


class NotesView(TemplateView):
    template_name = 'notes/list.html'
    
    def __init__(self):
        self.notes_service = injector.get(NotesService)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = {}

        notes = self.notes_service.get_all_notes()
        serializer = NoteSerializer(notes, many=True)
        context['state']['state-notes'] = json.dumps(serializer.data)
        return context
