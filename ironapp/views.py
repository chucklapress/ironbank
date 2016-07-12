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


def is_balance():
    transactions = AcctBalance.objects.all()
    balance = 0
    for items in transactions:
        if item.is_deposit == True:
            balance += entry
        else:
            #is_deposit == False
            balance -= entry
            return balance()


from django.contrib.auth.mixins import LoginRequiredMixin
class AccountView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "acctbalance_form.html"
    model = AcctBalance
    def get_queryset(self):
        return AcctBalance.objects.filter(customer=self.request.user)

class OpenAcctView(CreateView):
    model = AcctBalance
    template_name = "open_account.html"
    fields = ["entry", "is_deposit","date","memo_or_note","account_number"]
    success_url = '/'
    def form_valid(self, form):
        accttrans =form.save(commit=False)
        accttrans.customer = self.request.user
        return super().form_valid(form)


class AccountDetailView(DetailView):
    model = AcctBalance
    template = "acctbalance_detail.html"
