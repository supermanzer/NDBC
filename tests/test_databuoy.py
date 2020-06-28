# -*- coding: utf-8 -*-
"""
DataBuoy class tests

Verifying the desired functionality of NDBC DataBuoy class methods.
"""
import os
import json

from datetime import datetime

from unittest import TestCase

from NDBC.NDBC import DataBuoy


class DataBuoyTests(TestCase):

    def setUp(self) -> None:
        self.station_id = '46042'
        self.DB = DataBuoy(self.station_id)

    def test_instantiate_with_stationID(self):
        data_buoy = DataBuoy("46042")
        self.assertIsInstance(data_buoy, DataBuoy)

    def test_instantiate_without_stationID(self):
        data_buoy = DataBuoy()
        self.assertIsInstance(data_buoy, DataBuoy)

    def test_get_stdmet(self):
        # Get the default (most current month of data)
        self.DB.get_stdmet()
        self.assertTrue(self.DB.data)

    def test_datetime_conversion_index(self):
        self.DB.get_stdmet(datetime_index=True)
        dt = self.DB.data['stdmet']['data'].iloc[1].name
        self.assertIsInstance(dt, datetime)

    def test_datetime_conversion_column(self):
        self.DB.get_stdmet()
        dt = self.DB.data['stdmet']['data'].iloc[1]['datetime']
        self.assertIsInstance(dt, datetime)

    def test_station_metadata(self):
        self.DB.get_station_metadata()
        self.assertTrue(self.DB.station_info)
        # Station 46042 has many attributes, let's make sure we got them all
        self.assertTrue(all([
            term in self.DB.station_info.keys()
            for term in [
                'lat', 'lon', 'Site elevation', 'Air temp height',
                'Anemometer height', 'Barometer elevation', 'Sea temp depth',
                'Water depth', 'Watch circle radius']
        ]))

    def test_bad_metadata(self):
        with self.assertRaises(LookupError):
            db = DataBuoy()
            db.get_station_metadata()

    def test_save_no_stdmet(self):
        filename = 'test_buoy.json'
        self.DB.save(filename=filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            station_json = f.read()
            self.assertIn('station_id', station_json)
            obj = json.loads(station_json)
            self.assertIsInstance(obj, dict)
        os.remove(filename)

    def test_save_with_stdmet(self):
        filename = 'test_buoy.json'
        self.DB.get_stdmet()
        self.DB.save(filename=filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            station_json = f.read()
            self.assertIn('station_id', station_json)
            obj = json.loads(station_json)
            self.assertIsInstance(obj, dict)
            self.assertIsInstance(obj['data']['stdmet'], dict)
            self.assertIn('data', obj['data']['stdmet'].keys())
        os.remove(filename)

    def test_save_and_load(self):
        filename = 'test_buoy.json'
        self.DB.save(filename)
        inst = DataBuoy.load(filename)
        for k in self.DB.__dict__.keys():
            self.assertTrue(hasattr(inst, k))

    def test_radial_search(self):
        self.DB.get_station_metadata()
        # For radial search, if no centroid (lat1, lon1) is provided AND the
        # instantiated DataBuoy object has defined lat & lon these will be
        # used to define the center of the circle

        # Fetch all buoy stations within a 50km radius
        near_stations = self.DB.station_search(
            search_type='radial', distance=50, uom='metric'
        )
        # We return a set to ensure we get unique station IDs
        self.assertIsInstance(near_stations, set)
        # We should return alphanumeric strings identifying stations
        for station_id in near_stations:
            # Test that we got a string
            self.assertIsInstance(station_id, str)
            # Test that we can instantiate new DataBuoy objects from the
            # station_id values returned (if any).
            test_db = DataBuoy(station_id)
            self.assertIsInstance(test_db, DataBuoy)

    def test_box_search(self):
        # Defining kwargs for box search
        kws = {
            'lat1': 36, 'lat2': 37, 'lon1': -120, 'lon2': -122,
            'search_type': 'box', 'obs_type': 'buoy'
        }
        box_stations = self.DB.station_search(**kws)
        self.assertIsInstance(box_stations, set)
        for station_id in box_stations:
            self.assertIsInstance(station_id, str)
            test_db = DataBuoy(station_id)
            self.assertIsInstance(test_db, DataBuoy)
