
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from apps.pages import views

urlpatterns = [
    url(r'^robots.txt$', serve,{'path': "/webapp/static/robots.txt", 'document_root': settings.BASE_DIR, 'show_indexes': False}),
    url(r'^favicon.ico/$', serve,{'path': "/webapp/static/favicon.ico", 'document_root': settings.BASE_DIR, 'show_indexes': False}),
    url(r'^favicon.ico$', serve,{'path': "/webapp/static/favicon.ico", 'document_root': settings.BASE_DIR, 'show_indexes': False}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR, show_indexes=True)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_DIR, show_indexes=True)

urlpatterns += [
    url(r'^admin/', admin.site.urls),
    url(r'^',       include('pages.urls')),
]

handler404 =  views.handler404
handler500 =  views.handler500
