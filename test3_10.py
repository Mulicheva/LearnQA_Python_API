class TestLesson3Ex10:
    def test_check_phrase(self):
        phrase = input("Set a phrase: ")
        len_phrase =len(phrase)
        assert len_phrase < 15, "Length of phrase more or equal than 15 symbols"