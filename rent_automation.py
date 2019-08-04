class RentAutomation():
    def __init__(self):
        self.load_config

    """Loads config for rent from config.yaml

    .secrets should NOT be checked into source control

    Sets the following:
    self.RENT_COLLECTION_DEADLINE_DAY
    self.RENT_PAYMENT_DEADLINE_DAY
    self.RENT_PAYMENT_SECTION_ID
    self.FINANCE_PROJECT_ID
    """
    def load_config(self):
        with open("config.yaml") as file:
            data = file.read()
            config = yaml.load(data, Loader=yaml.FullLoader)
            self.RENT_COLLECTION_DEADLINE_DAY =  config['RENT_COLLECTION_DEADLINE_DAY']
            self.RENT_PAYMENT_DEADLINE_DAY = config['RENT_PAYMENT_DEADLINE_DAY']
            self.RENT_PAYMENT_SECTION_ID = config['RENT_PAYMENT_SECTION_ID']
            self.FINANCE_PROJECT_ID = config['FINANCE_PROJECT_ID']

    def run(self):
        pass

