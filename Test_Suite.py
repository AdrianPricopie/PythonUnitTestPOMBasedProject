import unittest
from tests.LoginTest import TestLoginFeature
from tests.Search_user_test import TestSearchFeature

import HtmlTestRunner


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_de_rulat = unittest.TestSuite()
        test_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginFeature),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchFeature)
        ])
        # daca avem mai multe clase de test, rezultatele vor fi puse in acelasi raport de executie
        runner = HtmlTestRunner.HTMLTestRunner(

            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(test_de_rulat)
