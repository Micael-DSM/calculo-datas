from datetime import date
from run import calcular_idade, dias_faltam, dias_passaram


# ---------- Testes de calcular_idade ----------

def test_idade_aniversario_ja_passou():
    assert calcular_idade(date(2000, 1, 10), date(2026, 10, 28)) == 26


def test_idade_aniversario_ainda_nao_chegou():
    assert calcular_idade(date(2000, 12, 25), date(2026, 10, 28)) == 25


def test_idade_aniversario_e_hoje():
    assert calcular_idade(date(2000, 10, 28), date(2026, 10, 28)) == 26


def test_idade_aniversario_e_amanha():
    assert calcular_idade(date(2000, 10, 29), date(2026, 10, 28)) == 25


def test_idade_nasceu_hoje():
    assert calcular_idade(date(2026, 10, 28), date(2026, 10, 28)) == 0


# ---------- Testes de dias_faltam ----------

def test_dias_faltam_ate_primeiro_de_novembro():
    assert dias_faltam(date(2026, 11, 1), date(2026, 10, 28)) == 4


def test_dias_faltam_mesmo_dia():
    assert dias_faltam(date(2026, 10, 28), date(2026, 10, 28)) == 0


def test_dias_faltam_ate_ano_novo():
    assert dias_faltam(date(2027, 1, 1), date(2026, 10, 28)) == 65

# ---------- Testes de dias_passaram ----------

def test_dias_passaram_no_mesmo_mes():
    assert dias_passaram(date(2026, 10, 1), date(2026, 10, 28)) == 27


def test_dias_passaram_mesmo_dia():
    assert dias_passaram(date(2026, 10, 28), date(2026, 10, 28)) == 0


def test_dias_passaram_um_ano():
    assert dias_passaram(date(2025, 10, 28), date(2026, 10, 28)) == 365