"""Task 2: read cats information from a text file."""


def get_cats_info(path: str) -> list[dict]:
    """
    Read cats information from a file and return it as a list of dictionaries.

    Each line in the file must have the format: id,name,age
    Returns an empty list if the file is not found or contains invalid data.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []

            for line_number, line in enumerate(file, start=1):
                stripped_line = line.strip()
                if not stripped_line:
                    continue

                parts = stripped_line.split(",")
                if len(parts) != 3:
                    raise ValueError(
                        f"Invalid data format in line {line_number}: {stripped_line}"
                    )

                cat_id, name, age = (part.strip() for part in parts)
                cats.append({"id": cat_id, "name": name, "age": age})

            return cats

    except (FileNotFoundError, ValueError):
        return []


if __name__ == "__main__":
    cats = get_cats_info("cats.txt")
    print(cats)
