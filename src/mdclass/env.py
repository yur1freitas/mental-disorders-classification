from os import getenv

# Variável de Ambiente que indica se a aplicação está em modo de desenvolvimento ou produção
_MODE = getenv('MODE', 'development')

SEED: int | None = None if _MODE == 'production' else 42
"""
Variável Global que define a Seed (random_state) sob determinado tipo de modo de aplicação
"""
