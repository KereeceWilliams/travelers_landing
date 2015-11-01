from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
                      url(r'^$', Home.as_view(), name='home'),
                       url(r'^question/create/$', QuestionCreateView.as_view(), name='question_create'),
                       url(r'^success/$', Success.as_view(), name='success'),
                       url(r'^video/create/$', VideoCreateView.as_view(), name='video_create'),
                        url(r'^survey/create/$', SurveyCreateView.as_view(), name='survey_create'),
                       )