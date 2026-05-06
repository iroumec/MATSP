"""
Application's entry point.
"""

from pathlib import Path
from algorithm import run_algorithm

import argparse

from configuration import build_config

from data_managers import (
    save_output,
    load_config,
)

def process_config(config_path: Path):
    """
    Docstring.
    """
    config = build_config(load_config(str(config_path)))
    return run_algorithm(config)

def main():
    """
    Docstring
    """

    # ------------------------------------------------------------------------------------------- #
    # Arguments Parsing
    # ------------------------------------------------------------------------------------------- #

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to a .yml file or a directory containing .yml files"
    )

    args = parser.parse_args()
    path = Path(args.config)

    # ------------------------------------------------------------------------------------------- #
    # Config Building
    # ------------------------------------------------------------------------------------------- #

    configurations = []

    # Just one file.
    if path.is_file():
        configurations.append(build_config(load_config(str(path))))

    # A directory with one or more paths.
    elif path.is_dir():
        # Only .yml and .yaml files.
        files = sorted([
            p for p in path.iterdir()
            if p.suffix in (".yml", ".yaml")
        ])

        if not files:
            raise ValueError("No .yml or .yaml files found in directory")

        for file in files:
            configurations.append(build_config(load_config(str(file))))

    else:
        raise ValueError("Invalid path: not a file or directory")

    # ------------------------------------------------------------------------------------------- #
    # Algorithm Execution
    # ------------------------------------------------------------------------------------------- #

    results = []
    for configuration in configurations:
        results.append(run_algorithm(configuration))

    # ------------------------------------------------------------------------------------------- #
    # Output Saving
    # ------------------------------------------------------------------------------------------- #

    output_path = save_output(results)

    print(f"Results saved in folder {output_path}!")

if __name__ == "__main__":
    main()
