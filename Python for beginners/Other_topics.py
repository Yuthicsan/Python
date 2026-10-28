"""
Map, Filter, Reduce 
Decorators
Docstrings
Annotations
Exceptions 
"""


from functools import wraps


def log_call(func):
    """Log when a function is called."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


@log_call
def analyze_marks(marks: list[int]) -> dict[str, int | list[int]]:
    """
    Analyze student marks.

    Args:
        marks: A list of integer marks.

    Returns:
        A dictionary containing passed marks and their total.
    """
    passed_marks = list(filter(lambda mark: mark >= 40, marks))
    total = sum(map(lambda mark: mark, passed_marks))

    return {
        "passed_marks": passed_marks,
        "total": total
    }


try:
    marks = [int(value) for value in input(
        "Enter marks separated by spaces: "
    ).split()]

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")

    report = analyze_marks(marks)
    print(report)

except ValueError as error:
    print("Invalid input:", error)