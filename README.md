vupy
====

Python helper for vufind.

[![pypi version](http://img.shields.io/pypi/v/vupy.svg?style=flat)](https://pypi.python.org/pypi/vupy)

Installation
------------

    $ pip install vupy


vufmdump
--------

Dump binary MARC21 records from VuFind/SOLR.

To download at most 100000 records in chunks of 20 records per SOLR request
from `http://localhost:8983/solr/collection1` into MARC files with 500 records
each, which are stored under `/tmp` with the prefix `coll1-`, run:

    $ vufmdump --url http://localhost:8983/solr/collection1 --limit 100000 --size 20 \
               --records 500 --prefix coll1 --directory /tmp


Options:

    usage: vufmdump [-h] [--url URL] [--query QUERY] [--limit LIMIT] [--size SIZE]
                    [--records RECORDS] [--directory DIRECTORY] [--prefix PREFIX]
                    [--delay DELAY] [--encoding ENCODING]

    optional arguments:
      -h, --help            show this help message and exit
      --url URL, -u URL     Solr server URL (default:
                            http://localhost:8983/solr/biblio)
      --query QUERY, -q QUERY
                            Solr query (default: title:lucene)
      --limit LIMIT, -l LIMIT
                            stop after approximately this number of records, 0 =
                            unlimited (default: 0)
      --size SIZE, -s SIZE  number of records per query (default: 20)
      --records RECORDS, -r RECORDS
                            number of records per file (default: 10000)
      --directory DIRECTORY, -i DIRECTORY
                            directory to write files to (must exists) (default: .)
      --prefix PREFIX, -p PREFIX
                            file prefix, number and .mrc extension will be
                            appended automatically (default: vufmdump-)
      --delay DELAY, -d DELAY
                            delay in seconds between queries (will be jittered)
                            (default: None)
      --encoding ENCODING, -e ENCODING
                            encoding to use (default: utf-8)
