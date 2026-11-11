# Лабораторная работа 2 — Docker image и writable layer

Вариант 08, префикс `salakhov-08`.

Сборка: `docker build --build-arg VERSION=1.0 -t salakhov-08/probe:0.9 .`
Запуск: `docker run --rm -p 8024:5008 salakhov-08/probe:0.9`

Сервис предоставляет `GET /`, `GET /me` и вариантный `GET /hostname`.
