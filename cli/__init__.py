"""Ledger CLI package

Current status: skeleton placeholder. Implements an empty Typer application so
CI and tests have an entrypoint. Real commands will be added in task 0.8.
"""
from __future__ import annotations

import typer

app = typer.Typer(help="Command-line interface for the Practical Ledger Framework.")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """Base command. Shows help when no sub-command is given."""
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help()) 