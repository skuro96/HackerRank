class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        abs_max = 0
        for i in range(len(self.__elements)):
            for j in range(i, len(self.__elements)):
                abs_max = max(abs_max, abs(self.__elements[i] - self.__elements[j]))
        self.maximumDifference = abs_max

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)