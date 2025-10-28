from os import getenv

_MODE = getenv('MODE', 'development')

SEED = None if _MODE == 'production' else 42
