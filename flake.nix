{
  description = "Projet3A";

  nixConfig = {
    extra-substituters = [
      "https://nix-community.cachix.org"
      "https://vrheadcache.cachix.org"
    ];
    extra-trusted-public-keys = [
      "nix-community.cachix.org-1:mB9FSh9qf2dCimDSUo8Zy7bkq5CX+/rkCWyvRCYg3Fs="
      "vrheadcache.cachix.org-1:v0XsYmHf9iA9ZtIsdc+Bjyqtzx6DO5f/fiXq2Lq+blA="
    ];
  };

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        config = {
          allowUnfree = true;
        };
      };

      python = pkgs.python312;

      pythonWithPackages = python.withPackages (ps:
        with ps; [
          pip
          opencv-python-headless
        ]);
    in {
      devShells.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          python312Packages.python-lsp-server
          black
          pythonWithPackages
        ];

        env.LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
          pkgs.stdenv.cc.cc.lib
          pkgs.libz
        ];

        shellHook = ''

          if [ ! -d .venv ]; then
            echo "Creating virtualenv with ultralytics ..."
            ${python.interpreter} -m venv .venv
            source .venv/bin/activate
            pip install --upgrade pip
            pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
            pip install ultralytics
          else
            source .venv/bin/activate
          fi

          echo "Virtualenv activated. 'ultralytics' installed with."
        '';
      };
    });
}
