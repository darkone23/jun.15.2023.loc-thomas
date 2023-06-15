{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [ 
    pkgs.git
    pkgs.just
    pkgs.python3Packages.virtualenv
    pkgs.python3Packages.python-lsp-server
    pkgs.python3Packages.certifi
    pkgs.python3Packages.urllib3
    pkgs.python3Packages.idna
    pkgs.python3Packages.charset-normalizer
    pkgs.python3Packages.requests
    pkgs.python3Packages.uvicorn
    pkgs.python3Packages.anyio
    pkgs.python3Packages.sniffio
    pkgs.python3Packages.starlette
    pkgs.python3Packages.rich
  ];

  # https://devenv.sh/scripts/
  scripts.hello.exec = "echo hello from $GREET";

  enterShell = ''
    hello
    git --version
  '';

  # https://devenv.sh/languages/
  languages.nix.enable = true;
  languages.python.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  # pre-commit.hooks.shellcheck.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";

  # See full reference at https://devenv.sh/reference/options/
}
