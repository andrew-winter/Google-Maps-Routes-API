import datetime
import os
import requests
import googlemaps


# %%
def build_address(line_one = '', city = '', state = '', *, line_two = False):
    '''Programmatically build US street address

    Optionally add line two and state
    '''
    address = line_one
    if line_two:
        address += line_two
    address += f', {city}'
    # Account for District of Columbia
    if state:
        address += f', {state}'
    return address

# %%
wh_info = ('1600 Pennsylvania Drive', 'District of Colubmia')
wh_address = build_address(*wh_info)

# %%
coordinates_origin = (34.063978346887474, -118.36504834829995)
coordinates_destination = (34.04558775149983, -118.2359983655502)
def build_request(origin, destination, *, params=False):
    '''Programmatically build request for Google's Routes API

    Pass coordinates in tuples for both origin and destination
    '''
    location_map = {'origin': origin, 'destination': destination}
    location_params = {
        k: {'location': {'latLng': {'latitude': v[0], 'longitude': v[1]}}}
        for (k, v)
        in zip(location_map.keys(), location_map.values())}
    if not params:
        other_params = {
            'travelMode': 'DRIVE',
            'routingPreference': 'TRAFFIC_AWARE',
            'computeAlternativeRoutes': False,
            'routeModifiers': {
                'avoidTolls': False,
                'avoidHighways': False,
                'avoidFerries': False},
            'languageCode': 'en-US',
            'units': 'IMPERIAL'}
    request = location_params | other_params
    return request
example_request = build_request(coordinates_origin, coordinates_destination)

# %%
routes_url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key':  os.environ.get('GOOGLE_MAPS_API_KEY')}
r = requests.request('POST', routes_url, data=example_request, headers=headers)


# %%

    'units': 'IMPERIAL'}



# %%
gmaps = googlemaps.Client(key=os.environ.get('GOOGLE_MAPS_API_KEY'))

wh_geocode = gmaps.geocode(wh_address)

# %%
class GoogleMap:
    def __init__(self, df, etl, validation):
        self.df = df.copy()
        self.etl = etl
        self.validation = validation

    def validate_source(self):
        input_df = self.df.copy()
        output_df = input_df.copy
        for step in self.validation:
            output_df.apply(step, axis=0)
        return output_df

# %%
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# %%
# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# %%
# Request directions via public transit
now = datetime.datetime.now()
directions_result = gmaps.directions('Sydney Town Hall',
                                     'Parramatta, NSW',
                                     mode='transit',
                                     departure_time=now)

# Validate an address with address validation
addressvalidation_result =  gmaps.addressvalidation(['1600 Amphitheatre Pk'], 
                                                    regionCode='US',
                                                    locality='Mountain View', 
                                                    enableUspsCass=True)

# Get an Address Descriptor of a location in the reverse geocoding response
address_descriptor_result = gmaps.reverse_geocode((40.714224, -73.961452), enable_address_descriptor=True)

# %%
