from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from library.models import  BookThatWillBeShared


class ShareableBooksView(ListView):
    model = BookThatWillBeShared
    template_name = "book_share/list.html"

class DetailShareableBookView(DetailView):
    model = BookThatWillBeShared
    template_name = "book_share/detail.html"


class UpdateShareableBookView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BookThatWillBeShared
    fields = [
        'book_id',
        'shared'
    ]
    template_name = "book_share/update.html"
    
    success_url = reverse_lazy("shareable_books")
    
    def test_func(self):
        obj = self.get_object()
        return obj.user_id == self.request.user


    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)



class ShareBookView(LoginRequiredMixin, CreateView):
    model = BookThatWillBeShared
    fields = [
        'book_id'
    ]
    template_name = "book_share/create.html"
    
    success_url = reverse_lazy("shareable_books")
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)



    