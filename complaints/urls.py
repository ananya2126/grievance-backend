from django.urls import path
from .views import (
    CreateComplaintView,
    ListComplaintsView,
    ResolveComplaintView,
)

urlpatterns = [
    path("create/", CreateComplaintView.as_view()),
    path("", ListComplaintsView.as_view()),
    path("resolve/<int:pk>/", ResolveComplaintView.as_view()),
]