from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from authentication.forms import CustomUserCreationForm
from .models import AuthUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class AuthUserDetailView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AuthUser

    fields = [
        'username',
        'avatar',
        'first_name',
        'last_name',
        'email',
        'phone_number'
    ]
    template_name = "authentication/profile/update.html"

    def test_func(self):
        obj = self.get_object()
        return obj.id == self.request.user.id


class SignupPageView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'authentication/profile/signup.html'
    form_class = CustomUserCreationForm

class HomePageView(TemplateView):
    template_name = "authentication/home.html"
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context     

class UserDetailPage(LoginRequiredMixin, DetailView):
    model = AuthUser
    context_object_name = "profile"
    template_name = "authentication/profile/detail.html"
    login_url = "login"             