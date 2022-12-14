from django.db.models import CharField, Manager, OuterRef, Subquery, Value
from django_action_reservation.managers import TargetQuerySet

from django_popularity.conf import settings


@classmethod
def objects_with_popularity(
    cls,
    geo=settings.POPULARITY_DEFAULT_GEO,
):
    from django_popularity.models import Popularity

    pops = Popularity.objects.get_queryset().filter(mid=OuterRef('mid'), geo=geo)
    return cls.objects \
               .annotate(geo=Value(geo, CharField(max_length=10))) \
               .annotate(score1080=Subquery(pops.values('score1080')[:1])) \
               .annotate(score360=Subquery(pops.values('score360')[:1])) \
               .annotate(score180=Subquery(pops.values('score180')[:1])) \
               .annotate(score90=Subquery(pops.values('score90')[:1])) \
               .annotate(score30=Subquery(pops.values('score30')[:1])) \
               .annotate(title=Subquery(pops.values('title')[:1]))


@classmethod
def objects_with_mid_info(cls):
    from django_popularity.models import SuggestionResult

    sugs = SuggestionResult.objects.filter(mid=OuterRef('mid'))
    return cls.objects \
              .annotate(type=Subquery(sugs.values('type'))) \
              .annotate(title=Subquery(sugs.values('title')))


@property
def popularities(self):
    from django_popularity.models import Popularity

    return Popularity.objects.filter(mid=self.mid)


class PopularityManager(Manager.from_queryset(TargetQuerySet)):
    def get_queryset(self):
        from django_popularity.models import GeoStandard

        active_geo_list = GeoStandard.objects.filter(is_active=True).values('geo')
        return super().get_queryset().filter(geo__in=active_geo_list)
