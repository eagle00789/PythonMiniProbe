#!/usr/bin/env python

from nose.tools import *
import sensors.nmap

def test_nmap_get_kind():
    test_nmap = nmap.NMAP()
    assert_equal(test_nmap.get_kind(), 'mpnmap')