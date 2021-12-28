class Alert:
    def __init__(self, color, year, humidity_mean, temperature_mean, vibration_mean):
        self.color = color
        self.year = year
        self.humidity_mean = humidity_mean
        self.temperature_mean = temperature_mean
        self.vibration_mean = vibration_mean
        self.alert = False


