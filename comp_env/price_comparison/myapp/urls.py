from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
url(r'^$',views.enterprod,name='enterprod'),
url(r'^createtable',views.createtable,name='createtable'),
]