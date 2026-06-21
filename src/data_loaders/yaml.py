"""
YAML loading algorithm.
"""

# =============================================================================================== #
# Imports
# =============================================================================================== #

import yaml

# =============================================================================================== #
# Function
# =============================================================================================== #

def load_config(path: str) -> any:

    """
    Loads a YAML configuration.
    
    Args:
        path (srt): Configuration path.

    Returns:
        stream (any): If the YAML file is valid, it returns its stream
    """

    with open(path, "r", encoding="utf-8") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise ValueError(
                f"UNEXPECTED ERROR: Could not read the YAML configuration: {exc}."
            ) from exc

# =============================================================================================== #
