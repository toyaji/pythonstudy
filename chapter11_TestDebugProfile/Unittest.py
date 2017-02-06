# -*- coding: utf-8 -*-

import unittest

from chapter11_TestDebugProfile import DocString


# 단위 테스트를 철저하게 분석하려면 요런식으로 unittest 모듈 불러다가 해야함

class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        # 테스트 시작전 설정 작업 셋팅 가능
        pass

    def tearDown(self):
        # 테스트 이후 청소 작업 셋팅 가능
        pass

    def testsimpltstring(self):
        r = DocString.split('GOOG 100 490.50')
        self.assertEqual(r, ['GOOG', '100', '490.50'])   # assertEqual(x, y, [,msg]) x와 y가 다른 경우에 메시지 띄워줌

    def testtypeconvert(self):
        r = DocString.split('GOOG 100 490.50', [str, int, float])
        self.assertEqual(r, ['GOOG', 100, 490.5])

    def testdelimiter(self):
        r = DocString.split('GOOG,100,490.50', delimeter=',')
        self.assertEqual(r, ['GOOG', '100', '490.50'])

# 단위 테스트 실행
if __name__ == '__mein__':
    unittest.main()