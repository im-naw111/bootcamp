from django.conf.urls import url

from bootcamp.search import views

app_name = 'search'
urlpatterns = [
    url(r'^$', views.SearchListView.as_view(), name='results'),
]
