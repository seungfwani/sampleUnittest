import unittest
import os
import xmlrunner

def custom_function(file_name):
    with open(file_name, 'rt') as f:
        return sum(1 for _ in f)

class CustomTests(unittest.TestCase):

    def setUp(self):
        print('\nsetUp')
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
                안녕하세요. 
                unittest 중입니다.
                감사합니다.
                """.strip())

    def tearDown(self):
        print('\ntearDown')
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 4)
 
    def test_no_file(self):
        with self.assertRaises(IOError):
            custom_function('abc.txt')

if __name__=='__main__':
    with open('./unittest_results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
