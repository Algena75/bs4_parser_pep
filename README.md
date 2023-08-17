# Проект парсинга pep
Проект реализует парсинг документации Python:
* собирает ссылки на статьи о нововведениях в Python
* собирает информацию о статусах версий Python
* скачивает архив с актуальной документацией в формате pdf
## Команда разработчиков:
Когорта 19+ и
Алексей Наумов
## Используемые технолологии:
agrparse
библиотека bs4
библиотека requests с надстройкой requests_cache
прогресс-бар tqdm
## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Algena75/bs4_parser_pep.git
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас windows
    ```
    source venv/scripts/activate
    ```
```
python3 -m pip install --upgrade pip
```
Установите зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
## Документация по программе:
python3 main.py -h
