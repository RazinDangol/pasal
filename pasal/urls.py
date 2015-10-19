"""pasal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/h/tp/ur/s/
Ex/mples:/
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', 'products.views.show',name='products'),
    url(r'^category/','products.views.category',name='category'),
    url(r'^customer/','products.views.customer',name='customer'),
    url(r'^sales/','products.views.sales',name='sales'),
    url(r'^product/(?P<id>[0-9]+)/$','products.views.product_id',name='product-{}'.format(id)),
    url(r'^signup/$','products.views.signup',name='signup'),
    url(r'^login/$','products.views.login',name='login'),
    url(r'^login/success/','products.views.login_success',name='login_success'),
    url(r'^login/invalid/','products.views.login_invalid',name='login_invalid'),
    url(r'^login/disabled/','products.views.login_disabled',name='login_disabled'),
    url(r'^signup/success/','products.views.signup_success',name='signup_success'),

        ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)