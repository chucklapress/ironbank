from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView

from ironapp.models import AcctBalance


class IndexView(TemplateView):
    template_name = 'index.html'

class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

class AccountView(ListView):
    template_name = "acctbalance_form.html"
    model = AcctBalance


class ItemView(DetailView):
    model = AcctBalance

    def get_queryset(self):
        return AcctBalance.objects.filter(customer=self.request.user)









