#! /usr/bin/env python
#
# Scans the .test files on the command line and parses each, running
# the tests listed.  Results are printed out.
# 

import sys
import os
import string


def usage_exit():
    print "Usage: \n" + sys.argv[0] + " testfile"
    sys.exit()

def run_tests(test_name, config_name, input_name, expected_name):
    # print "Test:   " + test_name
    # print "Config: " + config_name
    # print "Input:  " + input_name
    # print "Output: " + expected_name
    cmd = "../src/uncrustify -L255 -c config/" + config_name + " -f input/" + input_name + " > results/" + test_name + ".out"
    a = os.system(cmd)
    if a != 0:
        print "FAILED: " + test_name
        return
    b = os.system("diff -u results/" + test_name + ".out output/" + expected_name + " > /dev/null")
    if b != 0:
        print "MISMATCH: " + test_name
        return
    print "PASSED: " + test_name

def process_test_file(filename):
    fd = open(filename, "r")
    if fd == None:
        print "Unable to open " + filename
        return
    print "Processing " + filename
    for line in fd:
        line = string.rstrip(string.lstrip(line))
        parts = string.rsplit(line)
        if (len(parts) < 4) or (parts[0][0] == '#'):
            continue
        run_tests(parts[0], parts[1], parts[2], parts[3])


#
# entry point
# 

if len(sys.argv) < 2:
    usage_exit()

for item in sys.argv[1:]:
    process_test_file(item)

sys.exit()

