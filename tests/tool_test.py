# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():

    assert haversine(0.0, 0.0, 0.0, 0.0)==0
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == 70.00789153218594

