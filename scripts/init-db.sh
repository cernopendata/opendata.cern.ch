#!/usr/bin/env bash

# Destroy db and indexes
cernopendata db destroy --yes-i-know
curl -XDELETE 'http://localhost:9200/_all/'

# Init and create db and indexes
cernopendata db init
cernopendata db create
cernopendata index init

# Populate records with 'recid' type
cernopendata fixtures collections
cernopendata fixtures records
cernopendata fixtures pids

# Index records
cernopendata index queue init
cernopendata index reindex -t recid --yes-i-know
cernopendata index run

# Populate and index records with type 'term'
cernopendata fixtures terms

