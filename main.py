import logging
import asana
import yaml
import ipdb

class App():
    def __init__(self):
        self.load_secrets()
        self.setup_client()

    def load_secrets(self):
        with open(".secrets") as file:
            data = file.read()
            secrets = yaml.load(data, Loader=yaml.FullLoader)
            self.CLIENT_ID = secrets['CLIENT_ID']
            # self.CLIENT_SECRET = secrets['CLIENT_ID']
            # self.ACCESS_TOKEN =  secrets['ACCESS_TOKEN']

    def setup_client(self):
        self.client = asana.Client.access_token(self.ACCESS_TOKEN)

def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Asana Household Manager starting...")
    app = App()

if __name__ == "__main__":
    main()

