from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sentiment/$', views.sentiment, name='sentiment'),
			   ]
