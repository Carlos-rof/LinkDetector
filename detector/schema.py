import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from .models import URL


class URLType(DjangoObjectType):
    class Meta:
        model = URL


class Query(graphene.ObjectType):
    urls = graphene.List(URLType, url=graphene.String(), id_dominio=graphene.String(), track=graphene.Int())

    def resolve_urls(self, info, url=None, id_dominio=None, track=None, **kwargs):
        queryset = URL.objects.all()

        if url:
            _filter = Q(full_url__icontains=url)
            queryset = queryset.filter(_filter)

        if id_dominio and track:
            _filter = Q(id_dominio__icontains=id_dominio, track__icontains=track)
            queryset = queryset.filter(_filter)

        return queryset


class CreateURL(graphene.Mutation):
    url = graphene.Field(URLType)

    class Arguments:
        full_url = graphene.String()
        id_dominio = graphene.String()
        track = graphene.String()

    def mutate(self, info, full_url, id_dominio, track):
        url = URL(full_url=full_url, id_dominio=id_dominio, track=track)
        url.save()

        return CreateURL(url=url)


class Mutation(graphene.ObjectType):
    create_url = CreateURL.Field()
