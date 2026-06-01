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


def has_required_fields(user: dict) -> bool:
    required_fields = ["name", "email", "age"]
    for field in required_fields:
        if field not in user:
            return False
        if user[field] == "":
            return False
    return True


def is_valid_user(user: dict) -> bool:
    if not has_required_fields(user):
        return False
    if "@" not in user["email"]:
        return False
    if not isinstance(user["age"], int):
        return False
    if user["age"] <= 0:
        return False
    return True


def count_valid_user(users: list[dict]) -> int:
    valid_count = 0
    for user in users:
        if is_valid_user(user):
            valid_count += 1
    return valid_count


def collect_invalid_user(users: list[dict]) -> list[dict]:
    invalid_users = []
    for user in users:
        if not is_valid_user(user):
            invalid_users.append(user)
    return invalid_users


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
