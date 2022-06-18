class Device:

    def __init__(self, type_of_device: str = "voltmeter", brand_of_the_device: str = "B-16A",
                 measurement_limit_minimum: float = 0, measurement_limit_maximum: float = 100, graduation_year: int = 2020):
        self.type_of_device = type_of_device
        self.brand_of_the_device = brand_of_the_device
        self.measurement_limit_minimum = measurement_limit_minimum
        self.measurement_limit_maximum = measurement_limit_maximum
        self.graduation_year = graduation_year

    def __str__(self):
        return f"The device is {self.type_of_device}, the brand of the device - {self.brand_of_the_device} and " \
               f"its measurement limit is from {self.measurement_limit_minimum} to {self.measurement_limit_maximum}," \
               f" year of release - {self.graduation_year}"
