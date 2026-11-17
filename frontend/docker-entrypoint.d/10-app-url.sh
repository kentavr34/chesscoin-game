#!/bin/sh
# Подставляет актуальный домен в манифест TonConnect при старте контейнера.
# Домен прода менялся трижды (06.06, 29.07, 09.2026 — истёк chesscoin.app).
# Теперь это переменная APP_URL, а не пересборка фронтенда.
set -eu

MANIFEST=/usr/share/nginx/html/tonconnect-manifest.json

if [ -n "${APP_URL:-}" ] && [ -f "$MANIFEST" ]; then
  # В манифесте все ссылки вида https://<домен>/путь — меняем только домен.
  sed -i -E "s#https://[^/\"]+#${APP_URL}#g" "$MANIFEST"
fi
