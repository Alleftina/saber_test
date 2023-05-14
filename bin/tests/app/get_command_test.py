from unittest import TestCase, main
from bin.app import cli
from click.testing import CliRunner

dict_ex = {'builds':
               [{'name': 'approach_important',
                 'tasks': ['map_gray_centaurs']},
                {'name': 'audience_stand',
                 'tasks': ['enable_fuchsia_fairies', 'read_blue_witches', 'upgrade_olive_gnomes']},
                {'name': 'time_alone', 'tasks': ['design_olive_cyclops', 'upgrade_lime_leprechauns']}]}
wrong_dict_ex = [1, 2, 3]


class ListCommandTest(TestCase):
    def test_right_params_builds(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['get', 'builds', 'approach_important'])
        self.assertEqual(result.exit_code, 0)

    def test_right_params_task(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['get', 'tasks', 'approach_important'])
        self.assertEqual(result.exit_code, 0)

    def test_wrong_params_1(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['get', 'wrong_params', 'wrwar'])
        self.assertEqual(result.exit_code, 0)


if __name__ == '__main__':
    main()
