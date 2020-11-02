import os
import subprocess

import pytest


@pytest.fixture
# script working directory
def test_font_dir():
    swd = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(swd)


def test_strip():
    command = "pyfiglet -f doh -s 0"
    expected = '''\
     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0 000 0:::::0
0:::::0 000 0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000
'''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    assert result.stdout.decode() == expected
    assert result.returncode == 0


def test_strip():
    command = "pyfiglet -f doh -s 0"
    expected = '''\
     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0 000 0:::::0
0:::::0 000 0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000
'''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    assert result.stdout.decode() == expected
    assert result.returncode == 0


def test_strip_strange_font(test_font_dir):
    install_command = "pyfiglet -L %s/doh-odd.flf " % test_font_dir
    subprocess.run(install_command, shell=True, check=True)

    command = "pyfiglet -f doh-odd -s 0"
    expected = '''\
     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
                   
0:::::0     0:::::0
                   
0:::::0 000 0:::::0
                   
0:::::0 000 0:::::0
                   
0:::::0     0:::::0
                   
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000
'''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    assert result.stdout.decode() == expected
    assert result.returncode == 0


# normalize is just strip with padding
def test_normalize():
    command = "pyfiglet -f doh -n 0"
    expected = '''\

     000000000     
   00:::::::::00   
 00:::::::::::::00 
0:::::::000:::::::0
0::::::0   0::::::0
0:::::0     0:::::0
0:::::0     0:::::0
0:::::0 000 0:::::0
0:::::0 000 0:::::0
0:::::0     0:::::0
0:::::0     0:::::0
0::::::0   0::::::0
0:::::::000:::::::0
 00:::::::::::::00 
   00:::::::::00   
     000000000

'''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    assert result.stdout.decode() == expected
    assert result.returncode == 0
