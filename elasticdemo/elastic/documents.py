from typing import Any
from django.db.models.indexes import Index
from django_elasticsearch_dsl import Document, search 
from elasticsearch_dsl.serializer import serializer
from django_elasticsearch_dsl.registries import registry
from elasticsearch import Elasticsearch , RequestsHttpConnection
from .models import Car
from elasticsearch_dsl import connections
from django.template import context, Template
from django.shortcuts import render
from django.conf import settings
from django.core.management.base import BaseCommand

from elastic import models

es = Elasticsearch(HOST="http://localhost", PORT=9200)
es = Elasticsearch()
# def index(request):
    
#     logs= es.apache.search().query("match", hostname="apache.com")
#     return render(request, "index.html")


# class Command(BaseCommand):

#     def __init__(self):
#         super(Command, self).__init__()
#         self.indexes = []
#         connections = settings.ELASTICSEARCH_DSL
#         indexes = settings.ES_INDEXES
#         for name, value in connections.items():
#             for index_name in indexes.get(name):
#                 self.indexes.append({
#                     'connection_name': name,
#                     'connection': value,
#                     'index_name': index_name,
#                 })


posts=Index('posts')
@posts.doc_type
class PostDocument(Document):
    class Meta:
        es.indices.exists(index='logstash')
        fields = [
            'title',
            'id',
            'slug',
            'image',
            'discription',
        ]