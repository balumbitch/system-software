# Архитектура capstone: items-s22

## Обзор

Распределённая система каталога товаров (items) с API gateway, микросервисами и CI/CD.

## Компоненты

```
[Client] → [API Gateway / nginx] → [items-svc-s22 :8201]
                ↓
         [PostgreSQL]
                ↓
         [Redis cache]
```

## Стек

| Слой | Технология |
|------|------------|
| API | REST (FastAPI), GraphQL |
| RPC | gRPC (ItemsService) |
| Оркестрация | Kubernetes + Helm (items-app) |
| CI | GitHub Actions, Docker multi-stage |
| Наблюдаемость | latency-метрики, audit для invoices-s22 |

## Потоки данных

1. `POST /api/items` — создание товара с полем sku
2. Синхронные чтения через gateway
3. Асинхронные события — через saga при заказах (см. week-04)

## Масштабирование

items-s22 масштабируется горизонтально за счёт stateless API и shared DB connection pool.
