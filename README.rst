==============
here-geocoding
==============


.. image:: https://img.shields.io/pypi/v/here_geocoding.svg
        :target: https://pypi.python.org/pypi/here_geocoding

.. image:: https://img.shields.io/travis/mariosmsk/here_geocoding.svg
        :target: https://travis-ci.com/mariosmsk/here_geocoding

.. image:: https://readthedocs.org/projects/here-geocoding/badge/?version=latest
        :target: https://here-geocoding.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




The "here-geocoding" package is a Python library designed to streamline the process of converting addresses stored in an Excel (xlsx) file into latitude and longitude coordinates. It provides a convenient solution for geocoding large sets of addresses using the HERE geocoding service.

The package is based on the: https://github.com/heremaps/here-location-services-python

* Free software: MIT license
* Documentation: https://here-geocoding.readthedocs.io.

How to install
---------------

**Environments -> base (root) -> open terminal -> pip install here-geocoding**

* pip install here-geocoding

Example
-------

Find the api key: https://platform.here.com/admin/apps/

.. code-block:: python
    
    from here_geocoding import geocoding

    api_key = 'YOUR API KEY'  # OK

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
    
    # Example 4
    # using as example the csv file from: https://github.com/geocommons/geocoder/blob/master/test/data/address-sample.csv
    d.geocode_excel(file_path='address-sample.xlsx', start_row=-1, end_row=20, address_column='address', bbox=None,
                    to_crs=None, export_file_name='test', export_file_type='csv')

    # Example 5
    d.geocode_excel(file_path='address-sample.xlsx', start_row=-1, end_row=20, address_column='address', bbox=None,
                    to_crs=None, export_file_name='test', export_file_type='geojson')

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
