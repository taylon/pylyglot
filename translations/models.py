from django.db import models
from bidu.languages.models import Language
from bidu.packages.models import Package

class Translation(models.Model):

    msgstr = models.TextField()
    revisiondate = models.DateTimeField(blank=True, null=True)
    translated = models.BooleanField()
    standardized = models.BooleanField(default=False)

    language = models.ForeignKey(Language)
    package = models.ForeignKey(Package, blank=True, null=True)

    def __unicode_(self):
        return self.msgstr.encode("utf-8")
