from unittest import TestCase, main
from bin.directories import get_file_path

right_path = r'C:\Users\Vladimir\Documents\python\saber_test\bin\123'
wrong_path = r'C:\Users\Vladimir\Documents\python\12'


class FindNamesTest(TestCase):
    def test_right_file(self):
        self.assertEqual(get_file_path(right_path), None)

    def test_wrong_file(self):
        self.assertEqual(get_file_path(wrong_path), None)


if __name__ == '__main__':
    main()
