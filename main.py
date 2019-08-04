import logging
import asana
import yaml
import ipdb

class App():
    def __init__(self):
        self.load_secrets()
        self.client = self.setup_client()

    """Loads the access token from .secrets.yaml

    .secrets should NOT be checked into source control

    Sets the following:
    self.ACCESS_TOKEN
    """
    def load_secrets(self):
        with open(".secrets.yaml") as file:
            data = file.read()
            secrets = yaml.load(data, Loader=yaml.FullLoader)
            self.ACCESS_TOKEN =  secrets['ACCESS_TOKEN']


    """Loads config from config.yaml

    .secrets should NOT be checked into source control

    Sets the following:
    self.RENT_COLLECTION_DEADLINE_DAY
    self.RENT_PAYMENT_DEADLINE_DAY
    """
    def load_config(self):
        with open("config.yaml") as file:
            data = file.read()
            config = yaml.load(data, Loader=yaml.FullLoader)
            self.RENT_COLLECTION_DEADLINE_DAY =  config['RENT_COLLECTION_DEADLINE_DAY']
            self.RENT_PAYMENT_DEADLINE_DAY = config['RENT_PAYMENT_DEADLINE_DAY']


    def setup_client(self):
        self.client = asana.Client.access_token(self.ACCESS_TOKEN)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Asana Household Manager starting...")
    app = App()


if __name__ == "__main__":
    main()

