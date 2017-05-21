from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls import include, patterns
from django.views.generic.base import TemplateView
from registration.backends.default.views import (
    ActivationView,
    RegistrationView,
)

from registration.backends.simple.views import RegistrationView
from registration_email.forms import EmailRegistrationForm


urlpatterns = [
    url(r'^$', views.store, name='index'),
    url(r'^book/(\d+)', views.book_details, name='book_details'),
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^checkout/(\w+)', views.checkout, name= 'checkout'),
    url(r'^process/(\w+)', views.process_order, name= 'process_order'),
    url(r'^order_error/', views.order_error, name= 'order_error'),
    url(r'^complete_order/(\w+)', views.complete_order, name= 'complete_order'),

    # django-registration views
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),

    url(r'^activate/(?P<activation_key>\w+)/$',
            ActivationView.as_view(
            template_name='registration/activate.html',
            get_success_url=getattr(
                settings, 'REGISTRATION_EMAIL_ACTIVATE_SUCCESS_URL',
                lambda request, user: '/'),
        ),
        name='registration_activate'),
    url(r'^register/$',
        RegistrationView.as_view(
            form_class=EmailRegistrationForm,
            get_success_url=getattr(
                settings, 'REGISTRATION_EMAIL_REGISTER_SUCCESS_URL',
                lambda request, user: '/'),
        ),
        name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='registration/registration_complete.html'),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='registration/registration_closed.html'),
        name='registration_disallowed'),

    # django auth urls
    url(r'', include('registration_email.auth_urls')),
]
