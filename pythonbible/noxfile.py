from __future__ import annotations

import nox

nox.options.default_venv_backend = "uv"


@nox.session(python=["3.10", "3.11", "3.12", "3.13", "3.14"])
def tests(session: nox.Session) -> None:
    session.run("uv", "sync", "--active")
    session.run("uv", "sync", "--active", "--group", "test")
    session.run("uv", "run", "--active", "pytest")


@nox.session(python=["3.13"])
def coverage(session: nox.Session) -> None:
    session.run("uv", "sync", "--active")
    session.run("uv", "sync", "--active", "--group", "test")
    session.run("uv", "run", "--active", "coverage", "run", "-m", "pytest")
    session.run("uv", "run", "--active", "coverage", "report", "--show-missing")
