import io
import sys
from orderpizza import main


def test_order_calculation(monkeypatch, capsys):
    inputs = iter(["1", "2", "6"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr().out
    assert "Total Amount: ₹398" in captured
    assert "GST: ₹71.64" in captured
    assert "Final Amount: ₹469.64" in captured
