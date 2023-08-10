# To get the country location of the number
from phonenumbers import carrier
import phonenumbers

from phonNum import number

from phonenumbers import geocoder

personNum = phonenumbers.parse(number)

personLocation = geocoder.description_for_number(personNum, "en")
print(personLocation)

# Get service provider e.g Aitel, MTN, ETC

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# Get the latitude and longitude for  the map

geocoder = OpenCageGeocode(key)
query = str(personLocation)

result = geocoder.geocode(query)
print(result)
