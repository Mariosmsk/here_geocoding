"""Main module."""
import requests
import pyproj  # 2.6.1post1
import random
import pandas as pd
import urllib
import json
import os
import re
from here_location_services import LS


class geocoding:

    def __init__(self, api_key=None):
        try:
            self.ls = LS(api_key=api_key)
        except:
            print('Use your api key: https://platform.here.com/admin/apps/')

    def address_to_lnglat(self, address=None, bbox=None, to_crs=None, geojson=False):
        if address is None:
            return False
        try:
            if bbox is None:
                geo = self.ls.geocode(query=address)
            else:
                geo = self.ls.autosuggest(query=address, search_in_bbox=bbox)
            data_json = json.dumps(geo.to_geojson(), indent=2, sort_keys=True)
            data = json.loads(data_json)
            try:
                lat = data['features'][0]['properties']['access'][0]['lat']
                lng = data['features'][0]['properties']['access'][0]['lng']
            except:
                try:
                    lat = data['features'][0]['geometry']['coordinates'][1]
                    lng = data['features'][0]['geometry']['coordinates'][0]
                except:
                    lat = None
                    lng = None
            x, y = (lng, lat)
            if to_crs:
                proj = pyproj.Transformer.from_crs(4326, to_crs, True)
                x, y = proj.transform(y1, x1)
        except Exception as e:
            print(e)

        if geojson:
            data = geo.to_geojson()
            return [data]

        return y, x

    def geocode_excel(self, file_path='', start_row=-1, end_row=None, address_column=None, bbox=None, to_crs=None,
                      export_file_name='test', export_file_type='csv'):

        df = pd.read_excel(file_path)
        if end_row is None:
            end_row = df[address_column].__len__()

        latlng = []
        for i, address in enumerate(df[address_column]):
            if end_row < i:
                break
            if i > start_row:
                x, y = self.address_to_lnglat(address=address, bbox=bbox, to_crs=to_crs)
                all_col_values = list(df.iloc[i, :])
                all_col_values.extend([y, x])
                latlng.append(all_col_values)

        all_col_keys = list(df.keys())
        all_col_keys.extend(['lat', 'lng'])
        df_new = pd.DataFrame(latlng, columns=all_col_keys)
        export_file = export_file_name + '.' + export_file_type
        if export_file_type == 'csv':
            df_new.to_csv(export_file)
        if export_file_type == 'geojson':
            geojson = {
                "type": "FeatureCollection",
                "features": []
            }

            for _, row in df_new.iterrows():
                properties = {}
                for key in df.keys():
                    properties[key] = row[key]

                feature = {
                    "type": "Feature",
                    "properties": properties,
                    "geometry": {
                        "type": "Point",
                        "coordinates": [row['lat'], row['lng']]
                        # Replace 'Longitude' and 'Latitude' with your column names
                    }
                }
                geojson['features'].append(feature)

            with open(export_file, 'w') as f:
                json.dump(geojson, f)
            print(f'File created "{export_file}".')
