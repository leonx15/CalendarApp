# config.py

class Config:
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Opcjonalnie, aby unikać ostrzeżeń

    # Jeśli masz inne ustawienia konfiguracyjne, które chcesz dodać, możesz je umieścić tutaj


# Opcjonalne klasy dla różnych konfiguracji środowisk:

class DevelopmentConfig(Config):
    DEBUG = True
    # Inne specyficzne dla środowiska deweloperskiego ustawienia

class ProductionConfig(Config):
    DEBUG = False
    # Inne specyficzne dla środowiska produkcyjnego ustawienia

# Możesz dodawać kolejne klasy konfiguracyjne w miarę potrzeb (na przykład dla środowiska testowego).
