
# 1396. Design Underground System

class UndergroundSystem(object):

    def __init__(self):
        self.customer_details = {}
        self.ride_details = {}

    def check_in(self, user_id, station_name, t):
        customer_data = self.customer_details.get(user_id)
        if customer_data is None:
            # store customer details
            self.customer_details[user_id] = {"station_in": station_name, "t_in": t}

    def check_out(self, user_id, station_name, t):
        customer_data = self.customer_details.get(user_id)
        # if id exist store his ride details
        if customer_data is not None:
            # ride details
            station_in = customer_data["station_in"]
            station_out = station_name
            # get the last ride details of this src and dst station - a dictionary
            ride_dict = self.ride_details.get((station_in, station_out))
            # if first src-dst stations - create new dictionary
            if ride_dict is None:
                current_ride_time = t - customer_data["t_in"]
                self.ride_details[(station_in, station_out)] = {"ride_time": float(current_ride_time), "counter": 1.0}
            else:
                current_ride_time = t - customer_data["t_in"]
                ride_dict["ride_time"] += current_ride_time
                ride_dict["counter"] += 1
            del self.customer_details[user_id]

    def get_average_time(self, start_station, end_station):
        avg_time = 0.0
        ride_dict = self.ride_details.get((start_station, end_station))
        # if ride details exist
        if ride_dict is not None:
            ride_time = ride_dict["ride_time"]
            counter = ride_dict["counter"]
            avg_time = ride_time/counter
        return avg_time
