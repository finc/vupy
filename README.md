vupy
====

Python helper for vufind.

[![pypi version](http://img.shields.io/pypi/v/vupy.svg?style=flat)](https://pypi.python.org/pypi/vupy)

Installation
------------

    pip install vupy


vufmdump
--------

Dump binary MARC21 records from VuFind.

    usage: vufmdump [-h] [--url URL] [--query QUERY] [--limit LIMIT] [--size SIZE]
                    [--records RECORDS] [--directory DIRECTORY] [--prefix PREFIX]
                    [--delay DELAY] [--encoding ENCODING]

    optional arguments:
      -h, --help            show this help message and exit
      --url URL, -u URL     Solr server URL
      --query QUERY, -q QUERY
                            Solr query
      --limit LIMIT, -l LIMIT
                            max records, 0 = unlimited
      --size SIZE, -s SIZE  number of records per query
      --records RECORDS, -r RECORDS
                            number of records per file
      --directory DIRECTORY, -i DIRECTORY
                            directory to write files to (must exists)
      --prefix PREFIX, -p PREFIX
                            file output basename, number and .mrc extension will
                            be appended automatically
      --delay DELAY, -d DELAY
                            delay in seconds between queries
      --encoding ENCODING, -e ENCODING
                            encoding to use
