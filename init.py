# this package is included to access to extenal file resource
import ssl
import sys

sys.path.append('./')

from clients.client import Client

# context to allow access to external file resources (https://...)
ssl._create_default_https_context = ssl._create_unverified_context

Client.main()
