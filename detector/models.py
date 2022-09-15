from hashlib import md5
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from graphql import GraphQLError


class URL(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    id_dominio = models.CharField(max_length=8, default='')
    track = models.IntegerField(unique=True, default=0)

    def clicked(self):
        self.clicks += 1
        print(self.clicks)
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        validate = URLValidator()
        try:
            validate(self.full_url)
        except ValidationError as e:
            raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)
