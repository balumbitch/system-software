# Security audit: invoices-s22

## Область

Микросервис invoices-s22: REST API, хранение счетов (amount), развёртывание в Kubernetes.

## Находки

| # | Риск | Статус |
|---|------|--------|
| 1 | Отсутствие TLS на ingress | Средний — включить HTTPS |
| 2 | Секреты в plain env | Высокий — перейти на K8s Secrets |
| 3 | Нет rate limiting | Средний — добавить на gateway |

## Меры

- Образ invoices-s22 сканировать в CI (Trivy)
- Минимальные RBAC для service account
- Логировать доступ к /api/invoices без PII в amount
