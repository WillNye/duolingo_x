from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from training.views import LanguageViewSet, PhraseViewSet, PhraseStatsViewSet

router = DefaultRouter()
router.register(r'languages', LanguageViewSet)
router.register(r'phrases', PhraseViewSet)
router.register(r'stats', PhraseStatsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-v1/', include(router.urls, namespace='api'))
]
