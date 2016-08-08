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


def is_balance(user):
    transactions = AcctBalance.objects.filter(customer=user)
    balance = 0
    for items in transactions:
        if items.is_deposit == True:
            balance += items.entry
        elif items.is_deposit == False:
            balance -= items.entry
        elif items.is_transfer == True:
            balance -= items.entry
            if balance >0:
                print("This transaction is not supported")

    return balance


from django.contrib.auth.mixins import LoginRequiredMixin
class AccountView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "acctbalance_form.html"
    model = AcctBalance
    def get_queryset(self):
        return AcctBalance.objects.filter(customer=self.request.user)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        self.is_balance = is_balance(self.request.user)
        context["balance"] = self.is_balance
        return context



class OpenAcctView(CreateView):
    model = AcctBalance
    template_name = "open_account.html"
    fields = ["entry", "is_deposit","date","memo_or_note","account_number","is_transfer"]
    success_url = '/'
    def form_valid(self, form):

        accttrans = form.save(commit=False)
        accttrans.customer = self.request.user
        credit = accttrans.is_deposit == True
        if accttrans.entry > is_balance(self.request.user) and not accttrans.is_deposit:
            form.add_error("entry", "overdraft not allowed")
            return super().form_invalid(form)
        return super().form_valid(form)





class AccountDetailView(DetailView):
    model = AcctBalance
    template = "acctbalance_detail.html"
