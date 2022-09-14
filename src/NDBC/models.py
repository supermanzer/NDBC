"""Define data models

This file defines the common data models classes for NDBC 
"""

from dataclasses import dataclass
from typing import Union
import pandas


@dataclass
class DataPackage:
    """Define data package

    This class defines a custom data class for individual NDBC data packages.
    """

    data_type: str
    data: pandas.DataFrame
    metadata: dict


class DataStation:
    """Define basic data station class/object

    This class is focused on only the data properties necessary to identify a station
    """

    def __init__(self, station_id=False) -> None:
        if station_id:
            self.station_id = station_id

    def set_station_id(self, station_id: Union[int, str]) -> None:
        """Set ID for data station

        Provide a mechanism to set a station ID if an object was instantiated without one

        Args:
            station_id (Union[int, str]): The alphanumeric station identifier
        """
        self.station_id = station_id
