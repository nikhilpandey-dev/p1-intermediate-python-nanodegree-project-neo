from models import NearEarthObject, CloseApproach

neo = NearEarthObject(433, 'Eros', 16.84, "Y")

ca = CloseApproach(433, "1900-Jan-01 00:11", 0.0921795123769547, 16.7523040362574, neo)

print(ca)
print(type(ca.time))
print(ca.time_str)
print(ca.distance)
print(ca.velocity) 
print(ca)