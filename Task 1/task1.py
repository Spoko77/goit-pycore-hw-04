def total_salary(path: str) -> tuple[int, float]:
    """
    Calculate the total and average salary from a file.

    Each line in the file must have the format: name,salary
    Returns (0, 0) if the file is empty, not found, or contains invalid data.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            salaries = []

            for line_number, line in enumerate(file, start=1):
                stripped_line = line.strip()
                if not stripped_line:
                    continue

                parts = stripped_line.split(",")
                if len(parts) != 2:
                    raise ValueError(
                        f"Invalid data format in line {line_number}: {stripped_line}"
                    )

                _, salary_text = parts
                salary = int(salary_text.strip())
                salaries.append(salary)

            if not salaries:
                return 0, 0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except (FileNotFoundError, ValueError):
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary.txt")
    print(f"Загальна сума: {total}, Середня: {average}")
