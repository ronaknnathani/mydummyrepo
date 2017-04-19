#!/bin/python

import pytest
from src.adder import adder

def test_adder():
  assert adder(2, 2) == 4

