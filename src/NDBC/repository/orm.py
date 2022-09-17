"""repository/orm.py

Defining the mapping between our data storage format(s) and domain models
"""

from ctypes import Union
import json
import pandas as pd
from NDBC.NDBC import DataBuoy

# the top level property where observation data is stored
OBSERVATIONS_KEY = "obsv"
# The key identifying actual measurement data for a given data package
DATA_KEY = "data"
# The key identifying metadata for a given data package
META_KEY = "meta"
# The default file string to be written
DEFAULT_FILE_STRING = "data_buoy_{station_id}.json"


class BuoyORM:
    """Mapping of data buoy data to file system data

    This ORM abstracts the methods of serializing DataBuoy
    classes to JSON and writing them to disk.
    """

    def serialize_dataframe(
        self, dataframe: pd.DataFrame, orient: str, date_format: str
    ) -> dict:
        """Return a pandas DataFrame as a JSON string

        Transform a pandas DataFrame into a JSON string.  Preserve the specific
        transformations applied (orient, date_format) as metadata to ensure
        we can de-serialize accurately.

        Args:
            dataframe (DataFrame): A pandas DataFrame with buoy data
            orient (str, optional): The orientation of the serialized JSON. Defaults to "records".
            date_format (str, optional): The formatting applied to datetime values. Defaults to "iso".

        Returns:
            dict: The serialized data and metadata
        """

        df_json = dataframe.to_json(orient=orient, date_format=date_format)
        return {"orient": orient, "date_format": date_format, "data_json": df_json}

    def serialize_buoy(self, db: DataBuoy, orient: str, date_format: str) -> str:
        """Serialize DataBuoy object

        Return a valid JSON string containing all DataBuoy properties.  DataFrames are not
        JSON serializable so each DataFrame instance needs to be converted to JSON.

        Args:
            db (DataBuoy): DataBuoy object to be serialized
            orient (str): DataFrame to JSON orientation.
            date_format (str): Date string format

        Returns:
            str: JSON representation of DataBuoy
        """
        buoy_data = {OBSERVATIONS_KEY: {}}
        for k, v in db.data.items():
            buoy_data[OBSERVATIONS_KEY][k][DATA_KEY] = self.serialize_dataframe(
                db=v.pop(DATA_KEY), orient=orient, date_format=date_format
            )
            buoy_data[OBSERVATIONS_KEY][k].update(v)
        buoy_data.update({k: v for k, v in db.__dict__.items() if k != DATA_KEY})
        return json.dumps(buoy_data)

    def save_to_file(
        self,
        db: DataBuoy,
        filename: Union[str, bool] = False,
        orient: str = "records",
        date_format: str = "iso",
    ) -> None:
        """Save DataBuoy state to file

        Write DataBuoy to `.json` file.

        Args:
            db (DataBuoy): DataBuoy object
            filename (Union[str, bool], optional): Filename to write to.
            orient (str, optional): pandas DataFrame orientation to be used when converting to JSON. Defaults to "records".
            date_format (str, optional): Format used to convert datetime to strings. Defaults to "iso".
        """
        file_name = (
            filename
            if filename
            else DEFAULT_FILE_STRING.format(station_id=db.station_id)
        )
        buoy_str = self.serialize_buoy(db, orient, date_format)
        with open(file_name, "w+") as f:
            f.write(buoy_str)

    def load_from_file(self, filename):
        """Instantiate a DataBuoy class from a JSON file

        Loads a

        Args:
            filename (str): _description_
        """
        if not filename.endswith(".json"):
            raise ValueError(
                "Incorrect file provided.  DataBuoy class can only be instantiated from JSON files"
            )

        data_str = open(filename, "r").read()
        data_obj = json.loads(data_str)
        for data_type in data_obj.get(OBSERVATIONS_KEY, {}).keys():
            orient = data_obj[OBSERVATIONS_KEY][data_type][META_KEY].get(
                "orient", "records"
            )
            data_obj[OBSERVATIONS_KEY][data_type][DATA_KEY] = pd.read_json(
                path_or_buf=data_obj[OBSERVATIONS_KEY][data_type][DATA_KEY],
                orient=orient,
            )
        return data_obj
