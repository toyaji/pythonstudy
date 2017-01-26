class Times(object):
    factor = 1
    @classmethod
    def mul(cls, x):
        return cls.factor*x

class TwoTimes(Times):
    factor = 2

x = TwoTimes.mul(5)

print(x)


from chapter7_ClassOOP.StaticMethod import Date

class EuroDate(Date):
    def __str__(self):
        return "%02d/%02d%04d" % (self.day, self.month, self.year)

print(EuroDate.now())

# EuroDate 의 객체가 아니라 Date 의 객체가 반환됨. 여기서 Static Method 와 Class Method 차이가 있음