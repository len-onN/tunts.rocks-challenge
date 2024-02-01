from app import get_average, calculate_final_grade, determine_situation


def test_get_average():
    assert get_average(80, 90, 70) == 8
    assert get_average(50, 60, 75) == 7


def test_calculate_final_grade():
    assert calculate_final_grade(4) == 0
    assert calculate_final_grade(6) == 4
    assert calculate_final_grade(8) == 0


def test_determine_situation():
    assert determine_situation(20, 8) == ("Reprovado por Falta", 0)
    assert determine_situation(10, 4) == ("Reprovado por Nota", 0)
    assert determine_situation(5, 6) == ("Exame Final", 4)
    assert determine_situation(0, 9) == ("Aprovado", 0)
