from Exercises.practice import (
    collect_invalid_user,
    count_valid_user,
    has_required_fields,
    is_valid_user,
    normalize_name,
    is_valid_email,
    get_pass_fail_status,
    is_empty,
    count_file_types,
)


class TestPractice:
    def test_normalize_name(self):
        assert normalize_name("   john smith  ") == "John Smith"

    def test_valid_email(self):
        assert is_valid_email("john@example.com") is True

    def test_invalid_email(self):
        assert is_valid_email("john.example.com") is False

    def test_score_excellent(self):
        assert get_pass_fail_status(95) == "excellent"

    def test_score_pass(self):
        assert get_pass_fail_status(75) == "pass"

    def test_score_fail(self):
        assert get_pass_fail_status(40) == "fail"

    def test_empty_string(self):
        assert is_empty("") is True

    def test_spaces_only(self):
        assert is_empty(" ") is True

    def test_non_empty_string(self):
        assert is_empty("hello") is False

    def test_count_file_types(self):
        files = [
            "report.pdf",
            "image.png",
            "data.csv",
            "notes.txt",
            "photo.png",
            "summary.pdf",
        ]
        assert count_file_types(files) == {"pdf": 2, "png": 2, "csv": 1, "txt": 1}

    def test_has_required_fields(self):
        user = {"name": "John", "email": "john@example.com", "age": 30}
        assert has_required_fields(user) is True

    def test_has_required_fields_missing_email(self):
        user = {"name": "John", "age": 30}
        assert has_required_fields(user) is False

    def test_has_required_fields_empty_name(self):
        user = {"name": "", "email": "john@example.com", "age": 30}
        assert has_required_fields(user) is False

    def test_is_valid_user_data(self):
        user = {"name": "John", "email": "john@example.com", "age": 30}
        assert is_valid_user(user) is True

    def test_is_valid_user_invalid_email(self):
        user = {"name": "John", "email": "johnexample.com", "age": 30}
        assert is_valid_user(user) is False

    def test_is_valid_user_age_as_string(self):
        user = {"name": "John", "email": "john@example.com", "age": "30"}
        assert is_valid_user(user) is False

    def test_is_valid_user_negative_age(self):
        user = {"name": "John", "email": "john@example.com", "age": -10}
        assert is_valid_user(user) is False

    def test_cound_valid_user(self):
        user = {"name": "John", "email": "john@example.com", "age": 30}
        user2 = {"name": "Jane", "email": "jane@example.com", "age": 25}
        user3 = {"name": "", "email": "sara@example.com", "age": 22}
        assert count_valid_user([user, user2, user3]) == 2

    def test_collect_invalid_user(self):
        user = {"name": "John", "email": "john@example.com", "age": 30}
        user2 = {"name": "Sara", "email": "sara@example.com", "age": "22"}
        assert collect_invalid_user([user, user2]) == [user2]