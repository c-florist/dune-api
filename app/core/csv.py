import csv
from pathlib import Path


def load_from_csv(file_path: Path, skip_header: bool = True) -> list[tuple[str | int | None, ...]]:
    """Loads data from a CSV file and returns a list of tuples."""
    data = []
    with open(file_path) as f:
        reader = csv.reader(f)

        if skip_header:
            _ = next(reader)

        for row in reader:
            processed_row = [None if item == "" else item for item in row]
            data.append(tuple(processed_row))

    if not data:
        raise ValueError(f"CSV file at path {file_path} is empty")

    return data
