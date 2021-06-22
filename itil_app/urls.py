from .users.views import CreateUser
from knox import views as knox_views
from django.urls import path, include


urlpatterns = [
	path('login', include('knox.urls')),
	path('signup', CreateUser.as_view()),
]