from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexPageList


urlpatterns = [
    url(r'^', include('allauth.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('user_profile.urls')),
    #url(r'^activity/', include('actstream.urls')),

    url(r'^$', IndexPageList.as_view(), name='index'),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
