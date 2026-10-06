from analyzer import analyze_password

def test_weak_common_password():
    res = analyze_password("password123")
    assert res["is_common"] is True
    assert res["classification"] == "VERY WEAK"
    assert res["score"] == 0

def test_keyboard_pattern():
    res = analyze_password("qwertyuiop1234")
    assert res["keyboard_pattern"] is True
    assert res["score"] < 50

def test_strong_passphrase():
    res = analyze_password("correct-horse-battery-staple-99!")
    assert res["is_common"] is False
    assert res["classification"] in ["STRONG", "VERY STRONG"]
    assert res["score"] >= 80

def test_personal_context_warning():
    res = analyze_password("JohnRover2024!", context_words=["John", "Rover"])
    assert res["personal_match"] > 0
    assert res["score"] < 80
