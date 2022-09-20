"""
Catalog search functionality
"""

from pathlib import Path
from typing import Union, List, Tuple, Dict, Any

from pandas import Series
from geopandas import GeoDataFrame
from shapely.geometry import Polygon
from geojson import Feature, FeatureCollection
from tqdm import tqdm

from up42.auth import Auth
from up42.order import Order
from up42.utils import (
    get_logger,
    any_vector_to_fc,
    fc_to_query_geometry,
    format_time_period,
)

logger = get_logger(__name__)


# pylint: disable=duplicate-code
class Tasking():
    """
    The Tasking class enables access to the UP42 tasking functionality.

    Use tasking:
    ```python
    tasking = up42.initialize_tasking()
    ```
    """

    def __init__(self, auth: Auth):
        self.auth = auth

    def __repr__(self):
        return f"Tasking(auth={self.auth})"