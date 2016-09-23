from django.conf.urls import patterns, url, include

from testapp import views

urlpatterns = patterns(

        # code test
        url(r'summaryData/', views.summary_data, name='view_data'),
)
