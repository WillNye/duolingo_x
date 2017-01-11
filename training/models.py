from django.db import models
from django.contrib.auth.models import User

from datetime import datetime as dt


class Language(models.Model):
    name = models.CharField(max_length=250, null=False)
    audio_base = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.name


class Phrase(models.Model):
    english_translation = models.CharField(max_length=750, null=False)
    foreign_translation = models.CharField(max_length=750, null=False)
    language = models.ForeignKey(Language, null=False)
    audio_id = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.english_translation


class PhraseStats(models.Model):
    user = models.ForeignKey(User, null=False)
    phrase = models.ForeignKey(Phrase, null=False)
    is_make_streak = models.BooleanField(default=False, null=False)
    streak_number = models.IntegerField(default=0, null=False)
    last_heard = models.DateTimeField(default=dt.now(), null=False)

    def __str__(self):
        if self.is_make_streak:
            stat_str = "Made {} in a row"
        else:
            stat_str = "Missed {} in a row"
        return stat_str.format(str(self.streak_number))

