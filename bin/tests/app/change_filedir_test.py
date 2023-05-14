from unittest import TestCase, main
from bin.app import cli
from click.testing import CliRunner

class ChangeFileDir(TestCase):
    def test_right_params(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['cfd', r'C:\Users\Vladimir\Documents\python\saber_test\bin\123'])
        self.assertEqual(result.exit_code, 0)

    def test_wrong_params_1(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['cfd', r'C:\Users\Vladimir\Documents\python\saber_test\123\123'])
        self.assertEqual(result.exit_code, 2)


if __name__ == '__main__':
    main()
