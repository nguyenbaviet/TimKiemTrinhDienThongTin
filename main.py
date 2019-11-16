from urllib.request import urlopen
import urllib.parse as parse
import simplejson
from tokenization.sent_tokenizer import word_tokenizer
import argparse

BASE_LINK = 'http://localhost:8983/solr/test/select?q='


def get_conn(link):
    conn = urlopen(link)
    return conn

def normalizier_query(query):
    query = word_tokenizer(query)
    new_query = []
    for q in query:
        new_query.append(parse.quote('title:"' + q + '"'))
    query = parse.quote(' && ').join(q for q in new_query)
    return query
def excuteQuery(query):
    query = normalizier_query(query)
    final_link = BASE_LINK + query
    print(final_link)
    con = get_conn(final_link)
    data = simplejson.load(con)
    print(data['response']['numFound'])

excuteQuery("Việt Nam")