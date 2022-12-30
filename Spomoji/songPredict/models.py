from django.db import models


class AudioStored(models.Model):
    song = models.FileField(upload_to='documents/')

    class Meta:
        db_table = 'AudioStored'