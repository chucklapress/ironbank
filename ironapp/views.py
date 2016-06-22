from urllib import request

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView

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


class OpenAcctView(CreateView):
    model = AcctBalance
    template_name = "open_account.html"

