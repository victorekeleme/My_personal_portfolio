from django.urls import path
from portfolioApp.views import ProfileListView

urlpatterns = [
    path('', ProfileListView.as_view(), name = 'porfolio'),
]
