# -*- coding: utf-8 -*-
"""
DataBuoy class tests

Verifying the desired functionality of NDBC DataBuoy class methods.
"""
from datetime import datetime

from unittest import TestCase

from NDBC.NDBC import DataBuoy


class DataBuoyTests(TestCase):

    def setUp(self) -> None:
        self.DB = DataBuoy("46042")

    def test_instantiate_with_stationID(self):
        data_buoy = DataBuoy("46042")
        self.assertIsInstance(data_buoy, DataBuoy)

    def test_instantiate_without_stationID(self):
        data_buoy = DataBuoy()
        self.assertIsInstance(data_buoy, DataBuoy)

    def test_getstdmet(self):
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

    def test_badmetadata(self):
        with self.assertRaises(LookupError):
            db = DataBuoy()
            db.get_station_metadata()
