from django.contrib import admin
from django.urls import path, include
from TaskApp.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomeView.as_view(), name='index'),
    path('userapp/', include("UserApp.urls")),
    path('taskapp/', include("TaskApp.urls")),
]
