# Write a class program to set and get train details

class Train:

    def __init__(self, TrainId, TrainName, TrainNumber, Destination, Timing):
        self.TrainId = TrainId
        self.TrainName = TrainName
        self.TrainNumber = TrainNumber
        self.Destination = Destination
        self.Timing = Timing

    # Getter and Setter for TrainId
    def getTrainId(self):
        return self.TrainId

    def setTrainId(self, TrainId):
        self.TrainId = TrainId

    # Getter and Setter for TrainName
    def getTrainName(self):
        return self.TrainName

    def setTrainName(self, TrainName):
        self.TrainName = TrainName

    # Getter and Setter for TrainNumber
    def getTrainNumber(self):
        return self.TrainNumber

    def setTrainNumber(self, TrainNumber):
        self.TrainNumber = TrainNumber

    # Getter and Setter for Destination
    def getDestination(self):
        return self.Destination

    def setDestination(self, Destination):
        self.Destination = Destination

    # Getter and Setter for Timing
    def getTiming(self):
        return self.Timing

    def setTiming(self, Timing):
        self.Timing = Timing

    # Display Train Details
    def display(self):
        print("Train ID     :", p1.getTrainId())
        print("Train Name   :", p1.getTrainName())
        print("Train Number :", p1.getTrainNumber())
        print("Destination  :", p1.getDestination())
        print("Timing       :", p1.getTiming())



p1 = Train(101, "Deccan Express", 12123, "Pune", "06:45 AM")
p2 = Train(102, "Sinhagad Express", 11009, "Mumbai", "02:30 PM")
p3 = Train(103, "Vande Bharat Express", 22223, "Solapur", "07:10 AM")




print()

p1.setTrainId(201)
p1.setTrainName("Mahalaxmi Express")
p1.setTrainNumber(17411)
p1.setDestination("Kolhapur")
p1.setTiming("08:30 PM")

print()

p1.display()

print(p3.getTrainName())