import json

class TaxGraph:
    
    def __init__(self):

        self.__tax_config = None
        self.tax_config = 'tax_config_fed.json'
        print(self.tax_config)

    @property
    def tax_config(self):
        return self.__tax_config

    @tax_config.setter
    def tax_config(self, fn_config):
        if self.tax_config is None:
            with open(fn_config) as f:
                self.__tax_config = json.load(f)


if __name__ == '__main__':
    tax_graph = TaxGraph()
