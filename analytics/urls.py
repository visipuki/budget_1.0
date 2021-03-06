from django.conf.urls import patterns, url
from analytics import views


urlpatterns = [
    url(r'^$', views.analyticsView),
    url(r'^(\d{2}-\d{2}-\d{4})_(\d{2}-\d{2}-\d{4})/$', views.analyticsView),
    url(
        r'^'+r'(?:(owner_id|incomeType_id|date__gte|date__lte|spendingType_id)/(.+?)/)?'*5+r'$',
        views.analyticsView
    ),
]
