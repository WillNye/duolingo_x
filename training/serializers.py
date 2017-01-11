from rest_framework import serializers

from .models import Language, Phrase, PhraseStats


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class PhraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = '__all__'


class PhraseStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhraseStats
        fields = '__all__'

