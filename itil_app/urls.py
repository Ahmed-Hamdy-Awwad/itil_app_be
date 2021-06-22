from rest_framework import routers
from knox import views as knox_views
from .ticket.views import TicketView
from django.urls import path, include
from .users.views import CreateUser, Login


router = routers.DefaultRouter()
router.register('ticket', TicketView, 'ticket')

urlpatterns = [
	path('', include(router.urls)),
	path('login', Login.as_view()),
	path('signup', CreateUser.as_view()),
	path('logout', knox_views.LogoutView.as_view()),
]