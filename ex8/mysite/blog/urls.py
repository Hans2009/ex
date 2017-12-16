from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^content$',views.blog_article,name="blog_article"),
]
