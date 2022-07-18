from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customers',views.CustomerView)
router.register('books',views.BookView)
router.register('loans',views.LoanView)

urlpatterns = [
    path('',include(router.urls))
]