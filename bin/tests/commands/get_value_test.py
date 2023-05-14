from unittest import TestCase, main
from bin.commands import find_all_names
from typing import Generator

dict_ex = {'builds':
               [{'name': 'approach_important',
                 'tasks': ['map_gray_centaurs']},
                {'name': 'audience_stand',
                 'tasks': ['enable_fuchsia_fairies', 'read_blue_witches', 'upgrade_olive_gnomes']},
                {'name': 'time_alone', 'tasks': ['design_olive_cyclops', 'upgrade_lime_leprechauns']}]}
wrong_dict_ex = [1, 2, 3]


class FindNamesTest(TestCase):
    def test_right_file(self):
        self.assertEqual(find_all_names(dict_ex).__next__(), 'approach_important')

    def test_wrong_file(self):
        self.assertEqual(find_all_names(wrong_dict_ex).__next__(), None)


if __name__ == '__main__':
    main()
