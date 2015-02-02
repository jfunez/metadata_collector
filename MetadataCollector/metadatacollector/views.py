from pyramid.view import view_config
from pyramid.response import Response
import json


@view_config(route_name='index', request_method='GET')
def index(request):
    return Response('MetadataCollector API')


@view_config(route_name='collection_documents', request_method='GET')
def collection_documents(request):
    collection_acronym = request.matchdict['collection_acronym']
    result = {
        'collection_acronym': collection_acronym,
    }
    return Response(json.dumps(result), content_type="application/json")


@view_config(route_name='journal_documents', request_method='GET')
def journal_documents(request):
    journal_issn = request.matchdict['journal_issn']
    result = {
        'journal_issn': journal_issn,
    }
    return Response(json.dumps(result), content_type="application/json")


@view_config(route_name='collection_citations', request_method='GET')
def collection_citations(request):
    collection_acronym = request.matchdict['collection_acronym']
    result = {
        'collection_acronym': collection_acronym,
    }
    return Response(json.dumps(result), content_type="application/json")


@view_config(route_name='journal_citations', request_method='GET')
def journal_citations(request):
    journal_issn = request.matchdict['journal_issn']
    result = {
        'journal_issn': journal_issn,
    }
    return Response(json.dumps(result), content_type="application/json")

