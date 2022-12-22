from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Publication

# Create your views here.


def home(request):
    context = {"publications": Publication.objects.all(), "title": "Publications Index"}
    return render(request, "publications/home.html", context)


class PublicationListView(ListView):
    model = Publication
    template_name = "publications/home.html"
    context_object_name = "publications"
    ordering = ["date_posted"]


class UserPublicationListView(ListView):
    model = Publication
    template_name = "publications/user_publications.html"
    context_object_name = "publications"
    ordering = ["date_posted"]

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Publication.objects.filter(user=user).order_by("-date_posted")


class PublicationDetailView(DetailView):
    model = Publication


class PublicationCreateView(LoginRequiredMixin, CreateView):
    model = Publication
    fields = ["title","first_author_first_name","first_author_last_name","author_list", "abstract", "references", "laboratory", "journal_name", "journal_volume","published_date"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
    fields = ["title","first_author_first_name","first_author_last_name","author_list", "abstract", "references", "laboratory", "journal_name", "journal_volume","published_date"]


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # prevents users from updating anyone else's publication. UserPassesTestMixin
    def test_func(self):
        publication = self.get_object()
        if self.request.user == publication.user:
            return True
        return False


class PublicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publication
    success_url = "/"

    def test_func(self):
        publication = self.get_object()
        if self.request.user == publication.user:
            return True
        return False


def about(request):
    return render(request, "publications/about.html", {"title": "Publications Index"})
