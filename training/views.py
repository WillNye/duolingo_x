# -*- coding: utf-8 -*-

from rest_framework import viewsets

from .serializers import LanguageSerializer, PhraseSerializer, PhraseStatsSerializer

from .models import Language, Phrase, PhraseStats


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class PhraseViewSet(viewsets.ModelViewSet):
    serializer_class = PhraseSerializer
    queryset = Phrase.objects.all()


class PhraseStatsViewSet(viewsets.ModelViewSet):
    serializer_class = PhraseStatsSerializer
    queryset = PhraseStats.objects.all()




