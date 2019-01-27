#!/usr/bin/python3
from __future__ import print_function
import unittest
import os
import sys


class Test_files(unittest.TestCase):

    def __init__(self, testname='test_firstline' ,args=[__name__,"."]):
        super().__init__(testname)
        self._loc = args[1]

    def setUp(self):
        self._files = [py for py in os.listdir(self._loc) if ".py" in py]
        if len(self._files) == 0:
            print("Error: No python files where found")
            sys.exit(1)

    def test_firstline(self):
        for f_name in self._files:
            with open(self._loc +'/'+ f_name) as f:
                self.assertEqual(f.readline(), '#!/usr/bin/python3\n')
                f.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    if len(sys.argv) > 1 :
        suite.addTest(Test_files('test_firstline', sys.argv))
    else:
        suite.addTest(Test_files('test_firstline'))

    unittest.TextTestRunner(verbosity=2).run(suite)
