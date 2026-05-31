from Exercises.practice import normalize_name, is_valid_email, get_pass_fail_status, is_empty, count_file_types


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
        files = ["report.pdf", "image.png", "data.csv", "notes.txt", "photo.png", "summary.pdf"]
        assert count_file_types(files) == {"pdf": 2, "png": 2, "csv": 1, "txt": 1}