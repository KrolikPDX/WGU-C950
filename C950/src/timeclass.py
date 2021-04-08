#Joseph Demyanovskiy 001208427

class Time(object):
    def __str__(self):
        #So we don't print time as 10:7 instead of 10:07
        if self.minute < 10:
            return str(int(self.hour)) + ":" + "0" + str(int(self.minute))
        return str(int(self.hour)) + ":" + str(int(self.minute))

    def __init__(self, hour, minute):
        #Military time
        self.hour = hour
        self.minute = minute

    def add(self, minute):
        # SPACE | TIME COMPLEXITY:
        # O(1) | O(1)
        total_minutes = minute + self.minute
        if total_minutes >= 60:
            hours = (total_minutes // 60)
            self.hour += hours
            total_minutes = (total_minutes - (hours * 60))
        self.minute = total_minutes
        # TOTAL SPACE | TIME COMPLEXITY: O(1) | O(1)

#Setup comparisons to have the ability to compare times
    def __le__(self, other):
        if other is not None:
            if self.hour < other.hour:
                return True
            elif self.hour > other.hour:
                return False
            elif self.hour == other.hour:
                if self.minute < other.minute or self.minute == other.minute:
                    return True
            else:
                return False
    #If self.time < other.time return true
    def __lt__(self, other):
        if other is not None:
            if self.hour < other.hour:
                return True
            elif self.hour > other.hour:
                return False
            else:
                if self.minute < other.minute:
                    return True
                else:
                    return False
    #If self.time >= other return true
    def __ge__(self, other):
        if other is not None:
            if self.hour > other.hour:
                return True
            elif self.hour < other.hour:
                return False
            elif self.hour == other.hour:
                if self.minute > other.minute or self.minute == other.minute:
                    return True
            else:
                return False
    #If self.time > other.time return true
    def __gt__(self, other):
        return not self.__lt__(other)






