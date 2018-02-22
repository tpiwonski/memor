from django.urls import path
from django.conf.urls import url, include

# from rest_framework.routers import DefaultRouter

from memor.views.notes import NotesView, AddNoteView
from memor.views.main import HomeView
from memor.api.notes import NotesAPI

# router = DefaultRouter()
# router.register(r'notes', NotesAPI)

urlpatterns = [    
    path('', HomeView.as_view(), name='home'),
    path('notes', NotesView.as_view(), name='list_notes'),
    path('notes/add', AddNoteView.as_view(), name='add_note'),
    url(r'api/notes/(?P<note_id>[0-9]+){0,1}', NotesAPI.as_view(), name="api_notes")
    # url(r'^api', include(router.urls))
]
