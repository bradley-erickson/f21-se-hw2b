from pathlib import Path
import sys
import unittest

path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

import code


class TestSum(unittest.TestCase):

    def test_call_api(self):
        self.assertEqual(code.call_api(), 200, "Should be 200")


if __name__ == '__main__':
    unittest.main()
