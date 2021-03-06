from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers

from core.views import StudentViewSet, UniversityViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities',  UniversityViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
