from ... import constants as ytm_constants

__all__ = __name__.split('.')[-1:]

def search_suggestions(self, query=None):
    url = self._url_api(ytm_constants.ENDPOINT_YTM_API_SEARCH_SUGGESTIONS)

    params  = ytm_constants.URL_PARAMS
    payload = ytm_constants.PAYLOAD

    payload['input'] = query or ''

    resp = self.session.post \
    (
        url    = url,
        params = params,
        json   = payload,
    )

    data = resp.json()

    return data