class FO(object):
    #flying object
    def __init__(self):
        self.lat = 0.0
        self.lon = 0.0
        self.alt = 0.0
        self.angle = 0.0

    def getParams(self, msg):
        if msg.sentence_type == "GGA":
            print(msg.fields)
            self.lat = float(msg.lat)
            self.lon = float(msg.lon)
            self.alt = float(msg.altitude)
        else:
            if msg.sentence_type == "RMC":
                print(msg.fields)
                self.lat = float(msg.lat)
                self.lon = float(msg.lon)
                self.angle = float(msg.true_course)
