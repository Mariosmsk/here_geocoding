#!/usr/bin/env python
from here_geocoding import geocoding

api_key = 'QlwnYCsPMyPc2CJXrpyb7b1fjnvnw38BHN0gjXlfpOY'  # OK

d = geocoding(api_key=api_key)

# Example 1
lng, lat = d.address_to_lnglat(address='1 Panepistimiou Ave., Aglantzia, 2109, Nicosia, Cyprus')
print(lng, lat)

# Example 2
lng, lat = d.address_to_lnglat(address='Perikleous 94, Nicosia',
                               bbox=[33.34597224, 35.13605854, 33.36261015, 35.14613025])
print(lng, lat)

# Example 3
data_geojson = d.address_to_lnglat(address='1 Panepistimiou Ave., Aglantzia, 2109, Nicosia, Cyprus', geojson=True)
print(data_geojson)
z
# Example 4
# using as example the csv file from: https://github.com/geocommons/geocoder/blob/master/test/data/address-sample.csv
d.geocode_excel(file_path='address-sample.xlsx', start_row=-1, end_row=20, address_column='address', bbox=None,
                to_crs=None, export_file_name='test', export_file_type='csv')

# Example 5
d.geocode_excel(file_path='address-sample.xlsx', start_row=-1, end_row=20, address_column='address', bbox=None,
                to_crs=None, export_file_name='test', export_file_type='geojson')
