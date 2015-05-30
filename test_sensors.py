#!/usr/bin/env python

from nose.tools import *
from sensors import nmap,adns,apt,cpuload,cputemp

def test_nmap_get_kind():
    """Check nmap returns the correct kind"""
    test_nmap = nmap.NMAP()
    assert_equal(test_nmap.get_kind(), 'mpnmap')

def test_nmap_icmp_echo_request():
    """Check nmap const ICMP_ECHO_REQUEST is set correct"""
    test_nmap = nmap.NMAP()
    assert_equal(test_nmap.ICMP_ECHO_REQUEST, 8)

def test_nmap_dec2bin():
    """Check nmap dec2bin results """
    test_nmap = nmap.NMAP()
    assert_equal(test_nmap.dec2bin(255,8),'11111111')
    assert_equal(test_nmap.dec2bin(254,8),'11111110')
    assert_equal(test_nmap.dec2bin(128,8),'10000000')
    assert_equal(test_nmap.dec2bin(127,8),'01111111')
    assert_equal(test_nmap.dec2bin(0,8),'00000000')

def test_nmap_ip2bin():
    """Check nmap ip2bin results """
    test_nmap = nmap.NMAP()
    assert_equal(test_nmap.ip2bin('255.255.255.255'),'11111111111111111111111111111111')
    assert_equal(test_nmap.ip2bin('254.254.254.254'),'11111110111111101111111011111110')
    assert_equal(test_nmap.ip2bin('128.128.128.128'),'10000000100000001000000010000000')
    assert_equal(test_nmap.ip2bin('127.127.127.127'),'01111111011111110111111101111111')
    assert_equal(test_nmap.ip2bin('0.0.0.0'),'00000000000000000000000000000000')

def test_adns_get_kind():
    """Check dns returns the correct kind"""
    test_adns = adns.aDNS()
    assert_equal(test_adns.get_kind(), 'mpdns')

def test_apt_get_kind():
    """Check apt returns the correct kind"""
    test_apt = apt.APT()
    assert_equal(test_apt.get_kind(), 'mpapt')

def test_cpuload_get_kind():
    """Check cpuload returns the correct kind"""
    test_cpuload = cpuload.CPULoad()
    assert_equal(test_cpuload.get_kind(), 'mpcpuload')

def test_cputemp_get_kind():
    """Check cputemp returns the correct kind"""
    test_cputemp = cputemp.CPUTemp()
    assert_equal(test_cputemp.get_kind(), 'mpcputemp')
