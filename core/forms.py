# vim: ts=4 sw=4 expandtab ai
# -*- encoding: utf-8 -*-

from django import forms
from pylyglot.languages.models import Language

class SearchForm(forms.Form):

    available_languages = Language.objects.all().values_list('id', 'short_name').order_by('short_name')

    languages = forms.ChoiceField(choices = available_languages)
    query = forms.CharField()

class PackageSearchForm(forms.Form):

    query = forms.CharField()
