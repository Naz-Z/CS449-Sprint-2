import unittest
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python run_tests.py [TestSimpleGame|TestGeneralGame|all]")
        sys.exit(1)
    
    test_type = sys.argv[1]
    
    if test_type == 'TestSimpleGame':
        from test_simple_game import TestSimpleGame
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleGame)
    elif test_type == 'all':
        from test_base_game import TestBaseGame
        from test_simple_game import TestSimpleGame
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestBaseGame))
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSimpleGame))
    else:
        print(f"Unknown test type: {test_type}")
        sys.exit(1)
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    sys.exit(not result.wasSuccessful())
