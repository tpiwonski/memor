from django.apps import AppConfig
from injector import Injector

from memor.bindings import Bindings

injector = None

class MemorConfig(AppConfig):
    name = 'memor'

    def ready(self):
        global injector
        injector = Injector([Bindings])
