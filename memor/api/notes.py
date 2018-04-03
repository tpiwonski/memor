from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView

from memor.services.notes import NotesService
from memor.serializers.notes import NoteSerializer
from memor.apps import injector

from memor.interactors.notes import DeleteNoteInteractor, ShowNotesInteractor
from memor.repositories.notes import DeleteNoteRepository, ShowNotesRepository
from memor.presenters.notes import GetNotesPresenter

class NotesAPI(APIView):
    
    def __init__(self):
        self.notes_service = injector.get(NotesService)

    def delete(self, request, note_id, format=None):
        # self.notes_service.delete_note_by_id(note_id)

        repository = DeleteNoteRepository()
        interactor = DeleteNoteInteractor(repository, None)
        interactor.execute(note_id=note_id)

        return HttpResponse(status=204)

    def get(self, request, note_id=None, format=None):
        if note_id:
            note = self.notes_service.get_note_by_id(note_id)
            notes = [note]
            serializer = NoteSerializer(notes, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            repository = ShowNotesRepository()
            presenter = GetNotesPresenter()
            interactor = ShowNotesInteractor(repository, presenter)
            interactor.execute()
            return presenter.get_response()
