""" Tests """
import os
from subprocess import getstatusoutput

PRG = './apob.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """
    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Usage """
    for flag in ['-h', '--help']:
        retval, out = getstatusoutput(f'{PRG} {flag}')
        assert retval == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_default_values():
    """ Test command line default values. """
    retval, out = getstatusoutput(f'{PRG}')
    assert retval == 0
    assert out.splitlines()[0] == 'TC: 166, HDLC: 34, TG: 188'


# --------------------------------------------------
def test_tc_flag():
    """ Test Total Cholesterol flag. """
    retval, out = getstatusoutput(f'{PRG} -tc 150')
    assert retval == 0
    assert out.splitlines()[0] == 'TC: 150, HDLC: 34, TG: 188'


# --------------------------------------------------
def test_hdlc_flag():
    """ Test High-Density Lipoprotein Cholesterol flag. """
    retval, out = getstatusoutput(f'{PRG} -hdlc 30')
    assert retval == 0
    assert out.splitlines()[0] == 'TC: 166, HDLC: 30, TG: 188'


# --------------------------------------------------
def test_tg_flag():
    """ Test triglycerides flag. """
    retval, out = getstatusoutput(f'{PRG} -tg 190')
    assert retval == 0
    assert out.splitlines()[0] == 'TC: 166, HDLC: 34, TG: 190'


# --------------------------------------------------
def test_not_integer_input():
    """ Tests for bad input. """
    retval, out = getstatusoutput(f'{PRG} -tg BAD_INPUT')
    assert retval == 2
    assert out == """usage: apob.py [-h] [-tc int] [-hdlc int] [-tg int]
apob.py: error: argument -tg/--triglycerides: invalid int value: 'BAD_INPUT'"""
