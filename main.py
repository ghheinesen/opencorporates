#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.opencorporates


def main():
    opencorporates = lib.opencorporates.OpenCorporates()
    print(opencorporates.get_versions())
    print(opencorporates.get_companies(
        jurisdiction_code='dk',
        company_number='25052943',
        sparse=True)
    )
    print(opencorporates.get_companies(
        jurisdiction_code='dk',
        company_number='25052943',
        sparse=False)
    )
    print(opencorporates.get_companies_search(q='bank',
                                              jurisdiction_code='dk'))
    return

if __name__ == "__main__":
    main()
