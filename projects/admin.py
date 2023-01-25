from django.contrib import admin
from projects.models import Project
from tasks.models import Task


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
