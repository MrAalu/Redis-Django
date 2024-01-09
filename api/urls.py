from django.urls import path
from api.views import Custom_View

urlpatterns = [path("", Custom_View.as_view())]
