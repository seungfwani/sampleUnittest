import unittest
import os,sys
import xmlrunner
import customClass as cust

class CustomTests(unittest.TestCase):

    def setUp(self):
        # test전에 구조 생성
        print('setUp')
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
                안녕하세요. 
                unittest 중입니다.
                감사합니다.
                """.strip())

    def tearDown(self):
        # 테스트 종료 후 파일 삭제
        print('tearDown')
        try:
            os.remove(self.file_name)
        except:
            pass

    def test_runs(self):
        # 단순 실행 여부 판단
        cust.custom_function(self.file_name)

    def test_line_count(self):
        # check line count
        self.assertEqual(cust.custom_function(self.file_name), 3)

    def test_no_file(self):
        # 자이건 어떠냐
        # 이거도 해봐
        # 한번더 푸시
        # 제발 해봐
        # 한번더
        with self.assertRaises(IOError):
            cust.custom_function('abc.txt')

if __name__ == '__main__':
    print(os.path.abspath( __file__ ).split('\\')[-1].split('.')[0])
    print(sys._getframe().f_code.co_filename.split('.')[0])
    # with open('./QualityReports/unittest_results.xml', 'wb') as output:
    #     unittest.main(
    #         testRunner=xmlrunner.XMLTestRunner(output=output),
    #         failfast=False, buffer=False, catchbreak=False)
