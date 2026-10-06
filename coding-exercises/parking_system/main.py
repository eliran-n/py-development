
# 1603. Design Parking System

class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big         # 1
        self.medium = medium   # 2
        self.small = small     # 3
        self.parking_cnt = {"1": self.big, "2": self.medium , "3": self.small}

    def addCar(self, carType):
        if 3 < carType < 1:
            return False
        if self.parking_cnt[str(carType)] > 0:
            self.parking_cnt[str(carType)] -= 1
            return True
        else:
            return False

if __name__ == "__main__":
    p1 = ParkingSystem(4, 2, 2)
    status = p1.addCar(1)
    print(status)
    status = p1.addCar(1)
    print(status)
    status = p1.addCar(2)
    print(status)
    status = p1.addCar(2)
    print(status)
    status = p1.addCar(2)
    print(status)
    status = p1.addCar(3)
    print(status)