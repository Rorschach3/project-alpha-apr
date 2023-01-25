from django.urls import path
from tasks.views import tasks

urlpatterns = [
    path("", tasks, name="tasks"),
]
