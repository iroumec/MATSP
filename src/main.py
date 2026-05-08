"""
Application's entry point.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from pathlib import Path
from algorithm import run_algorithm

import argparse

from configuration import Config, build_config

from data_managers import (
    save_output,
    load_config,
)
from functions import assert_same_instance

# =============================================================================================== #
# Functions
# =============================================================================================== #

def parse_arguments() -> Path:

    """
    Parses the application arguments.

    Returns:
        configurations_path (Path): Path where the configurations files reside.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to a .yml file or a directory containing .yml files"
    )

    args = parser.parse_args()
    return Path(args.config)

# =============================================================================================== #

def build_configurations(path: Path) -> list[Config]:

    """
    Builds a list of valid configurations.

    Args:
        path (Path): Path with the YAML configuration files.

    Returns:
        configurations (List[Config]): Configuration objects.
    """

    configurations: list[Config] = []

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

    return configurations

# =============================================================================================== #

def main():

    """
    Runs the application.
    """

    # ------------------------------------------------------------------------------------------- #
    # Arguments Parsing
    # ------------------------------------------------------------------------------------------- #

    path = parse_arguments()

    # ------------------------------------------------------------------------------------------- #
    # Config Building
    # ------------------------------------------------------------------------------------------- #

    configurations = build_configurations(path)

    # ------------------------------------------------------------------------------------------- #
    # Validations
    # ------------------------------------------------------------------------------------------- #

    assert_same_instance(configurations)

    if len(configurations) == 0:
        raise ValueError("ERROR: No configurations.")

    # ------------------------------------------------------------------------------------------- #
    # Algorithm Execution
    # ------------------------------------------------------------------------------------------- #

    various_configurations: bool = len(configurations) > 1

    if various_configurations:
        print("Executing configurations...")

    results = []
    for index, configuration in enumerate(configurations):
        if various_configurations:
            print(f"\nExecuting configuration C{index+1}...")
        else:
            print("Executing configuration...")
        results.append(run_algorithm(configuration))
        if various_configurations:
            print(f"Configuration C{index+1} executed!")
        else:
            print("Configuration executed!")

    if various_configurations:
        print("\nAll configurations have been executed!")

    # ------------------------------------------------------------------------------------------- #
    # Output Saving
    # ------------------------------------------------------------------------------------------- #

    print("\nPreparing summary...")

    output_path = save_output(results)

    print(f"\nResults saved in folder {output_path}!")

# =============================================================================================== #
# Entry Point
# =============================================================================================== #

if __name__ == "__main__":
    main()

# =============================================================================================== #
