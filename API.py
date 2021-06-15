import requests

{
     "post code": "90210",
     "country": "United States",
     "country abbreviation": "US",
     "places": [
         {
             "place name": "Beverly Hills",
             "longitude": "-118.4065",
             "state": "California",
             "state abbreviation": "CA",
             "latitude": "34.0901"
         }
     ]
}
def test_get_locations_for_us_90210_check_status_code_equals_200():
     response = requests.get("http://api.zippopotam.us/us/90210")
     assert response.status_code == 200