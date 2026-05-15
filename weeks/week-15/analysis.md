# Анализ производительности: notifications-s22

## Latency

| Сценарий | p50 latency | p95 latency |
|----------|-------------|-------------|
| REST GET /api/notifications | 8 ms | 22 ms |
| GraphQL query notifications | 10 ms | 28 ms |
| gRPC ListNotifications | 5 ms | 14 ms |

## Наблюдения

Сервис notifications-s22 при пиковой нагрузке (100 RPS) сохраняет p95 latency ниже 30 ms.
Канал доставки (channel) не влияет на latency заметно; узкое место — сериализация JSON в REST.

## Рекомендации

- Кешировать списки уведомлений на gateway
- Для внутренних вызовов использовать gRPC между микросервисами
