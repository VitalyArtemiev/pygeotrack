import math
from math import pi

import FO
import geo
import numpy as np

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

class GO(object):
    #ground object

    def __init__(self, latitude, longitude, altitude):
        self.lat = latitude
        self.lon = longitude
        self.alt = altitude
        self.pitch = 0.0
        self.yaw = 0.0
        self.pitchdeg = 0.0
        self.yawdeg = 0.0

    def calcDir(self, obj):
        #print(obj.lat, obj.lon, obj.alt)
        #print(self.lat, self.lon, self.alt)

        x, y, z = geo.geodetic_to_enu(obj.lat, obj.lon, obj.alt, self.lat, self.lon, self.alt)
        print(x,y,z)
        self.pitch = angle_between((x,y,z),(x,y,0))
        self.yaw = angle_between((1,0,0),(x,y,0))

        from math import pi
        if self.yaw > pi :
            yaw = self.yaw - pi
            pitch = pi - self.pitch

        self.pitchdeg = math.degrees(self.pitch)
        self.yawdeg = math.degrees(self.yaw)

    def printDir(self):
        print("pitch " + str(self.pitch / pi) + "PI")
        print("yaw " + str(self.yaw / pi) + "PI")

    def printDirDeg(self):
        print("pitch " + str(self.pitch) + "degrees")
        print("yaw " + str(self.yaw) + "degrees")



