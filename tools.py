from crewai.tools import tool


@tool("Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression.
    Example: 25 * 4
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)

    except Exception:
        return "I could not calculate that expression."
