from django.conf.urls import patterns, url
from expense import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^all_transactions/$', views.transactions, name='all transactions'),
        url(r'^add_transaction/$', views.add_transaction, name='add_transaction'),
        url(r'^add_category/$', views.add_category, name='add_category'),)