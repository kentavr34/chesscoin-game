# ChessCoin

A multiplayer chess game that runs inside Telegram as a Mini App.

**Play:** https://t.me/chessgamecoin_bot

All of the code in this repository was written with [Claude Code](https://claude.com/claude-code). The author, Kanan Rahimov, is a psychiatrist and not a programmer: he wrote the design, the rules and the bug reports, and the agent wrote the code.

## What is in the game

- real-time games between players, with spectators and replays
- play against the Stockfish engine ("J.A.R.V.I.S"), several levels and time controls
- battles with a stake in in-game coins, public and private, with invite links
- ELO rating, leaderboard, profiles
- tournaments (Swiss system)
- team "country wars" with a shared treasury
- lessons, puzzles and a puzzle of the day
- a shop (avatars, themes), tasks and referrals
- an optional TON wallet connection (TonConnect)
- interface in English, Russian, Azerbaijani and Turkish

## How it is built

| Part | Stack |
|---|---|
| `backend/` | Node.js, TypeScript, Express, Socket.io, Prisma, PostgreSQL, Redis |
| `frontend/` | React, TypeScript, Vite (Telegram Mini App) |
| `bot/` | Python, aiogram |
| `stockfish/` | Stockfish engine service |
| `nginx/`, `docker-compose*.yml` | deployment |

About 53,000 lines of code, 37 database models and 50 migrations. The project started in April 2026.

## Running it

Copy `backend/.env.example` to `.env`, fill in your own values (bot token, database and Redis passwords, JWT secrets) and start the services with Docker Compose. No secrets are stored in this repository.

## An honest note

This is a snapshot of a working project, published without its history. The audience is still small, some modes (tournaments, country wars) have not been tested with many real players, and during development the agent broke working parts more than once. What kept a long project stable were plain rules: check the live result before saying "done", never touch what has been approved, write every mistake down and turn it into a rule.

## Contact

Kanan Rahimov — kenan@ragimoff.org
