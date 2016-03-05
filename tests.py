import os
import unittest
import subprocess

WORKING_DIR = os.getcwd() + '/files/'


class TestFormFill(unittest.TestCase):
    def setUp(self):
        subprocess.call(['rm', '-rf', WORKING_DIR + 'base.pdf'])
        subprocess.call(['rm', '-rf', WORKING_DIR + 'filled.pdf'])
        subprocess.call(['cp', WORKING_DIR + 'master.pdf', WORKING_DIR +
                        'base.pdf'])
        subprocess.call(['cp', WORKING_DIR + 'master.pdf', WORKING_DIR +
                        'filled.pdf'])

    def test_form_fill(self):

