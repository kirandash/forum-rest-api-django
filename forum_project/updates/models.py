from django.core.serializers import serialize
# user model to be extracted from django.conf - settings
from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    # serialize entire model
    def serialize(self):
        qs = self
        return serialize('json', qs, fields=('user', 'content', 'image'))


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True,
                              null=True)
    # update should be current time of saving the model
    update = models.DateTimeField(auto_now=True)
    # timestamp should be only once during add (created on date)
    timestamp = models.DateTimeField(auto_now_add=True)

    # get query set in objects
    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    # serialize an instance of model
    def serialize(self):
        return serialize("json", [self], fields=('user', 'content', 'image'))
