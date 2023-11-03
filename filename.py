import random


def rename(keyword: str) -> str:
    file_name = keyword.strip().lower().replace(" ", "-")
    return f"{file_name}-{random.randint(100, 1000)}"
