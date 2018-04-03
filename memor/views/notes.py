import json

from django.views.generic.edit import CreateView
from django.views.generic import ListView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse
from django.utils import timezone
from django.db import transaction

from memor.apps import injector

from memor.models.notes import Note, NoteReminder
from memor.forms.notes import NoteForm
from memor.services.notes import NotesService
from memor.serializers.notes import NoteSerializer

from memor.models.reminders import Reminder

from memor.interactors.notes import AddNoteInteractor, ShowNotesInteractor, AddNoteReminderInteractor
from memor.repositories.notes import AddNoteRepository, ShowNotesRepository, AddNoteReminderRepository
from memor.presenters.notes import AddNotePresenter, ShowNotesPresenter, AddNoteReminderPresenter
from memor.factories.notes import NotesFactory

class AddNoteView(FormView):
    template_name = 'notes/add.html'
    success_url = reverse_lazy('list_notes')
    form_class = NoteForm

    # def __init__(self):
        # self.notes_service = injector.get(NotesService)

    def form_valid(self, form):        
        factory = NotesFactory()
        repository = AddNoteRepository()
        presenter = AddNotePresenter()
        interactor = AddNoteInteractor(factory, repository, presenter)
        interactor.execute(note_text=form.cleaned_data['text'])
        note_id = interactor.note_id

        repository = AddNoteReminderRepository()
        # presenter = AddNoteReminderPresenter()
        interactor = AddNoteReminderInteractor(factory, repository, None)
        interactor.execute(note_id=note_id, note_remind_on=form.cleaned_data['remind_on'])

        return presenter.get_response()

        # note = self.notes_service.create_note(text=form.cleaned_data['text'])
        #self.notes_service.add_note_reminder(note.id, remind_on=timezone.now())
        # AddNoteWithReminderSomething(note_text=form.cleaned_data['text'], remind_on=timezone.now()).execute()
        # return super().form_valid(form)


class NotesView(TemplateView):
    template_name = 'notes/list.html'
    
    # def __init__(self):
        # self.notes_service = injector.get(NotesService)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        repository = ShowNotesRepository()
        presenter = ShowNotesPresenter()
        interactor = ShowNotesInteractor(repository, presenter)
        interactor.execute()
        context.update(presenter.get_context())
        return context

        # context['state'] = {}
        # notes = self.notes_service.get_all_notes()
        # serializer = NoteSerializer(notes, many=True)
        # context['state']['state-notes'] = json.dumps(serializer.data)
        # return context


class AddNoteWithReminderSomething(object):

    def __init__(self, note_text, remind_on):
        self.note_text = note_text
        self.remind_on = remind_on
    
    @transaction.atomic
    def execute(self):
        note = Note(text=self.note_text, added_on=timezone.now())
        #note.save()
        reminder = Reminder(remind_on=self.remind_on)
        #reminder.save()
        #raise Exception('boom')
        #note.notereminder_set.create(reminder=reminder)
        # note.reminders.add(reminder)
        note_reminder = NoteReminder(note=note, reminder=reminder)
        note.save();
        reminder.save()
        note_reminder.save()

