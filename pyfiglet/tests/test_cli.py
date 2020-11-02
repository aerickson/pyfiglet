import os
import subprocess

import pytest


@pytest.fixture
# script working directory
def test_font_dir():
    swd = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(swd)


def test_strip():
    # command = "%s/bin/tq %s/btq/tests/simple.toml ." % (root_dir, root_dir)
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
    result = subprocess.run(command, shell=True, capture_output=True)
    assert result.stdout.decode() == expected


def test_strip(test_font_dir):
    # command = "%s/bin/tq %s/btq/tests/simple.toml ." % (root_dir, root_dir)
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
    result = subprocess.run(command, shell=True, capture_output=True)
    assert result.stdout.decode() == expected



def test_strip_strange_font():
    # command = "%s/bin/tq %s/btq/tests/simple.toml ." % (root_dir, root_dir)
    install_command = "pyfiglet -L %s/doh-odd " % test_font_dir
    subprocess.run(install_command, shell=True)

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
    result = subprocess.run(command, shell=True, capture_output=True)
    assert result.stdout.decode() == expected


# normalize is just strip with padding
def test_normalize():
    # command = "%s/bin/tq %s/btq/tests/simple.toml ." % (root_dir, root_dir)
    command = "pyfiglet -f doh -n 0"
    # print(command)
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
    result = subprocess.run(command, shell=True, capture_output=True)
    assert result.stdout.decode() == expected
