# Результаты замеров: invoices-s22

## Сравнение REST и gRPC

| Метрика | REST (HTTP/JSON) | gRPC (protobuf) |
|---------|------------------|-----------------|
| Средняя latency | 12 ms | 4 ms |
| p99 latency | 45 ms | 15 ms |
| Размер payload | ~850 bytes | ~120 bytes |

## Вывод

Для сервиса invoices-s22 gRPC показывает меньшую latency и компактнее сериализует данные (float amount, invoice id).
REST проще отлаживать в браузере и не требует codegen.
