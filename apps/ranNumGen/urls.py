from django.conf.urls import url 
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'random_word$', views.ran_gen),
  url(r'reset$', views.reset)
]
