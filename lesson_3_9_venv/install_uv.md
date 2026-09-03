# macOS і Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Перевірка встановлення
uv --version

# Ініціалізувати проєкт у поточній папці
uv init .

# створити віртутальне середовище
uv venv

# Запутити вітрульне середовище Windows
.\.venv\Scripts\activate

# Запутити вітрульне середовище Linux\Mac
./.venv/bin/activate

# Встановлення пакету
uv add requests

# Синхронізувати середовище з uv.lock (аналог pip install -r)
uv sync