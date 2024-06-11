{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.poetry
  ];

  shellHook = ''
    python3.11 -m venv .venv
    source .venv/bin/activate
    poetry install
    playwright install

    export PYTHONPATH=$(pwd)
  '';
}

