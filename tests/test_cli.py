"""Smoke tests for the ledgercli Typer app."""
from typer.testing import CliRunner

from cli import app

runner = CliRunner()

def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Practical Ledger Framework" in result.output 