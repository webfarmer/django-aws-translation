from django.conf.urls import url
from pages import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),

    url(r'^admin/translate/$', views.AdminTranslateView, name="translate_page"),

    url(r'^400/$', views.FailView, kwargs={"slug": "400"}, name="server_400"),
    url(r'^403/$', views.FailView, kwargs={"slug": "403"}, name="server_403"),
    url(r'^404/$', views.FailView, kwargs={"slug": "404"}, name="server_404"),
    url(r'^500/$', views.FailView, kwargs={"slug": "500"}, name="server_500"),

    url(r'^(?P<slug>[a-zA-Z0-9_.-]+)/$', views.PageView.as_view(), name="page"),
]