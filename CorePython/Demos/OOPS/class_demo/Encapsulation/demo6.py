# Write a class program to set and get patient details

class Patient:

    # Constructor
    def __init__(self, WardNumber, PatientId, Name, Disease, MoNumber, Adrs):
        self.WardNumber = WardNumber
        self.PatientId = PatientId
        self.Name = Name
        self.Disease = Disease
        self.MoNumber = MoNumber
        self.Adrs = Adrs

    # Getter and Setter for WardNumber
    def getWardNumber(self):
        return self.WardNumber

    def setWardNumber(self, WardNumber):
        self.WardNumber = WardNumber

    # Getter and Setter for PatientId
    def getPatientId(self):
        return self.PatientId

    def setPatientId(self, PatientId):
        self.PatientId = PatientId

    # Getter and Setter for Name
    def getName(self):
        return self.Name

    def setName(self, Name):
        self.Name = Name

    # Getter and Setter for Disease
    def getDisease(self):
        return self.Disease

    def setDisease(self, Disease):
        self.Disease = Disease

    # Getter and Setter for Mobile Number
    def getMoNumber(self):
        return self.MoNumber

    def setMoNumber(self, MoNumber):
        self.MoNumber = MoNumber

    # Getter and Setter for Address
    def getAdrs(self):
        return self.Adrs

    def setAdrs(self, Adrs):
        self.Adrs = Adrs

    # Display Patient Details
    def display(self):
        print("Ward Number :", p1.getWardNumber())
        print("Patient ID  :", p1.getPatientId())
        print("Name        :", p1.getName())
        print("Disease     :", p1.getDisease())
        print("Mobile No   :", p1.getMoNumber())
        print("Address     :", p1.getAdrs())



p1 = Patient( "1st-floor-A",101, "Rajwardhan", "Fever", 7499232277, "YCM - Pune")
p2 = Patient("1st-floor-B",217 , "Ashish", "headache", 7822973954, "YCM - Pune")
p3 = Patient("1st-floor-C", 218, "soham", "low-wbc", 1234567890, "YCM - Pune")



# Update Details using Setters
print()

p1.setWardNumber(102)
p1.setPatientId("7th-floor-A")
p1.setName("Rohan")
p1.setDisease("Dengue")
p1.setMoNumber("9988776655")
p1.setAdrs("YCM-pune")


print()


p1.display()

print(p2.getName())
    
    
    

    

    

        