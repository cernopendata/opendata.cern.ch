#!/usr/bin/env bash
# Destroy db and indexes
cernopendata db destroy --yes-i-know
curl -XDELETE 'http://localhost:9200/_all/'

# Init and create db and indexes
cernopendata db init
cernopendata db create
cernopendata index init
