from unittest import TestCase, main
from bin.commands import get_command


dict_ex = {'builds':
               [{'name': 'approach_important',
                 'tasks': ['map_gray_centaurs']},
                {'name': 'audience_stand',
                 'tasks': ['enable_fuchsia_fairies', 'read_blue_witches', 'upgrade_olive_gnomes']},
                {'name': 'time_alone', 'tasks': ['design_olive_cyclops', 'upgrade_lime_leprechauns']}]}
wrong_dict_ex = [1, 2, 3]


class FindKeysTest(TestCase):
    def test_right_file(self):
        self.assertEqual(get_command(dict_ex, 'approach_important', 'build'), None)
        self.assertEqual(get_command(dict_ex, 'approach_important', 'task'), None)
    def test_wrong_file(self):
        self.assertEqual(get_command(wrong_dict_ex, 'audience_stand', 'build'), None)
        self.assertEqual(get_command(wrong_dict_ex, 'audience_stand', 'task'), None)

    def test_wrong_key(self):
        with self.assertRaises(ValueError) as e:
            get_command(dict_ex, 'audience_stand', 'wrong_key')
        self.assertEqual('Unknown type spec. Must be task or build', e.exception.args[0])

    def test_wrong_name(self):
        self.assertEqual(get_command(dict_ex, 'wrong_name', 'build'), None)
        self.assertEqual(get_command(dict_ex, 'wrong_name', 'task'), None)

if __name__ == '__main__':
    main()
