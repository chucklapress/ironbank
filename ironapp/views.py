from urllib import request

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View

from ironapp.models import AcctBalance

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class IndexView(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"

from django.contrib.auth.mixins import LoginRequiredMixin
class AccountView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "acctbalance_form.html"
    model = AcctBalance
    def get_queryset(self):
        return AcctBalance.objects.filter(customer=self.request.user)



class BalanceView(DetailView):
    template_name = "balance_view.html"
    model = AcctBalance
    def get_queryset(self):
        return AcctBalance.objects.filter(customer=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account"] = "account"
        return context



class OpenAcctView(CreateView):
    model = AcctBalance
    template_name = "open_account.html"
    fields = ["entry", "is_deposit","date","name","customer"]
    success_url = '/'


class AccountDetailView(DetailView):
    model = AcctBalance
