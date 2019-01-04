import unittest
import os

def custom_function(file_name):
    """ simple count file lines """
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
        # 테스트 종료 후 파일 삭제
        print('\ntearDown')
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        # 단순 실행 여부 판단
        custom_function(self.file_name)

    def test_line_count(self):
        self.assertEqual(custom_function(self.file_name), 3)

    def test_no_file(self):
        with self.assertRaises(IOError):
            custom_function('abc.txt')

if __name__ == '__main__':
    unittest.main()
