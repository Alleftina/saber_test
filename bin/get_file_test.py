from unittest import TestCase, main
from bin.main import get_file
import pathlib

right_path = pathlib.Path(pathlib.Path(__file__).parent, 'tasks.yaml')
wrong_path = pathlib.Path(pathlib.Path(__file__).parent, 'awfawfa')

class GetFileTest(TestCase):
    def test_right_path(self):
        self.assertEqual(type(get_file(right_path)), dict)

    def test_wrong_path(self):
        with self.assertRaises(SystemExit) as e:
            get_file(wrong_path)
        self.assertEqual(e.exception.code, 1)


