import trogon
import sqlite_utils


@sqlite_utils.hookimpl
def register_commands(cli):
    trogon.tui(help="Open terminal UI")(cli)
