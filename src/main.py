"""
Application's entry point.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

from pathlib import Path
from algorithm import run_algorithm

import argparse

from configuration import Config, build_configurations

from data_savers import save_output

# =============================================================================================== #
# Functions
# =============================================================================================== #

def parse_arguments() -> Path:

    """
    Parses the application arguments.

    Returns:
        configurations_path (Path): Path where the configuration files reside.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to a .yml file or a directory containing .yml files."
    )

    args = parser.parse_args()
    return Path(args.config)

# =============================================================================================== #

def main():

    """
    Runs the application.
    """

    # ------------------------------------------------------------------------------------------- #
    # Arguments Parsing
    # ------------------------------------------------------------------------------------------- #

    path: Path = parse_arguments()

    # ------------------------------------------------------------------------------------------- #
    # Config Building
    # ------------------------------------------------------------------------------------------- #

    print("Building configurations...")

    configurations: list[Config] = build_configurations(path)

    print("All configurations have been built successfully.")

    # ------------------------------------------------------------------------------------------- #
    # Validations
    # ------------------------------------------------------------------------------------------- #

    if len(configurations) == 0:
        raise ValueError("\nERROR: No configurations.")

    # ------------------------------------------------------------------------------------------- #
    # Algorithm Execution
    # ------------------------------------------------------------------------------------------- #

    various_configurations: bool = len(configurations) > 1

    print(f"\nTotal configurations to execute: {len(configurations)}")

    if various_configurations:
        print("\nExecuting configurations...")

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

    print("\nPreparing results...")

    output_path = save_output(results)

    print(f"\nResults saved in folder {output_path}!")

# =============================================================================================== #
# Entry Point
# =============================================================================================== #

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(e)

# =============================================================================================== #
