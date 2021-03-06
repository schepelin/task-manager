# coding: utf-8

from django.conf.urls import patterns, url

from tasks.views import TaskCreate, TaskList, TaskEdit, TaskDetail


urlpatterns = patterns(
    '',
    url('^$', TaskList.as_view(), name='task_list'),
    url(r'^new$', TaskCreate.as_view(), name='task_new'),
    url(r'^(?P<pk>\d+)/edit$', TaskEdit.as_view(), name='task_edit'),
    url(r'^(?P<pk>\d+)$', TaskDetail.as_view(), name='task_detail'),
)
