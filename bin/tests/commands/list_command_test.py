from unittest import TestCase, main
from bin.commands import list_command

dict_ex = {'builds':
               [{'name': 'approach_important',
                 'tasks': ['map_gray_centaurs']},
                {'name': 'audience_stand',
                 'tasks': ['enable_fuchsia_fairies', 'read_blue_witches', 'upgrade_olive_gnomes']},
                {'name': 'time_alone', 'tasks': ['design_olive_cyclops', 'upgrade_lime_leprechauns']}]}
wrong_dict_ex = [1, 2, 3]


class FindKeysTest(TestCase):
    def test_right_file(self):
        self.assertEqual(list_command(dict_ex, 'builds'), None)

    def test_wrong_file(self):
        self.assertEqual(list_command(wrong_dict_ex, 'builds'), None)



