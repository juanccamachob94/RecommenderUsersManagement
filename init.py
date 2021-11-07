import ssl

from clients.client import Client

ssl._create_default_https_context = ssl._create_unverified_context

# Client.main()

# -----

import os
from dotenv import load_dotenv
load_dotenv()

print(type(os.environ.get('PRUEBA')))
