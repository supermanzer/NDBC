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
