import expensetracker


def test_table_5_to_15(capsys):
    result = expensetracker.table_5_to_15()
    captured = capsys.readouterr().out

    for num in range(5, 16):
        assert num in result
        assert result[num] == [num * j for j in range(1, 11)]
        assert f"Table of {num}" in captured
        assert f"{num} * 1 = {num}" in captured
        assert f"{num} * 10 = {num * 10}" in captured
