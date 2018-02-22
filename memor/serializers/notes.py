from rest_framework.serializers import ModelSerializer

from memor.models.notes import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'text', 'added_on')
