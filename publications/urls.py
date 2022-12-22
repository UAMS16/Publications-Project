from django.urls import path
from .views import (
    PublicationListView,
    PublicationDetailView,
    PublicationCreateView,
    PublicationUpdateView,
    PublicationDeleteView,
    UserPublicationListView,
)
from . import views

urlpatterns = [
    path("", PublicationListView.as_view(), name="publications-home"),
    path(
        "user/<str:username>",
        UserPublicationListView.as_view(),
        name="user-publications",
    ),
    path(
        "publication/<int:pk>",
        PublicationDetailView.as_view(),
        name="publication-detail",
    ),
    path(
        "publication/new",
        PublicationCreateView.as_view(),
        name="publication-create",
    ),
    path(
        "publication/<int:pk>/update/",
        PublicationUpdateView.as_view(),
        name="publication-update",
    ),
    path(
        "publication/<int:pk>/delete/",
        PublicationDeleteView.as_view(),
        name="publication-delete",
    ),
    path("about", views.about, name="publications-about"),
]
