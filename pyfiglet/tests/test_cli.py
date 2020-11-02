import subprocess


def test_strip():
    # command = "%s/bin/tq %s/btq/tests/simple.toml ." % (root_dir, root_dir)
    command = "pyfiglet -f doh -s 0"
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
