# Указываем язык программирования
FROM python:latest

# Копируем все файлы нашего проекта во внутрь контейнера
COPY . /code

# Назначаем главную папку
WORKDIR /code

# Указываем нужные библиоотеки
RUN pip install uvicorn fastapi

# Запуск проекта
CMD ['uvicorn', 'main:app', '--reload', '--host=0.0.0.0']


