from unittest import TestCase, main
import pathlib

from bin.directories import get_file_data

right_path = pathlib.Path(r'C:\Users\Vladimir\Documents\python\saber_test\bin', 'tasks.yaml')

wrong_path = pathlib.Path(pathlib.Path(__file__).parent, 'awfawfa')


class GetFileTest(TestCase):
    def test_right_path(self):
        self.assertEqual(type(get_file_data(right_path)), dict)

    def test_wrong_path(self):
        with self.assertRaises(SystemExit) as e:
            get_file_data(wrong_path)
        self.assertEqual(e.exception.code, 1)
