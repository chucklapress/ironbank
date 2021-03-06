"""iron_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout


from ironapp.views import IndexView, SignUpView, AccountView, OpenAcctView, AccountDetailView

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^signup/', SignUpView.as_view(), name="sign_up_view"),
    url(r'^balance/$', AccountView.as_view(), name="acct_bal_view"),
    url(r'^openacct/',OpenAcctView.as_view(), name="open_acct_view"),
    url(r'^balance/(?P<pk>\d+)/$', AccountDetailView.as_view(), name="account_detail_view"),

)
