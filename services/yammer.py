import json

import foauth.providers


class Yammer(foauth.providers.OAuth2):
    # General info about the provider
    provider_url = 'https://www.yammer.com/'
    favicon_url = 'https://www.yammer.com/favicon.ico'
    docs_url = 'https://developer.yammer.com/api/'

    # URLs to interact with the API
    authorize_url = 'https://www.yammer.com/dialog/oauth'
    access_token_url = 'https://www.yammer.com/oauth2/access_token.json'
    api_domain = 'www.yammer.com'

    available_permissions = [
        (None, 'read and post to your stream'),
    ]

    def parse_token(self, content):
        data = json.loads(content)
        return data['access_token']['token'], None
