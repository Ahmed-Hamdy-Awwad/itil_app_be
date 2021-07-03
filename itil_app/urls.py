from rest_framework import routers
from .asset.views import AssetView
from knox import views as knox_views
from .ticket.views import TicketView
from django.urls import path, include
from .supplier.views import SupplierView
from .request_type.views import RequestTypeView
from .users.views import CreateUser, Login, UserView


router = routers.DefaultRouter()
router.register('user', UserView, 'user')
router.register('asset', AssetView, 'asset')
router.register('ticket', TicketView, 'ticket')
router.register('supplier', SupplierView, 'supplier')
router.register('requestype', RequestTypeView, 'requestype')

urlpatterns = [
	path('', include(router.urls)),
	path('login', Login.as_view()),
	path('signup', CreateUser.as_view()),
	path('logout', knox_views.LogoutView.as_view()),
]