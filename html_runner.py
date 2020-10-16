from unittest import TestLoader, TestSuite, TextTestRunner
from dotenv import load_dotenv

import os
import webbrowser
from web.libs.HTMLTestRunner import HTMLTestRunner

from web.TestCollection import TEST_LIST


load_dotenv()


def main():
    loader = TestLoader()

    # collection of tests
    test_suite = TestSuite(
        [loader.loadTestsFromTestCase(test_case) for test_case in TEST_LIST])

    outfile = open("./test_report.html", "w")
    runner = HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Selenium Tests'
    )

    runner.run(test_suite)
    webbrowser.open(os.path.realpath('./test_report.html'))


if __name__ == '__main__':
    main()
