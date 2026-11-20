# itmo-ai-practice-07

Тестовый репозиторий для практик 7.1 (AI code review) и 7.2 (issue triage) курса
AI engineering tools, ИТМО ФИТиП.

Содержимое намеренно небольшое: пара модулей на Python и тесты к ним.
PR и issues в этом репозитории создаются специально для проверки n8n-сценариев.

## Что внутри

- `src/calc.py` — простой калькулятор статистики
- `src/storage.py` — чтение/запись JSON-файла с результатами
- `tests/test_calc.py` — тесты

## Запуск

```bash
python3 -m pytest -q
```
