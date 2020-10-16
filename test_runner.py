from unittest import TestLoader, TestSuite, TextTestRunner
from dotenv import load_dotenv

from web.TestCollection import TEST_LIST

load_dotenv()


def main():
    loader = TestLoader()

    # collection of tests
    test_suite = TestSuite(
        [loader.loadTestsFromTestCase(test_case) for test_case in TEST_LIST])

    # Show text results
    runner = TextTestRunner(verbosity=2)

    runner.run(test_suite)


if __name__ == '__main__':
    main()
