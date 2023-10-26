#connection checker

from http.client import HTTPConnection
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """Return True if the target URL is online.
    Raise an exception otherwise."""
    error = Exception("Unknown Error")
    parser = urlparse(url)
    # Extract hostname from target URL
    host = parser.netloc or parser.path.split("/")[0]
    # check if url is available for both http and https
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            # send a head request to the url
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally: 
            connection.close()
    raise error