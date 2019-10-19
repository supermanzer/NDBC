# -*- coding: utf-8 -*-
"""
DataBuoy class tests

Verifying the desired functionality of NDBC DataBuoy class methods.
"""
from datetime import datetime

from unittest import TestCase

from NDBC.NDBC import DataBuoy


class DataBuoyTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.DB = DataBuoy(station_id="46042")

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

    def test_datetime_conversion(self):
        self.DB.get_stdmet()
        dt = self.DB.data[1].index.values
        self.assertIsInstance(dt, datetime)

    def test_station_metadata(self):
        self.assertTrue(self.DB.station_info)
