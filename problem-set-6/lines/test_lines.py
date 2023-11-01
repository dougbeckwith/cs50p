import lines


def test_empty_or_comment_lines():
    assert lines.is_empty_or_comment("# This is a comment\n") == True
    assert lines.is_empty_or_comment("   \n") == True
    assert lines.is_empty_or_comment("print('Hello, World!')\n") == False