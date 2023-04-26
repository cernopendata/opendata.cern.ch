#!/bin/bash
#
# Helper script for developers to generate certificates for running CERN Open Data portal locally.

openssl req -x509 -out ./elasticsearch-proxy/nginx.crt -keyout ./elasticsearch-proxy/nginx.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
