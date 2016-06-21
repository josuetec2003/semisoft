from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from marcadores.views import index, agregar_marcador, guardar_marcador

#localhost/static/bootstrap/css/bootstrap.css = url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^agregar-marcador/$', agregar_marcador, name='agregar_marcador'),
    url(r'^guardar-marcador/$', guardar_marcador, name='guardar_marcador'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
