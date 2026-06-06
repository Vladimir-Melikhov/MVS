from django.urls import path
from django.views.generic import TemplateView
from .views import MainListView, contact_send

urlpatterns = [
    path("", MainListView.as_view(), name="main"),
    path("legal/", TemplateView.as_view(template_name="main/legal.html"), name="legal"),
    path("contact/send/", contact_send, name="contact_send"),
]
