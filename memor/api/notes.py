from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView

from memor.services.notes import NotesService
from memor.serializers.notes import NoteSerializer
from memor.apps import injector


class NotesAPI(APIView):
    
    def __init__(self):
        self.notes_service = injector.get(NotesService)

    def delete(self, request, note_id, format=None):
        self.notes_service.delete_note_by_id(note_id)
        return HttpResponse(status=204)

    def get(self, request, note_id=None, format=None):
        if note_id:
            note = self.notes_service.get_note_by_id(note_id)
            notes = [note]
        else:
            notes = self.notes_service.get_all_notes()

        serializer = NoteSerializer(notes, many=True)
        return JsonResponse(serializer.data, safe=False)
