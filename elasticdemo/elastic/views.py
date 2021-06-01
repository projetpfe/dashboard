from django.db.models.indexes import Index
from django.http import response , request
from django.shortcuts import render
from elasticsearch import Elasticsearch , RequestsHttpConnection
from django_elasticsearch_dsl import search
#from django import pytest
from django.conf import settings
from django.db import models
# es_server = ["http://192.168.56.8:9200/"]
# es_index = "log*"
# es = Elasticsearch(es_server, connection_class=RequestsHttpConnection)
# def setup(request):
    
#     response = es.objects.all()
# #    s =search(using = es, Index = "log*").query("matche", any= "date")
# #    response = s.execute()
#     return render(request, 'index.html', context={'all_articles': response, 'message': 'Write something!'})


# for hit in response:
#     print("score:", hit.meta.score,"score:", hit.any, hit.timestamp)

   