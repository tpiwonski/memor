import json
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse

from memor.serializers.notes import NoteSerializer

class AddNotePresenter(object):
    
    def __init__(self):
        self.response = None
    
    def present_note(self, **response):
        self.response = redirect('list_notes')

    def get_response(self):
        return self.response


class ShowNotesPresenter(object):

    def __init__(self):
        self.response = None

    def present_notes(self, notes):
        self.response = notes

    def get_context(self):
        serializer = NoteSerializer(self.response, many=True)
        state = json.dumps(serializer.data)
        context = {
            'state': {
                'state-notes': state
            }
        }
        return context


class AddNoteReminderPresenter(object):
    pass


class GetNotesPresenter(object):

    def __init__(self):
        self.response = None

    def present_notes(self, notes):
        self.response = notes

    def get_response(self):
        serializer = NoteSerializer(self.response, many=True)
        return JsonResponse(serializer.data, safe=False)
