import json

class TaxGraph:
    
    def __init__(self):

        self.__tax_config = None
        self.tax_config = 'tax_config_fed.json'
        #print(self.tax_config)
        print(self.get_coordinates_by_fs('married_joint'))

    def get_coordinates_by_fs(self, filing_status):
        tax_coord = list()
        adjusted_gross_hi = int(self.tax_config['withholding_schedules'][filing_status][-1][0] * 1.2)
        x_range = range(0, adjusted_gross_hi, 50)
        y_tax_fed = [self.calc_tax(filing_status, x, self.tax_config) for x in x_range]
        tax_coord = [x_range, y_tax_fed]
        return tax_coord

    @property
    def tax_config(self):
        return self.__tax_config

    @tax_config.setter
    def tax_config(self, fn_config):
        if self.tax_config is None:
            with open(fn_config) as f:
                self.__tax_config = json.load(f)

    @classmethod
    def calc_tax(cls, filing_status, adjusted_gross, tax_config):
        # gross_pay - pre-tax deductions - standard_deduction = taxable_income
        # tax_amt = base_withholding + (taxable_income - over) * rate)
        tax_bracket = tax_config['withholding_schedules'][filing_status]
        std_ded = tax_config['standard_deductions'][filing_status]
        taxable_income = max(adjusted_gross - std_ded, 0)
        tax_amt = None
        for tb in tax_bracket:
            if taxable_income >= tb[0] and (tb[1] is None or taxable_income <= tb[1]):
                tax_amt = round(tb[2] + (taxable_income - tb[0]) * tb[3], 2)
                break
        #print('filing_status', filing_status, 'adjusted_gross', adjusted_gross, 'taxable_income', taxable_income, 'tax_amt', tax_amt)
        return tax_amt


if __name__ == '__main__':
    tax_graph = TaxGraph()
