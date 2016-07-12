#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import lib.api


def main(**kwargs):
    oc = lib.api.OpenCorporates('0.4.5')
    command = kwargs.pop('command', None)
    if command == 'compsearch':
        print oc.get_companies_search(**kwargs)
    elif command == 'compget':
        print oc.get_companies(**kwargs)
    else:
        print 'Not implemented!'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument(
        '-q',
        '--query',
        help='query string',
        type=str
    )
    parser.add_argument(
        '-j',
        '--jurisdiction-code',
        help='filter by jurisdiction',
        type=str
    )
    parser.add_argument(
        '-c',
        '--company-number',
        help='filter by company number',
        type=str
    )
    args = parser.parse_args()
    main(**vars(args))
