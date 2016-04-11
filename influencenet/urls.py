from django.conf.urls import include, url
from influencenet import views

urlpatterns = [
    url(r'^$', views.BuildNetworkView.as_view()),
    ]
