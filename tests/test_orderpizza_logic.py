from unittest.mock import patch
import orderpizza


def test_order_calculation(capsys):
    inputs = ["1", "2", "6"]
    with patch("builtins.input", side_effect=inputs):
        orderpizza.main()
    
    captured = capsys.readouterr().out
    assert "Margherita Pizza x 2 = ₹398" in captured
    assert "Total Amount: ₹398" in captured
    assert "GST: ₹71.64" in captured
    assert "Final Amount: ₹469.64" in captured
