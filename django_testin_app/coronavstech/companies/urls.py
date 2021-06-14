from rest_framework import routers
from django_testin_app.coronavstech.companies.views import CompanyViewSet

companies_router = routers.DefaultRouter()
companies_router.register(
                         "companies",
                         viewset=CompanyViewSet, basename="companies"
                         )
urlpatterns = companies_router.urls


