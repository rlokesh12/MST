from django.contrib.auth.models import User
from tastypie.resources import ModelResource,ALL_WITH_RELATIONS
from tastypie import fields
from .models import *


class CricketResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class BadmintonResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class BasketBallResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class FootballResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class TennisResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class ChessResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class GymResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class TableTennisResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }
class KabaddiResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }
class VolleyballResource(ModelResource):
    class Meta:
        queryset = Cricket.objects.all()
        filtering = {
            'college': ALL_WITH_RELATIONS,
        }


class MemberResource(ModelResource):
    cri = fields.ForeignKey(CricketResource, 'cri')
    bad = fields.ForeignKey(BadmintonResource, 'bad')
    tab = fields.ForeignKey(TableTennisResource, 'tab')
    ten = fields.ForeignKey(TennisResource, 'ten')
    foo = fields.ForeignKey(FootballResource, 'foo')
    kab = fields.ForeignKey(KabaddiResource, 'kab')
    che = fields.ForeignKey(ChessResource, 'che')
    gym = fields.ForeignKey(GymResource, 'gym')
    vol = fields.ForeignKey(VolleyballResource, 'vol')
    bas = fields.ForeignKey(BasketBallResource, 'bas')
    class Meta:
        queryset = Member.objects.all()
        filtering = {
            'name': ALL_WITH_RELATIONS,
            'id': ALL_WITH_RELATIONS,
            'college': ALL_WITH_RELATIONS,
            'city': ALL_WITH_RELATIONS,
            'cri': ALL_WITH_RELATIONS,
            'bad': ALL_WITH_RELATIONS,
            'tab': ALL_WITH_RELATIONS,
            'ten': ALL_WITH_RELATIONS,
            'bas': ALL_WITH_RELATIONS,
            'vol': ALL_WITH_RELATIONS,
            'che': ALL_WITH_RELATIONS,
            'gym': ALL_WITH_RELATIONS,
            'kab': ALL_WITH_RELATIONS,
            'foo': ALL_WITH_RELATIONS,
        }


