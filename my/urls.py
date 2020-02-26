from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hood/(?P<id>\d+)/', views.hood, name='hood'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^update/$', views.update_profile, name='update'),
    url(r'^post/(?P<id>\d+)', views.add_post, name='new_post')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
