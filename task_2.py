import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # [-+]?            — необов’язковий знак “+” або “−”
    # (?:              — початок групи без збереження
    #     \d * \.\d+   — 0 або більше цифр, потім крапка, потім хоча б одна цифра (наприклад, .5 або 0.5)
    #   | \d +\.\d *   — 1 або більше цифр, потім крапка, потім 0 або більше цифр(наприклад, 5. або 5.0)
    #   | \d +         — ціле число
    # )
    pattern = r'\b[-+]?(?:\d*\.\d+|\d+\.\d*|\d+)\b'
    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))
