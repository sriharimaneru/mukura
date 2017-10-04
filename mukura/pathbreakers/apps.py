#fom __future__ import unicode_literals

from django.apps import AppConfig
import algoliasearch_django as algoliasearch
from index import PathbreakerIndex

class PathbreakersConfig(AppConfig):
    name = 'pathbreakers'

    def ready(self):
      pathbreakermodel = self.get_model('Pathbreaker')
      algoliasearch.register(pathbreakermodel, PathbreakerIndex);
