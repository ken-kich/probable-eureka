from django.contrib import admin
from django.urls import path, include
from TaskApp.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),
    path('userapp/', include('UserApp.urls', namespace='UserApp')),
    path('taskapp/', include('TaskApp.urls', namespace='TaskApp')),
]
