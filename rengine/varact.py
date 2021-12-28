from business_rules import variables, actions, fields

class ProductVariables(variables.BaseVariables):
    def __init__(self, product):
        self.product = product

    @variables.numeric_rule_variable(label='Year')
    def year(self):
        return self.product.year

    @variables.string_rule_variable(label='Color')
    def color(self):
        return self.product.color

    @variables.numeric_rule_variable(label='Vibration mean')
    def vibration(self):
        return self.product.vibration_mean

    @variables.numeric_rule_variable(label='Temperature mean')
    def temperature(self):
        return self.product.temperature_mean

    @variables.numeric_rule_variable(label='Humidity mean')
    def humidity(self):
        return self.product.humidity_mean

    @variables.select_rule_variable(label='Alert', options=[True, False])
    def alert(self):
        return self.product.alert

class ProductActions(actions.BaseActions):
    def __init__(self, product):
        self.product = product

    @actions.rule_action(params={"alert" : fields.FIELD_TEXT})
    def alert_state(self, alert):
        self.product.alert = alert
