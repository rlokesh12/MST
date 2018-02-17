from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from .views import *
from .api import *

v1_api = Api(api_name='v1')
v1_api.register(MemberResource())
v1_api.register(CricketResource())
v1_api.register(BadmintonResource())
v1_api.register(BasketBallResource())
v1_api.register(TableTennisResource())
v1_api.register(TennisResource())
v1_api.register(GymResource())
v1_api.register(KabaddiResource())
v1_api.register(FootballResource())
v1_api.register(ChessResource())
v1_api.register(VolleyballResource())

urlpatterns = [
    url(r'^$', home_page),
    url(r'^register/$',register_page),
    # url(r'^gallery/$',gallery_page),
    url(r'^team/$',team_page),
    url(r'^about/$',about_page),
    url(r'^informals/$',informals_page),
    url(r'^schedule/$',schedule_page),
    url(r'^thankyou/$', tq_page),
    url(r'^failure/$', fail_page),
    url(r'^api/', include(v1_api.urls)),
    ]
