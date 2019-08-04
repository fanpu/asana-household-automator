import logging
import asana
import yaml
import ipdb
from rent_automation import RentAutomation
from house_fund_automation import HouseFundAutomation

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


    def setup_client(self):
        self.client = asana.Client.access_token(self.ACCESS_TOKEN)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Asana Household Manager starting...")
    app = App()
    rent_automation = RentAutomation()
    house_fund_automation = HouseFundAutomation()

    while True:
        rent_automation.run()
        house_fund_automation.run()



if __name__ == "__main__":
    main()

