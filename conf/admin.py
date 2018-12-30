from django.contrib import admin
from .models import conference_form

# Register your models here.
class ConfAdmin(admin.ModelAdmin):
    list_display = ['conference_name','conference_start','conference_end']
    class Meta:
        model=conference_form

admin.site.register(conference_form, ConfAdmin)