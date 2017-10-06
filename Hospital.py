import random
class Patient(object):
    def __init__(self, ID, name, allergies, bed_no = 'none'):
        self.ID = ID
        self.name = name
        self.allergies = allergies
        self.bed_no = bed_no
        

    def display (self):
        print ""
        print self.ID
        print self.name
        print self.allergies
        print self.bed_no

class Hospital(object):
    def __init__(self):
        self.patients = []
        self.hos_name = 'Death Valey Health Center'
        self.capacity = 2

    def admit (self, adm):
        if len(self.patients) >= self.capacity:
            	print "Hospital is full"
        else:
        	self.patients.append(adm)
        	adm.bed_no = random.randint(100,110)
          	print "Admission is complete"
        return self
        
    def display_info(self):
        for i in self.patients:
            i.display()
    
    def discharge(self, pat):
    	self.patients.remove(pat)
    	print "Discharging Patient"
    	return self


pat1 = Patient('q5t7y2', 'David', 'Coding')
pat2 = Patient('t4h9z1', 'Jason', 'Alcohol')
pat3 = Patient('a7b2p6', 'Kyo', 'OOP')
hos1 = Hospital().admit(pat1).admit(pat2).admit(pat3).discharge(pat1).display_info()
