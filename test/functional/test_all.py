from test_ls import *
from test_copy import *
from test_general import *
from test_rm import *
from test_mkdir import *
from xmlrunner import XMLTestRunner
import sys
import os

fname = 'test_results.xml'
if __name__ == '__main__':
    s=open(fname, 'w')
    unittest.main(testRunner=XMLTestRunner(stream=sys.stdout))
