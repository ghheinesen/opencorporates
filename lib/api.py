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

    def _get(self, url, **kwargs):
        """
        Wraps requests.get() and handles errors.
        :param url:
        :param params:
        :return:
        """
        # Todo: Handle errors
        response = requests.get(url, params=kwargs)
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
        https://api.opencorporates.com/documentation/API-Reference
        """
        url = self.API_URL + self.VERSIONS_PATH
        return self._get(url)

    def get_companies(self, **kwargs):
        """
        'GET companies/:jurisdiction_code/:company_number' call as described
        in the official documentation.

        Reference:
        https://api.opencorporates.com/documentation/API-Reference
        """
        jurisdiction_code = kwargs.get('jurisdiction_code')
        company_number = kwargs.get('company_number')
        url = self.API_URL + self.COMPANIES_PATH + \
            '/%s/%s' % (jurisdiction_code, company_number)
        return self._get(url, **kwargs)

    def get_companies_search(self, **kwargs):
        """
        'GET companies/search' call as described in the official documentation.

        Reference:
        https://api.opencorporates.com/documentation/API-Reference
        """
        url = self.API_URL + self.COMPANIES_SEARCH_PATH
        return self._get(url=url, **kwargs)
