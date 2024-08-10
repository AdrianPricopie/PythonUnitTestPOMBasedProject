import unittest
from Testing_resources.tests.LoginTest import TestLoginFeature
from Testing_resources.tests.Search_user_test import TestSearchFeature
from Testing_resources.tests.FilterProductTests import TestFilterFeature
import HtmlTestRunner


class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_de_rulat = unittest.TestSuite()
        test_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginFeature),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchFeature),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestFilterFeature)
        ])
        # daca avem mai multe clase de test, rezultatele vor fi puse in acelasi raport de executie
        runner = HtmlTestRunner.HTMLTestRunner(

            report_title='TestReport',
            combine_reports=True,
            report_name='Smoke Test Result'
        )

        runner.run(test_de_rulat)
