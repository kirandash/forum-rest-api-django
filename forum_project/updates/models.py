# user model to be extracted from django.conf - settings
from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


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

    def __str__(self):
        return self.content or ""
