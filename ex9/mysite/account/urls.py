from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='user_register'),

    #url(r'^download/$',views.download_file, {"template_name": "account/download.html"}, name='user_dl'),
    url(r'^download/$',views.download_file, name='user_dl'),

]
