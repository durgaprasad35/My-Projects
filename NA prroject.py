class Parallel:
    def __init__(self,res_1,res_2,res_3):
        self.resistance1 = res_1
        self.resistance2 = res_2
        self.resistance3 = res_3
    def slove(self):
        result = self.resistance1 * self.resistance2 * self.resistance3 
        sum = self.resistance1 + self.resistance2 + self.resistance3
        equivalent = result / sum
        print(equivalent)
        print(f"Hence the equivalent resistance in parellel connection is  {equivalent}")
        #print(result)
        #print(sum)

class Series:
    def __init__(self,ress1,ress2,ress3):
        self.resistor1 = ress1
        self.resistor2 = ress2
        self.resistor3 = ress3
    def slove(self):
        result2 = self.resistor1 + self.resistor2 + self.resistor3
        print(result2)
        print(f"Hence the equivalent resistance in series connection is {result2}")
parallel1 = Parallel(15,15,15)
parallel1.slove()
series1 = Series(15,15,15)
series1.slove()

