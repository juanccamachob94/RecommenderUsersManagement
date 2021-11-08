import ssl
import sys

sys.path.append('./')

from clients.client import Client

ssl._create_default_https_context = ssl._create_unverified_context

# Client.main()

# -----

import os
from dotenv import load_dotenv
load_dotenv()

print(os.environ.get(''))
