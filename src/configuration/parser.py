"""
Docstring.
"""
def parse_enum(enum_cls, value: str):
    """
    Docstring.
    """
    try:
        return enum_cls(value)
    except ValueError as exc:
        raise ValueError(f"Valor inválido '{value}' para {enum_cls.__name__}") from exc
