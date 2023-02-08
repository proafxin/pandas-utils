"""Specify variables for all tests"""

from io import StringIO

import pandas as pd
import pytest
import requests


@pytest.fixture(scope="function")
def data() -> pd.DataFrame:
    """Use this data for all the tests

    :return: Pandas dataframe of cities.
    :rtype: ``pd.DataFrame``
    """

    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv"
    response: requests.Response = requests.get(url, timeout=20)

    assert response.status_code == requests.codes.ok
    csv_data = pd.read_csv(StringIO(response.content.decode()))

    return csv_data
