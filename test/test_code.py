from pathlib import Path
import sys

path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

import code


def test_call_api():
    assert code.call_api() == 200


if __name__ == '__main__':
    test_call_api()
