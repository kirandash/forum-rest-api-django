from django.contrib import admin

from .forms import StatusForm
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    # fields to show on admin
    list_display = ['user', '__str__', 'image']

    # overwrite the default Django Form to use
    form = StatusForm

    # Not required, since the admin uses Status model by default
    # class Meta:
    #     model = Status


admin.site.register(Status, StatusAdmin)
