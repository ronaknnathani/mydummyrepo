#!/bin/python

import pytest
from src.adder import adder

def test_adder():
  assert adder(2, 2) == 4

def test_adder():
  assert adder(2, 3) == 5

def test_adder():
  assert adder(2, 4) == 6

def test_adder():
  assert adder(2, 5) == 7

