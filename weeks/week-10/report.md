# Отчёт по Docker: reviews-s22

## Сборка

```bash
docker build -t reviews-s22 -f weeks/week-10/Dockerfile weeks/week-10
```

## Размер образа

- Итоговый образ: **~180 MB** (python:3.11-slim + зависимости)
- Builder-стадия не попадает в финальный образ благодаря multi-stage

## Слои (layers)

Каждый шаг Dockerfile добавляет новый layer:

1. `FROM python:3.11-slim AS builder` — установка зависимостей
2. `FROM python:3.11-slim` — runtime, копирование только `/install` и кода
3. `EXPOSE 8209` — порт из варианта reviews-s22
4. `CMD` — запуск uvicorn

Multi-stage уменьшает размер: в финале нет pip cache и исходников builder.
