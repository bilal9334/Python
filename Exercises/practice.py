def normalize_name(name: str) -> str:
    return name.strip().title()


def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email


def get_pass_fail_status(score: int) -> str:
    if score >= 90:
        return "excellent"
    elif score >= 60:
        return "pass"
    return "fail"


def count_errors(log_lines: list[str]) -> int:
    error_count = 0
    for line in log_lines:
        if "ERROR" in line:
            error_count += 1
    return error_count


def is_empty(value: str) -> bool:
    if value.strip() == "" or value.strip() == " ":
        return True
    return False


def count_file_types(file_names: list[str]) -> dict[str, int]:
    result = {}
    for file_name in file_names:
        extension = file_name.split(".")[-1].lower()
        result[extension] = result.get(extension, 0) + 1
    return result


files = ["report.pdf", "image.png", "data.csv", "notes.txt", "photo.png", "summary.pdf"]

print(count_file_types(files))


print(normalize_name("   john smith  "))
print(is_valid_email("john@example.com"))
print(get_pass_fail_status(95))
print(get_pass_fail_status(75))
print(get_pass_fail_status(40))
print(count_errors(["INFO started", "ERROR: failed", "ERROR timeout"]))
print(is_empty(""))
print(is_empty(" "))
print(is_empty("hello"))
