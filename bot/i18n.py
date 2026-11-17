"""
bot/i18n.py — мультиязычные тексты ChessCoin Bot

Поддерживаемые языки:
  ru  — Русский       uk  — Українська    de  — Deutsch
  es  — Español       fr  — Français      tr  — Türkçe
  pt  — Português     zh  — 中文          en  — English (fallback)

Добавить новый язык:
  1. Добавь ключ в TRANSLATIONS (скопируй секцию "en" как шаблон)
  2. Добавь lang_code в _LANG_MAP
  Всё — бот подхватит автоматически.
"""

from __future__ import annotations

TRANSLATIONS: dict[str, dict[str, str]] = {
    # ── Русский ───────────────────────────────────────────────────────────────
    "ru": {
        "welcome_title":        "♟ Привет, <b>{name}</b>! Добро пожаловать в <b>ChessCoin</b> — первую шахматную Web3 платформу в Telegram.",
        "welcome_returning":    "♟ С возвращением, <b>{name}</b>!",
        "welcome_back_text":    (
            "Все твои монеты и достижения сохранены.\n"
            "🏆 Готов к новым победам?\n\n"
            "<i>Жми «Играть» и докажи свое мастерство на доске!</i>"
        ),
        "referral_bonus_line":  "🎁 Реферальный бонус <b>от 3 000 ᚙ</b> — после первой сыгранной партии!\n\n",
        "welcome_features":     (
            "<b>Что тебя ждет внутри?</b>\n"
            "⚔️ <b>PvP батлы</b> — играй на монеты с реальными людьми.\n"
            "🤖 <b>Тренировки</b> — побеждай бота J.A.R.V.I.S. и забирай до +20 000 ᚙ.\n"
            "🌍 <b>Войны стран</b> — защищай честь своей страны и получай призы.\n"
            "👥 <b>Рефералы</b> — зови друзей и получай до 15% с их побед (растёт со званием).\n\n"
            "<i>Открывай приложение прямо сейчас!</i>"
        ),
        "battle_invite":        (
            "♟ Привет, <b>{name}</b>! Тебя позвали на батл\n\n"
            "{ref_line}"
            "<i>Жми кнопку ниже чтобы войти в батл:</i>"
        ),
        "referral_bonus_battle":"🎁 Реферальный бонус от 3 000 ᚙ — после первой партии!\n\n",
        "btn_play":             "♟ Играть",
        "btn_leaderboard":      "🏆 Рейтинг",
        "btn_referrals":        "👥 Рефералы",
        "btn_join_battle":      "⚔️ Войти в батл",
        "referral_info_title":  "👥 <b>Реферальная программа</b>",
        "referral_info_body":   (
            "Приглашай — зарабатывай:\n\n"
            "🥇 <b>до 15%</b> от побед друга (растёт с званием)\n"
            "🥈 <b>10%</b> от побед его друзей\n"
            "🎁 <b>от 3 000 ᚙ</b> за первую партию друга\n\n"
            "<i>Бонус — только после первой партии.</i>\n\n"
            "Твоя ссылка:\n"
            "<code>{ref_link}</code>\n"
            "<i>(нажми чтобы скопировать)</i>"
        ),
        "invite_text":          (
            "👥 <b>Твоя реферальная ссылка:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "Пригласи друга — получи <b>от 3 000 ᚙ</b> и <b>до 15%</b> от каждой его победы (по званию)!\n\n"
            "<a href=\"{share_url}\">📤 Поделиться</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — шахматы за монеты</b>\n\n"
            "Команды:\n"
            "/start — открыть игру\n"
            "/play — играть прямо сейчас\n"
            "/invite — твоя реферальная ссылка\n"
            "/help — это сообщение"
        ),
    },

    # ── English ───────────────────────────────────────────────────────────────
    "en": {
        "welcome_title":        "♟ Hey <b>{name}</b>! Welcome to <b>ChessCoin</b> — the first Web3 chess platform in Telegram.",
        "welcome_returning":    "♟ Welcome back, <b>{name}</b>!",
        "welcome_back_text":    (
            "All your coins and achievements are saved.\n"
            "🏆 Ready for new victories?\n\n"
            "<i>Tap «Play» and prove your mastery on the board!</i>"
        ),
        "referral_bonus_line":  "🎁 Referral bonus <b>from 3 000 ᚙ</b> — after your first game!\n\n",
        "welcome_features":     (
            "<b>What's waiting for you inside?</b>\n"
            "⚔️ <b>PvP Battles</b> — play for coins against real players.\n"
            "🤖 <b>Training</b> — beat the J.A.R.V.I.S. bot and win up to +20,000 ᚙ.\n"
            "🌍 <b>Country Wars</b> — defend your country's honor and claim prizes.\n"
            "👥 <b>Referrals</b> — invite friends and get up to 15% of their wins (grows with rank).\n\n"
            "<i>Open the app right now!</i>"
        ),
        "battle_invite":        (
            "♟ Hey <b>{name}</b>! You're invited to a battle\n\n"
            "{ref_line}"
            "<i>Tap the button below to join the battle:</i>"
        ),
        "referral_bonus_battle":"🎁 Referral bonus from 3 000 ᚙ — after your first game!\n\n",
        "btn_play":             "♟ Play",
        "btn_leaderboard":      "🏆 Leaderboard",
        "btn_referrals":        "👥 Referrals",
        "btn_join_battle":      "⚔️ Join Battle",
        "referral_info_title":  "👥 <b>Referral Program</b>",
        "referral_info_body":   (
            "Invite friends — earn automatically:\n\n"
            "🥇 <b>up to 15%</b> from each friend's win (grows with your rank)\n"
            "🥈 <b>10%</b> from their friends' wins\n"
            "🎁 <b>from 3 000 ᚙ</b> when a friend plays their first game\n\n"
            "<i>Bonus is credited after the first game, not just sign-up.</i>\n\n"
            "Your link:\n"
            "<code>{ref_link}</code>\n"
            "<i>(tap to copy)</i>"
        ),
        "invite_text":          (
            "👥 <b>Your referral link:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "Invite a friend — get <b>from 3 000 ᚙ</b> and <b>up to 15%</b> from every win (by rank)!\n\n"
            "<a href=\"{share_url}\">📤 Share on Telegram</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — chess for coins</b>\n\n"
            "Commands:\n"
            "/start — open the game\n"
            "/play — play right now\n"
            "/invite — your referral link\n"
            "/help — this message"
        ),
    },

    # ── Українська ────────────────────────────────────────────────────────────
    "uk": {
        "welcome_title":        "♟ Привіт, <b>{name}</b>! Ласкаво просимо до ChessCoin",
        "referral_bonus_line":  "🎁 Реферальний бонус <b>від 3 000 ᚙ</b> — після першої партії!\n\n",
        "welcome_features":     (
            "Що на тебе чекає:\n"
            "⚔️ Батли на монети з живими гравцями\n"
            "🤖 J.A.R.V.I.S — до <b>+20 000 ᚙ</b> за перемогу\n"
            "🌍 Війни збірних країн\n"
            "👥 Реферали: до <b>15%</b> з перемог друзів\n\n"
            "<i>Відкривай і грай!</i>"
        ),
        "battle_invite":        (
            "♟ Привіт, <b>{name}</b>! Тебе запросили на батл\n\n"
            "{ref_line}"
            "<i>Натисни кнопку нижче щоб увійти в батл:</i>"
        ),
        "referral_bonus_battle":"🎁 Реферальний бонус від 3 000 ᚙ — після першої партії!\n\n",
        "btn_play":             "♟ Грати",
        "btn_leaderboard":      "🏆 Рейтинг",
        "btn_referrals":        "👥 Реферали",
        "btn_join_battle":      "⚔️ Увійти в батл",
        "referral_info_title":  "👥 <b>Реферальна програма</b>",
        "referral_info_body":   (
            "Запрошуй — заробляй:\n\n"
            "🥇 <b>до 15%</b> від перемог друга (зростає зі званням)\n"
            "🥈 <b>10%</b> від перемог його друзів\n"
            "🎁 <b>від 3 000 ᚙ</b> за першу партію друга\n\n"
            "Твоє посилання:\n"
            "<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>Твоє реферальне посилання:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 Поділитися</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — шахи за монети</b>\n\n"
            "/start — відкрити гру\n"
            "/play — грати зараз\n"
            "/invite — реферальне посилання\n"
            "/help — ця довідка"
        ),
    },

    # ── Deutsch ───────────────────────────────────────────────────────────────
    "de": {
        "welcome_title":        "♟ Hallo <b>{name}</b>! Willkommen bei ChessCoin",
        "referral_bonus_line":  "🎁 Empfehlungsbonus <b>ab 3 000 ᚙ</b> — nach deinem ersten Spiel!\n\n",
        "welcome_features":     (
            "Was dich erwartet:\n"
            "⚔️ Kämpfe mit echten Spielern um Einsatz\n"
            "🤖 J.A.R.V.I.S — bis zu <b>+20 000 ᚙ</b>\n"
            "🌍 Länderkämpfe\n"
            "👥 Empfehlungen: bis zu <b>15%</b> aus Siegen\n\n"
            "<i>Öffne die App und spiel!</i>"
        ),
        "battle_invite":        (
            "♟ Hallo <b>{name}</b>! Du wurdest zu einem Kampf eingeladen\n\n"
            "{ref_line}<i>Drücke die Schaltfläche unten:</i>"
        ),
        "referral_bonus_battle":"🎁 ab 3 000 ᚙ nach deinem ersten Spiel!\n\n",
        "btn_play":             "♟ Spielen",
        "btn_leaderboard":      "🏆 Rangliste",
        "btn_referrals":        "👥 Empfehlungen",
        "btn_join_battle":      "⚔️ Kampf beitreten",
        "referral_info_title":  "👥 <b>Empfehlungsprogramm</b>",
        "referral_info_body":   (
            "Lade Freunde ein — verdiene automatisch:\n\n"
            "🥇 <b>bis zu 15%</b> aus jedem Sieg (je nach Rang)\n"
            "🎁 <b>ab 3 000 ᚙ</b> beim ersten Spiel\n\n"
            "Dein Link:\n<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>Dein Empfehlungslink:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 Teilen</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — Schach für Münzen</b>\n\n"
            "/start — Spiel öffnen\n"
            "/play — Jetzt spielen\n"
            "/invite — Empfehlungslink\n"
            "/help — Hilfe"
        ),
    },

    # ── Español ───────────────────────────────────────────────────────────────
    "es": {
        "welcome_title":        "♟ ¡Hola <b>{name}</b>! Bienvenido a ChessCoin",
        "referral_bonus_line":  "🎁 Bono de referido <b>desde 3 000 ᚙ</b> — ¡tras tu primera partida!\n\n",
        "welcome_features":     (
            "Lo que te espera:\n"
            "⚔️ Batallas con jugadores reales por apuestas\n"
            "🤖 J.A.R.V.I.S — hasta <b>+20 000 ᚙ</b>\n"
            "🌍 Guerras entre países\n"
            "👥 Referidos: hasta <b>15%</b> de las ganancias\n\n"
            "<i>¡Abre la app y juega!</i>"
        ),
        "battle_invite":        (
            "♟ ¡Hola <b>{name}</b>! Te invitaron a una batalla\n\n"
            "{ref_line}<i>Pulsa el botón para unirte:</i>"
        ),
        "referral_bonus_battle":"🎁 desde 3 000 ᚙ tras tu primera partida!\n\n",
        "btn_play":             "♟ Jugar",
        "btn_leaderboard":      "🏆 Clasificación",
        "btn_referrals":        "👥 Referidos",
        "btn_join_battle":      "⚔️ Unirse a batalla",
        "referral_info_title":  "👥 <b>Programa de referidos</b>",
        "referral_info_body":   (
            "Invita amigos — gana automáticamente:\n\n"
            "🥇 <b>hasta 15%</b> de cada victoria (según tu rango)\n"
            "🎁 <b>desde 3 000 ᚙ</b> en su primera partida\n\n"
            "Tu enlace:\n<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>Tu enlace de referido:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 Compartir</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — ajedrez por monedas</b>\n\n"
            "/start — abrir el juego\n"
            "/play — jugar ahora\n"
            "/invite — enlace de referido\n"
            "/help — ayuda"
        ),
    },

    # ── Français ──────────────────────────────────────────────────────────────
    "fr": {
        "welcome_title":        "♟ Bonjour <b>{name}</b> ! Bienvenue sur ChessCoin",
        "referral_bonus_line":  "🎁 Bonus de parrainage <b>à partir de 3 000 ᚙ</b> — après ta 1ʳᵉ partie !\n\n",
        "welcome_features":     (
            "Ce qui t'attend :\n"
            "⚔️ Batailles contre de vrais joueurs\n"
            "🤖 J.A.R.V.I.S — jusqu'à <b>+20 000 ᚙ</b>\n"
            "🌍 Guerres entre pays\n"
            "👥 Parrainage : jusqu'à <b>15%</b> des gains d'amis\n\n"
            "<i>Ouvre l'app et joue !</i>"
        ),
        "battle_invite":        (
            "♟ Bonjour <b>{name}</b> ! Tu es invité à une bataille\n\n"
            "{ref_line}<i>Appuie sur le bouton ci-dessous :</i>"
        ),
        "referral_bonus_battle":"🎁 à partir de 3 000 ᚙ après ta 1ʳᵉ partie !\n\n",
        "btn_play":             "♟ Jouer",
        "btn_leaderboard":      "🏆 Classement",
        "btn_referrals":        "👥 Parrainages",
        "btn_join_battle":      "⚔️ Rejoindre",
        "referral_info_title":  "👥 <b>Programme de parrainage</b>",
        "referral_info_body":   (
            "Invite des amis — gagne automatiquement :\n\n"
            "🥇 <b>jusqu\'à 15%</b> de chaque victoire (selon ton rang)\n"
            "🎁 <b>à partir de 3 000 ᚙ</b> à sa 1ʳᵉ partie\n\n"
            "Ton lien :\n<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>Ton lien de parrainage :</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 Partager</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — échecs contre des pièces</b>\n\n"
            "/start — ouvrir le jeu\n"
            "/play — jouer maintenant\n"
            "/invite — lien de parrainage\n"
            "/help — aide"
        ),
    },

    # ── Türkçe ────────────────────────────────────────────────────────────────
    "tr": {
        "welcome_title":        "♟ Merhaba <b>{name}</b>! ChessCoin'e hoş geldin",
        "referral_bonus_line":  "🎁 Referans bonusu <b>3 000 ᚙ\'den başlayarak</b> — ilk oyundan sonra!\n\n",
        "welcome_features":     (
            "Seni neler bekliyor:\n"
            "⚔️ Gerçek oyuncularla coin bahisli maçlar\n"
            "🤖 J.A.R.V.I.S — <b>+20 000 ᚙ</b>'e kadar\n"
            "🌍 Ülke savaşları\n"
            "👥 Referanslar: kazançtan <b>%15'e kadar</b>\n\n"
            "<i>Uygulamayı aç ve oyna!</i>"
        ),
        "battle_invite":        (
            "♟ Merhaba <b>{name}</b>! Bir maça davet edildin\n\n"
            "{ref_line}<i>Katılmak için aşağıdaki butona bas:</i>"
        ),
        "referral_bonus_battle":"🎁 3 000 ᚙ\'den başlayarak ilk oyundan sonra!\n\n",
        "btn_play":             "♟ Oyna",
        "btn_leaderboard":      "🏆 Sıralama",
        "btn_referrals":        "👥 Referanslar",
        "btn_join_battle":      "⚔️ Maça Katıl",
        "referral_info_title":  "👥 <b>Referans Programı</b>",
        "referral_info_body":   (
            "Arkadaşlarını davet et — otomatik kazan:\n\n"
            "🥇 Her kazançtan <b>%15\'e kadar</b> (rütbene göre)\n"
            "🎁 İlk oyunda <b>3 000 ᚙ\'den başlayarak</b>\n\n"
            "Bağlantın:\n<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>Referans bağlantın:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 Paylaş</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — coin için satranç</b>\n\n"
            "/start — oyunu aç\n"
            "/play — hemen oyna\n"
            "/invite — referans bağlantısı\n"
            "/help — yardım"
        ),
    },

    # ── Português ─────────────────────────────────────────────────────────────
    "pt": {
        "welcome_title":        "♟ Olá <b>{name}</b>! Bem-vindo ao ChessCoin",
        "referral_bonus_line":  "🎁 Bônus de indicação <b>a partir de 3 000 ᚙ</b> — após a primeira partida!\n\n",
        "welcome_features":     (
            "O que te espera:\n"
            "⚔️ Batalhas com jogadores reais\n"
            "🤖 J.A.R.V.I.S — até <b>+20 000 ᚙ</b>\n"
            "🌍 Guerras entre países\n"
            "👥 Indicações: até <b>15%</b> dos ganhos\n\n"
            "<i>Abre o app e joga!</i>"
        ),
        "battle_invite":        (
            "♟ Olá <b>{name}</b>! Você foi convidado para uma batalha\n\n"
            "{ref_line}<i>Toca o botão abaixo para entrar:</i>"
        ),
        "referral_bonus_battle":"🎁 a partir de 3 000 ᚙ após a primeira partida!\n\n",
        "btn_play":             "♟ Jogar",
        "btn_leaderboard":      "🏆 Classificação",
        "btn_referrals":        "👥 Indicações",
        "btn_join_battle":      "⚔️ Entrar na batalha",
        "referral_info_title":  "👥 <b>Programa de indicações</b>",
        "referral_info_body":   (
            "Convide amigos — ganhe automaticamente:\n\n"
            "🥇 <b>até 15%</b> de cada vitória (conforme seu posto)\n"
            "🎁 <b>a partir de 3 000 ᚙ</b> na primeira partida\n\n"
            "Seu link:\n<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>Seu link de indicação:</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 Compartilhar</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — xadrez por moedas</b>\n\n"
            "/start — abrir o jogo\n"
            "/play — jogar agora\n"
            "/invite — link de indicação\n"
            "/help — ajuda"
        ),
    },

    # ── 中文 ──────────────────────────────────────────────────────────────────
    "zh": {
        "welcome_title":        "♟ 你好 <b>{name}</b>！欢迎来到 ChessCoin",
        "referral_bonus_line":  "🎁 推荐奖励 <b>3 000 ᚙ 起</b> — 首局游戏后发放！\n\n",
        "welcome_features":     (
            "等你的精彩：\n"
            "⚔️ 与真实玩家对战下注\n"
            "🤖 J.A.R.V.I.S — 最高 <b>+20 000 ᚙ</b>\n"
            "🌍 国家队战争\n"
            "👥 推荐计划：朋友赢局最高 <b>15%</b>\n\n"
            "<i>打开应用开始游戏！</i>"
        ),
        "battle_invite":        (
            "♟ 你好 <b>{name}</b>！你被邀请参加对战\n\n"
            "{ref_line}<i>点击下方按钮加入：</i>"
        ),
        "referral_bonus_battle":"🎁 首局后 3 000 ᚙ 起！\n\n",
        "btn_play":             "♟ 开始游戏",
        "btn_leaderboard":      "🏆 排行榜",
        "btn_referrals":        "👥 推荐",
        "btn_join_battle":      "⚔️ 加入对战",
        "referral_info_title":  "👥 <b>推荐计划</b>",
        "referral_info_body":   (
            "邀请朋友 — 自动获得收益：\n\n"
            "🥇 朋友每次获胜最高 <b>15%</b>（按军衔）\n"
            "🎁 首局 <b>3 000 ᚙ 起</b>\n\n"
            "你的链接：\n<code>{ref_link}</code>"
        ),
        "invite_text":          (
            "👥 <b>你的推荐链接：</b>\n\n"
            "<code>{ref_link}</code>\n\n"
            "<a href=\"{share_url}\">📤 分享</a>"
        ),
        "help_text":            (
            "♟ <b>ChessCoin — 用金币下棋</b>\n\n"
            "/start — 打开游戏\n"
            "/play — 立即游戏\n"
            "/invite — 推荐链接\n"
            "/help — 帮助"
        ),
    },
}

# ─── Карта кодов языков Telegram → ключ словаря ───────────────────────────────
_LANG_MAP: dict[str, str] = {
    "ru": "ru", "be": "ru", "kk": "ru",
    "uk": "uk",
    "de": "de",
    "es": "es",
    "fr": "fr",
    "tr": "tr",
    "pt": "pt", "pt-br": "pt",
    "zh": "zh", "zh-hans": "zh", "zh-hant": "zh",
}


def detect_lang(language_code: str | None) -> str:
    """Определяет язык по language_code из Telegram. Fallback: 'en'."""
    if not language_code:
        return "en"
    lower = language_code.lower()
    if lower in _LANG_MAP:
        return _LANG_MAP[lower]
    return _LANG_MAP.get(lower[:2], "en")


def t(lang_code: str | None, key: str) -> str:
    """Получить перевод. Fallback: английский → сам ключ."""
    lang = detect_lang(lang_code)
    return (
        TRANSLATIONS.get(lang, {}).get(key)
        or TRANSLATIONS.get("en", {}).get(key)
        or key
    )