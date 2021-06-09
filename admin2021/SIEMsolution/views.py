#from SIEMsolution.serializers import NewsDocumentSerializer
from django.shortcuts import render
from elasticsearch_dsl import connections
from elasticsearch_dsl import Search 
from django.http import  request
from django_elasticsearch_dsl import Document
from flask import Flask

import json


es = connections.create_connection(hosts=['192.168.56.8:9200'])

# Create your views here.


def home(request):
    return render(request, 'index.html')



def log(request):
    res= es.indices.exists(index='logstash')
    
    body = {      "query": {
                        "match": {
                               
                               "hostname" : "apache.com"
                                }
                        }
                }
    res=es.search(index="logstash", body=body)
    logs=res["_source"]
    context= {'data':logs}  
    return render(request, 'tables.html', context)




def error(request):
    return render(request, 'error.html')



def warning(request):
    body = {
                 "from":0,
                 "size":2,
                 "query": {
                        "match": {
                               "hostname":"apache.com",
                               "fields": [
                                   "tag"
                                   "host", 
                                   "hostname", 
                                   "cade"
                    ] 
                                }
                        }
                }
    return render(request, 'warning.html')




def infor(request):
    return render(request, 'infor.html')


def debug(request):
    return render(request, 'debug.html')


def search (request):
    q = request.GET.get('q')
    if q:
        body = { "from":2,
                 "size":1, "query": { "match": {"host": q }}}
        log =es.search(index="logstash", body=body)
    
    else:    
        log='no data'
    return render(request,'tables.html',{'data':log})    

def search_date (request):
    q = request.GET.get('q')
    if q:
        body = { "from":2,
                 "size":1, "query": { "match": {"date": q }}}
        log =es.search(index="logstash", body=body)
    
    else:    
        log=''
    return render(request,'tables.html',{'data':log})    




app = Flask(__name__)



def search_request(request):
    search_term = request.GET.get('apache.com')
    body={
            "query": {
                "multi_match" : {
                    "query": search_term, 
                    "fields": [
                        "host", 
                        "hostname", 
                        "code"
                    ] 
                }
            }
        }
    res = es.search(index="logstash", body=body)
    return render(request,'results.html',{'data':res})    


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host='0.0.0.0', port=5000)

