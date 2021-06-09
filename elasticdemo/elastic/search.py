
from typing import Any
from django_elasticsearch_dsl import Document, search ,DocType
from elasticsearch_dsl.serializer import serializer
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections, Elasticsearch , RequestsHttpConnection
from django.db import models
from elasticsearch_dsl import connections
from elasticsearch.helpers import bulk
from django.shortcuts import render

connections.create_connection()
class TaskIndex(DocType):
    title = models.CharField(max_length=100)
    class Meta:
        index = 'task-index'

def bulk_indexing():
    TaskIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Task.objects.all().iterator()))

# Simple search function
def _search(title):
    s = search().filter('term', title=title.text)
    response = s.execute()
    return response
