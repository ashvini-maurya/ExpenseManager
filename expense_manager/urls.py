from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from expense import views

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/expense/'


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expense_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^expense/', include('expense.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)