from knox import views as knox_views
from django.urls import path, include
from .users.views import CreateUser, Login


urlpatterns = [
	path('login', Login.as_view()),
	path('signup', CreateUser.as_view()),
	path('logout', knox_views.LogoutView.as_view()),
]