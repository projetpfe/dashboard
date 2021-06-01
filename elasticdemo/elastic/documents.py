from typing import Any
from django_elasticsearch_dsl import Document, search 
from elasticsearch_dsl.serializer import serializer
from django_elasticsearch_dsl.registries import registry
from elasticsearch import Elasticsearch , RequestsHttpConnection
from .models import Car
from elasticsearch_dsl import connections
from django.template import context, Template
from django.shortcuts import render



es = connections.create_connection(hosts=['192.168.56.8:9200'], timeout=20)

def index(request):
    
    logs = es.search(index="log*") \
    .filter("term", category="search") \
    .query("match", type="text")   \
    .exclude("match", description="beta")
    response = logs.execute()

    return render(response, "index.html")

