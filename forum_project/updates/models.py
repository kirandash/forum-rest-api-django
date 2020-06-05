import json
from django.core.serializers import serialize
# user model to be extracted from django.conf - settings
from django.conf import settings
from django.db import models


def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    # serialize entire model - list view
    # def serialize(self):
    #     qs = self
    #     return serialize('json', qs, fields=('user', 'content', 'image'))

    # serialize entire model - list view
    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     count = 0
    #     for obj in qs:
    #         stuct = json.loads(obj.serialize())
    #         final_array.append(stuct)
    #     return json.dumps(final_array)
    #     # return serialize('json', qs, fields=('user', 'content', 'image'))

    # serialize entire model - list view
    def serialize(self):
        # dot values method - self.values
        list_values = list(self.values("user", "content", "image"))
        print(list_values)
        return json.dumps(list_values)


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

    # serialize an instance of model - for detail view
    # def serialize(self):
    #     json_data = serialize("json", [self],
    #                           fields=('user', 'content', 'image'))
    #     # convert JSON data into python usable code ie. [{}] (structure)
    #     # [{}] a list of a dictionary
    #     stuct = json.loads(json_data)
    #     print(stuct)
    #     # removes model, pk and returns everything under the fields
    #     data = json.dumps(stuct[0]['fields'])
    #     return data

    # serialize an instance of model - for detail view - with mapping
    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""

        data = {
            "content": self.content,
            "user": self.user.id,
            "image": image
        }
        data = json.dumps(data)
        return data
