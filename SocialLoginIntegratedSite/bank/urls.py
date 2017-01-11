from django.conf.urls import patterns, url
from bank import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^loggedin/$', views.loggedin, name='loggedin'),
        url(r'^transaction_history/$', views.transaction_history, name='transaction_history'),
        url(r'^add_customer/$', views.add_customer, name='add_customer'),
        url(r'^new_transaction/$', views.new_transaction, name='new_transaction'),)

