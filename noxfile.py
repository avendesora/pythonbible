from __future__ import annotations

import nox

PYTEST = "pytest"
COVERAGE = "coverage"


@nox.session(python=["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"])
def tests(session: nox.Session) -> None:
    session.install(PYTEST)
    session.run(PYTEST)


@nox.session(python=["3.11"])
def coverage(session: nox.Session) -> None:
    session.install("coverage[toml]", PYTEST)
    session.run(COVERAGE, "run", "-m", PYTEST)
    session.run(COVERAGE, "report", "--show-missing")
