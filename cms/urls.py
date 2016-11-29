from django.conf.urls import url
from cms import views


urlpatterns = [
    url(r'^paper/$', views.paper_list, name='paper_list'),
    url(r'^paper/add/$', views.paper_edit, name='paper_add'),
    url(r'^paper/mod/(?P<paper_id>\d+)/$', views.paper_edit, name='paper_mod'),
    url(r'^paper/del/(?P<paper_id>\d+)/$', views.paper_del, name='paper_del'),
    url(r'^report/(?P<paper_id>\d+)/$', views.ReportList.as_view(),  name='report_list'),
    url(r'^report/add/(?P<paper_id>\d+)/$', views.report_edit, name='report_add'),
    url(r'^report/mod/(?P<paper_id>\d+)/(?P<report_id>\d+)/$', views.report_edit, name='report_mod'),
    url(r'^report/del/(?P<paper_id>\d+)/(?P<report_id>\d+)/$', views.report_del, name='report_del'),
    url(r'^admin_message/$', views.admin_message, name='admin_message')
]
