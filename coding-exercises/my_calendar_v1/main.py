
# 729. My Calendar I

class MyCalendar(object):

    def __init__(self):
        self.calendar = []

    def book(self, startTime, endTime):
        calendar_len = len(self.calendar)
        for i in range(0, calendar_len):
            existing_start = self.calendar[i][0]
            existing_end = self.calendar[i][1]
            # not on the case which promise there is no overlap - given the overlap condition
            if not (startTime >= existing_end or endTime <= existing_start):
                return False

        self.calendar.append([startTime, endTime])
        return True


if __name__ == "__main__":

    obj = MyCalendar()

    ret_val = obj.book(10, 30)
    print(ret_val)
    ret_val = obj.book(20, 30)
    print(ret_val)
    ret_val = obj.book(30, 50)
    print(ret_val)
    ret_val = obj.book(5, 10)
    print(ret_val)