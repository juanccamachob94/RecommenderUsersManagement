from amazon import amazon_credentials_container
from amazon_credentials_container import AmazonCredentialsContainer

class AmazonDefaultCredentialsContainer(AmazonCredentialsContainer):
    CREDENTIALS_TYPE = 'DEFAULT'
