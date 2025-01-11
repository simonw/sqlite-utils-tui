from click.testing import CliRunner
from sqlite_utils.cli import cli
import re


def test_default_help():
    result = CliRunner().invoke(cli, ["--help"])
    assert re.search(r"tui\s+Open terminal UI", result.output) is not None
