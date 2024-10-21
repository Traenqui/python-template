import nox

locations = "src", "tests", "noxfile.py"
python_versions = ["3.12"]
nox.options.sessions = "lint", "tests"


@nox.session(python=python_versions)
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python=python_versions)
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=python_versions[0])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
