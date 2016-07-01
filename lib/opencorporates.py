# -*- coding: utf-8 -*-

import requests


class OpenCorporates(object):
    # Current (at the time of writing) version of the OpenCorporates API.
    VERSION = '0.4.5'
    API_URL = 'https://api.opencorporates.com/v%s' % VERSION
    VERSIONS_PATH = '/versions'
    COMPANIES_PATH = '/companies'
    COMPANIES_SEARCH_PATH = COMPANIES_PATH + "/search"

    def __init__(self, version=VERSION):
        self.version = version

    def _get(self, url, params=None):
        """
        Wraps requests.get() and handles errors.
        :param url:
        :param params:
        :return:
        """
        # Todo: Handle errors
        response = requests.get(url, params=params)
        # Todo: Implement proper logging
        print('GET: %s' % response.request.url)
        if response.status_code == 200:
            result = response.content
        return result

# ----- get_x() methods ----- #
# These build the url and (optionally) params and delegate to self.get().

    def get_versions(self):
        """
        'GET versions' call as described in the official documentation.

        Reference:
        http://api.opencorporates.com/documentation/API-Reference
        """
        url = self.API_URL + self.VERSIONS_PATH
        return self._get(url)

    def get_companies(self, jurisdiction_code, company_number, sparse=False):
        """
        'GET companies/:jurisdiction_code/:company_number' call as described
        in the official documentation.

        Reference:
        http://api.opencorporates.com/documentation/API-Reference
        """
        params = {}
        url = self.API_URL + self.COMPANIES_PATH + \
            '/%s/%s' % (jurisdiction_code, company_number)
        if sparse:
            params = {'sparse': True}
        return self._get(url, params=params)

    def get_companies_search(self, q, jurisdiction_code=None,
                             country_code=None, company_type=None,
                             current_status=None, industry_codes=None,
                             registered_address=None, created_since=None,
                             incorporation_date=None, dissolution_date=None,
                             incorporated_before=None, incorporated_since=None,
                             disolved_before=None, dissolved_since=None,
                             exclude_inactive=None, inactive=None, branch=None,
                             nonprofit=None, fields=None,
                             normalize_company_name=None, created_at=None,
                             updated_at=None, order=None):
        """
        'GET companies/search' call as described in the official documentation.

        Reference:
        http://api.opencorporates.com/documentation/API-Reference
        """
        params = {
            'q': q,
            'jurisdiction_code': jurisdiction_code,
            'country_code': country_code,
            'company_type': company_type,
            'current_status': current_status,
            'industry_codes': industry_codes,
            'registered_address': registered_address,
            'created_since': created_since,
            'incorporation_date': incorporation_date,
            'dissolution_date': dissolution_date,
            'incorporated_before': incorporated_before,
            'incoporated_since': incorporated_since,
            'disolved_before': disolved_before,
            'dissolved_since': dissolved_since,
            'exclude_inactive': exclude_inactive,
            'inactive': inactive,
            'branch': branch,
            'nonprofit': nonprofit,
            'fields': fields,
            'normalize_company_name': normalize_company_name,
            'created_at': created_at,
            'updated_at': updated_at,
            'order': order,
        }
        url = self.API_URL + self.COMPANIES_SEARCH_PATH
        return self._get(url=url, params=params)
