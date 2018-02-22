from injector import Module, singleton
from functools import update_wrapper

class Bindings(Module):

    def configure(self, binder):
        from memor.repositories.notes import NotesRepository
        from memor.services.notes import NotesService

        binder.bind(NotesRepository, scope=singleton)
        binder.bind(NotesService, scope=singleton)
