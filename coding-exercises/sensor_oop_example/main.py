
class Sensor:

    def __init__(self, sensor_id, name):
        self.sensor_id = sensor_id
        self.name = name
        self.value = 0
        self.is_active = False

    def read_value(self):
        return self.value

    def set_value(self, new_val):
        if self.is_active:
            self.value = new_val
        else:
            print("Sensor is not active")

    def enable(self):
        self.is_active = True

    def disable(self):
        self.is_active = False

    def print_status(self):
        print(f"Sensor id: {self.sensor_id}")
        print(f"Sensor name: {self.name}")
        print(f"Sensor value: {self.value}")
        if self.is_active:
            print("Status: Active")
        else:
            print("Status: Disabled")

if __name__ == '__main__':

    sensor = Sensor(3, "Temperature")
    sensor.print_status()