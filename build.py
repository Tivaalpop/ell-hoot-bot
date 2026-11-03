#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build.py — يبني مشروع Ell Hoot AI Bot v6.0 كاملاً.
شغّله: python build.py
النتيجة: مجلد ell-hoot-bot/ فيه كل الملفات جاهزة للتشغيل.
"""

import os
import sys
from pathlib import Path

BASE = Path("ell-hoot-bot")
FILES = {}


# ============================================================
# config.py
# ============================================================
FILES["config.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Configuration — كل شيء من environment variables."""

import os
import sys
from pathlib import Path
from datetime import timezone, timedelta

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("DATA_DIR", BASE_DIR / "data"))
LOGS_DIR = Path(os.environ.get("LOGS_DIR", BASE_DIR / "logs"))
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    print("❌ BOT_TOKEN مطلوب في environment variables", file=sys.stderr)
    sys.exit(1)

try:
    ADMIN_ID = int(os.environ.get("ADMIN_ID", ""))
except ValueError:
    print("❌ ADMIN_ID غير صالح", file=sys.stderr)
    sys.exit(1)
if ADMIN_ID <= 0:
    print("❌ ADMIN_ID مطلوب", file=sys.stderr)
    sys.exit(1)

BOT_NAME = os.environ.get("BOT_NAME", "Ell Hoot AI")
CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "@Ell_Hoot")
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/Ell_Hoot")
SUPPORT_URL = os.environ.get("SUPPORT_URL", CHANNEL_URL)
FORCE_SUB_DEFAULT = False

DB_PATH = str(DATA_DIR / "bot.db")

AI_ENDPOINT = os.environ.get("AI_ENDPOINT", "https://android.chat.openai.com/backend-api/f/conversation")
AI_PREPARE_ENDPOINT = os.environ.get("AI_PREPARE_ENDPOINT", "https://android.chat.openai.com/backend-api/f/conversation/prepare")
AI_TIMEOUT = int(os.environ.get("AI_TIMEOUT", "90"))
AI_STREAM_EDIT_THROTTLE = float(os.environ.get("AI_STREAM_EDIT_THROTTLE", "0.7"))

AI_HEADERS = {
    "User-Agent": os.environ.get("AI_USER_AGENT", "ChatGPT/1.2027.000 (Android 15; RMX3834; build 2700000)"),
    "Accept": "application/json",
    "Content-Type": "application/json",
    "oai-package-name": "com.Modderme",
    "oai-client-type": "android",
    "oai-device-id": os.environ.get("AI_DEVICE_ID", "84329164059103383964"),
    "accept-language": "en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7",
    "x-device-tier": "lower_mid",
    "chatgpt-account-id": os.environ.get("AI_ACCOUNT_ID", "84329164059103383964"),
}

MAX_MESSAGES_PER_MIN = int(os.environ.get("MAX_MESSAGES_PER_MIN", "20"))
MAX_MESSAGE_LENGTH = int(os.environ.get("MAX_MESSAGE_LENGTH", "4000"))
SUBSCRIPTION_CACHE_TTL = int(os.environ.get("SUBSCRIPTION_CACHE_TTL", "300"))
MEMORY_MAX_ITEMS = int(os.environ.get("MEMORY_MAX_ITEMS", "20"))

TZ = timezone(timedelta(hours=int(os.environ.get("TZ_OFFSET", "3"))))

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_FILE = LOGS_DIR / "bot.log"

SUPPORTED_MODELS = {
    "auto": "🤖 تلقائي",
    "gpt-4": "🚀 GPT-4",
    "gpt-4o": "🦾 GPT-4o",
    "gpt-4-turbo": "🧠 GPT-4 Turbo",
    "gpt-4-turbo-preview": "⚡ GPT-4 Turbo Preview",
    "gpt-3.5-turbo": "💨 GPT-3.5 Turbo",
    "gpt-4o-mini": "📱 GPT-4o Mini",
    "gpt-4-32k": "📚 GPT-4 32K",
    "gpt-3.5-turbo-16k": "📖 GPT-3.5 16K",
}
DEFAULT_MODEL = "auto"

PERSONAS = {
    "friendly": {"name": "😊 ودود", "prompt": "أنت صديق ودود، ردودك دافئة ومشجعة."},
    "formal": {"name": "🎩 رسمي", "prompt": "أنت مساعد رسمي، ردودك دقيقة ومهنية."},
    "sarcastic": {"name": "😏 ساخر", "prompt": "أنت مساعد ساخر بذكاء، ردودك فيها نكتة خفيفة."},
    "poet": {"name": "📜 شاعر", "prompt": "أنت شاعر، ردودك بأسلوب أدبي جميل."},
    "teacher": {"name": "👨‍🏫 مدرس", "prompt": "أنت مدرس صبور، تشرح بخطوات واضحة."},
    "coder": {"name": "💻 مبرمج", "prompt": "أنت مبرمج محترف، ردودك تقنية ومباشرة."},
}

DIALECTS = {
    "msa": {"name": "🇸🇦 فصحى", "prompt": "تحدث بالفصحى."},
    "egy": {"name": "🇪🇬 مصري", "prompt": "تحدث باللهجة المصرية."},
    "gulf": {"name": "🇸🇦 خليجي", "prompt": "تحدث باللهجة الخليجية."},
    "levant": {"name": "🇱🇧 شامي", "prompt": "تحدث باللهجة الشامية."},
}

DEFAULT_PERSONA = "friendly"
DEFAULT_DIALECT = "egy"

XP_PER_MESSAGE = 10
XP_PER_LEVEL = 100
LEVELS = {
    1: {"name": "🌱 مبتدئ", "xp": 0},
    2: {"name": "🌿 نشط", "xp": 100},
    3: {"name": "🌳 متمرس", "xp": 300},
    4: {"name": "⭐ محترف", "xp": 700},
    5: {"name": "💎 خبير", "xp": 1500},
    6: {"name": "👑 أسطورة", "xp": 3000},
    7: {"name": "🔥 إمبراطور", "xp": 6000},
}

STREAK_REWARDS = {
    3: {"xp": 100, "msg": "🎁 +100 XP"},
    7: {"xp": 300, "msg": "🎁 +300 XP + نموذج مميز"},
    14: {"xp": 700, "msg": "🎁 +700 XP + Premium أسبوع"},
    30: {"xp": 2000, "msg": "🎁 +2000 XP + Premium شهر"},
}

REFERRAL_REWARDS = {
    5: {"premium_days": 7, "msg": "أسبوع Premium"},
    25: {"premium_days": 30, "msg": "شهر Premium"},
    100: {"premium_days": 3650, "msg": "Premium مدى الحياة"},
}

CHALLENGE_CATEGORIES = ["story", "code", "poem", "idea", "riddle"]
DEBUG = os.environ.get("DEBUG", "0") == "1"
'''


# ============================================================
# database.py
# ============================================================
FILES["database.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Database — SQLite + WAL + Thread-safe."""

import sqlite3
import threading
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any, Tuple

from config import DB_PATH, TZ, LEVELS

log = logging.getLogger("db")


class Database:
    def __init__(self, path: str):
        self.path = path
        self._local = threading.local()
        self._lock = threading.Lock()
        self._init_schema()

    def _get_conn(self) -> sqlite3.Connection:
        if not hasattr(self._local, "conn") or self._local.conn is None:
            conn = sqlite3.connect(self.path, check_same_thread=False, timeout=30)
            conn.execute("PRAGMA journal_mode=WAL")
            conn.execute("PRAGMA synchronous=NORMAL")
            conn.execute("PRAGMA foreign_keys=ON")
            conn.row_factory = sqlite3.Row
            self._local.conn = conn
        return self._local.conn

    def _init_schema(self):
        with self._lock:
            conn = sqlite3.connect(self.path, timeout=30)
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT DEFAULT '',
                first_name TEXT DEFAULT '',
                last_name TEXT DEFAULT '',
                joined_at TEXT,
                last_seen TEXT,
                is_banned INTEGER DEFAULT 0,
                ban_reason TEXT DEFAULT '',
                is_premium INTEGER DEFAULT 0,
                premium_until TEXT,
                xp INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                streak INTEGER DEFAULT 0,
                last_streak_date TEXT,
                messages_count INTEGER DEFAULT 0,
                referrals INTEGER DEFAULT 0,
                referred_by INTEGER,
                persona TEXT DEFAULT 'friendly',
                dialect TEXT DEFAULT 'egy',
                bot_name TEXT DEFAULT '',
                model TEXT DEFAULT 'auto',
                streaming_enabled INTEGER DEFAULT 1,
                memory_enabled INTEGER DEFAULT 1
            )""")
            c.execute("CREATE INDEX IF NOT EXISTS idx_users_last_seen ON users(last_seen)")
            c.execute("CREATE INDEX IF NOT EXISTS idx_users_xp ON users(xp DESC)")

            c.execute("""CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                key TEXT,
                value TEXT,
                created_at TEXT,
                UNIQUE(user_id, key)
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                conv_id TEXT UNIQUE,
                model TEXT,
                conversation_id TEXT,
                parent_message_id TEXT,
                created_at TEXT,
                messages_count INTEGER DEFAULT 0,
                last_activity TEXT
            )""")
            c.execute("CREATE INDEX IF NOT EXISTS idx_conv_user ON conversations(user_id)")

            c.execute("""CREATE TABLE IF NOT EXISTS messages_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                conv_id TEXT,
                user_message TEXT,
                bot_response TEXT,
                model TEXT,
                timestamp TEXT
            )""")
            c.execute("CREATE INDEX IF NOT EXISTS idx_msg_user ON messages_history(user_id)")

            c.execute("""CREATE TABLE IF NOT EXISTS saved_prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                prompt_name TEXT,
                prompt_text TEXT,
                created_at TEXT
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS bans (
                user_id INTEGER PRIMARY KEY,
                reason TEXT,
                banned_at TEXT,
                banned_by INTEGER
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                admin_id INTEGER,
                action TEXT,
                target TEXT,
                details TEXT,
                timestamp TEXT
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS bot_settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS gallery (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                title TEXT,
                content TEXT,
                category TEXT,
                likes INTEGER DEFAULT 0,
                created_at TEXT
            )""")
            c.execute("CREATE INDEX IF NOT EXISTS idx_gallery_likes ON gallery(likes DESC)")
            c.execute("""CREATE TABLE IF NOT EXISTS gallery_likes (
                user_id INTEGER,
                item_id INTEGER,
                PRIMARY KEY (user_id, item_id)
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS challenges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                title TEXT,
                description TEXT,
                start_at TEXT,
                end_at TEXT,
                is_active INTEGER DEFAULT 1
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS challenge_entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                challenge_id INTEGER,
                user_id INTEGER,
                content TEXT,
                votes INTEGER DEFAULT 0,
                created_at TEXT
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS challenge_votes (
                user_id INTEGER,
                entry_id INTEGER,
                PRIMARY KEY (user_id, entry_id)
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                room_code TEXT UNIQUE,
                owner_id INTEGER,
                title TEXT,
                created_at TEXT,
                is_active INTEGER DEFAULT 1
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS room_members (
                room_id INTEGER,
                user_id INTEGER,
                joined_at TEXT,
                PRIMARY KEY (room_id, user_id)
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS twins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                personality TEXT,
                trained_at TEXT,
                samples_count INTEGER DEFAULT 0,
                share_slug TEXT UNIQUE
            )""")

            c.execute("""CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT,
                message TEXT,
                is_sent INTEGER DEFAULT 0,
                created_at TEXT,
                sent_at TEXT
            )""")

            defaults = {
                "maintenance": "0", "force_sub": "0", "welcome_message": "أهلاً بك!",
                "streaming_default": "1", "max_messages_per_min": "20",
                "memory_enabled_global": "1", "xp_enabled": "1", "streak_enabled": "1",
                "referral_enabled": "1", "gallery_enabled": "1", "challenges_enabled": "1",
                "rooms_enabled": "1", "twins_enabled": "1",
            }
            for k, v in defaults.items():
                c.execute("INSERT OR IGNORE INTO bot_settings (key, value) VALUES (?, ?)", (k, v))

            conn.commit()
            conn.close()
            log.info("✅ DB schema ready")

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        conn = self._get_conn()
        cur = conn.execute(query, params)
        conn.commit()
        return cur

    def executemany(self, query: str, params_list: list) -> sqlite3.Cursor:
        conn = self._get_conn()
        cur = conn.executemany(query, params_list)
        conn.commit()
        return cur

    def fetchone(self, query: str, params: tuple = ()) -> Optional[sqlite3.Row]:
        return self._get_conn().execute(query, params).fetchone()

    def fetchall(self, query: str, params: tuple = ()) -> List[sqlite3.Row]:
        return self._get_conn().execute(query, params).fetchall()

    def get_setting(self, key: str, default: str = "") -> str:
        row = self.fetchone("SELECT value FROM bot_settings WHERE key = ?", (key,))
        return row["value"] if row else default

    def set_setting(self, key: str, value: str):
        self.execute("INSERT OR REPLACE INTO bot_settings (key, value) VALUES (?, ?)", (key, value))

    def get_bool(self, key: str, default: bool = False) -> bool:
        v = self.get_setting(key, "1" if default else "0")
        return v == "1"

    def ensure_user(self, user_id: int, username: str = "", first_name: str = "", last_name: str = "") -> sqlite3.Row:
        now = datetime.now(TZ).isoformat()
        row = self.fetchone("SELECT * FROM users WHERE user_id = ?", (user_id,))
        if not row:
            self.execute(
                "INSERT INTO users (user_id, username, first_name, last_name, joined_at, last_seen) VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, username or "", first_name or "", last_name or "", now, now),
            )
            log.info(f"👤 New user: {user_id}")
            return self.fetchone("SELECT * FROM users WHERE user_id = ?", (user_id,))
        self.execute(
            "UPDATE users SET last_seen = ?, username = COALESCE(NULLIF(?, ''), username), first_name = COALESCE(NULLIF(?, ''), first_name) WHERE user_id = ?",
            (now, username or "", first_name or "", user_id),
        )
        return self.fetchone("SELECT * FROM users WHERE user_id = ?", (user_id,))

    def get_user(self, user_id: int) -> Optional[sqlite3.Row]:
        return self.fetchone("SELECT * FROM users WHERE user_id = ?", (user_id,))

    def update_user(self, user_id: int, **fields):
        if not fields:
            return
        keys = ", ".join(f"{k} = ?" for k in fields)
        values = tuple(fields.values()) + (user_id,)
        self.execute(f"UPDATE users SET {keys} WHERE user_id = ?", values)

    def memory_set(self, user_id: int, key: str, value: str):
        self.execute(
            "INSERT OR REPLACE INTO memory (user_id, key, value, created_at) VALUES (?, ?, ?, ?)",
            (user_id, key, value, datetime.now(TZ).isoformat()),
        )

    def memory_get(self, user_id: int, key: str) -> Optional[str]:
        row = self.fetchone("SELECT value FROM memory WHERE user_id = ? AND key = ?", (user_id, key))
        return row["value"] if row else None

    def memory_all(self, user_id: int) -> Dict[str, str]:
        rows = self.fetchall("SELECT key, value FROM memory WHERE user_id = ?", (user_id,))
        return {r["key"]: r["value"] for r in rows}

    def memory_clear(self, user_id: int):
        self.execute("DELETE FROM memory WHERE user_id = ?", (user_id,))

    def add_xp(self, user_id: int, amount: int) -> Tuple[int, int, Optional[int]]:
        row = self.get_user(user_id)
        if not row:
            return 0, 1, None
        new_xp = row["xp"] + amount
        new_level = 1
        for lvl, data in sorted(LEVELS.items()):
            if new_xp >= data["xp"]:
                new_level = lvl
        leveled_up = new_level if new_level > row["level"] else None
        self.execute("UPDATE users SET xp = ?, level = ? WHERE user_id = ?", (new_xp, new_level, user_id))
        return new_xp, new_level, leveled_up

    def update_streak(self, user_id: int) -> Tuple[int, bool]:
        row = self.get_user(user_id)
        if not row:
            return 0, False
        now = datetime.now(TZ)
        today = now.date().isoformat()
        last = row["last_streak_date"]
        current_streak = row["streak"] or 0
        if last == today:
            return current_streak, False
        if last:
            try:
                last_date = datetime.fromisoformat(last).date()
                delta = (now.date() - last_date).days
                if delta == 1:
                    current_streak += 1
                else:
                    current_streak = 1
            except Exception:
                current_streak = 1
        else:
            current_streak = 1
        self.execute(
            "UPDATE users SET streak = ?, last_streak_date = ? WHERE user_id = ?",
            (current_streak, today, user_id),
        )
        return current_streak, True

    def add_referral(self, referrer_id: int) -> int:
        self.execute("UPDATE users SET referrals = referrals + 1 WHERE user_id = ?", (referrer_id,))
        row = self.fetchone("SELECT referrals FROM users WHERE user_id = ?", (referrer_id,))
        return row["referrals"] if row else 0

    def ban(self, user_id: int, reason: str = "", admin_id: int = 0):
        now = datetime.now(TZ).isoformat()
        self.execute(
            "INSERT OR REPLACE INTO bans (user_id, reason, banned_at, banned_by) VALUES (?, ?, ?, ?)",
            (user_id, reason, now, admin_id),
        )
        self.execute("UPDATE users SET is_banned = 1, ban_reason = ? WHERE user_id = ?", (reason, user_id))

    def unban(self, user_id: int):
        self.execute("DELETE FROM bans WHERE user_id = ?", (user_id,))
        self.execute("UPDATE users SET is_banned = 0, ban_reason = '' WHERE user_id = ?", (user_id,))

    def is_banned(self, user_id: int) -> bool:
        row = self.fetchone("SELECT 1 FROM bans WHERE user_id = ?", (user_id,))
        return row is not None

    def audit(self, admin_id: int, action: str, target: str = "", details: str = ""):
        self.execute(
            "INSERT INTO audit_log (admin_id, action, target, details, timestamp) VALUES (?, ?, ?, ?, ?)",
            (admin_id, action, target, details, datetime.now(TZ).isoformat()),
        )

    def stats(self) -> Dict[str, Any]:
        today = datetime.now(TZ).date().isoformat()
        return {
            "total_users": self.fetchone("SELECT COUNT(*) AS c FROM users")["c"],
            "today_users": self.fetchone("SELECT COUNT(*) AS c FROM users WHERE joined_at LIKE ?", (f"{today}%",))["c"],
            "banned": self.fetchone("SELECT COUNT(*) AS c FROM bans")["c"],
            "total_messages": self.fetchone("SELECT COUNT(*) AS c FROM messages_history")["c"],
            "today_messages": self.fetchone("SELECT COUNT(*) AS c FROM messages_history WHERE timestamp LIKE ?", (f"{today}%",))["c"],
            "total_conversations": self.fetchone("SELECT COUNT(*) AS c FROM conversations")["c"],
            "total_prompts": self.fetchone("SELECT COUNT(*) AS c FROM saved_prompts")["c"],
            "total_gallery": self.fetchone("SELECT COUNT(*) AS c FROM gallery")["c"],
            "total_twins": self.fetchone("SELECT COUNT(*) AS c FROM twins")["c"],
            "total_rooms": self.fetchone("SELECT COUNT(*) AS c FROM rooms WHERE is_active = 1")["c"],
        }

    def top_models(self, limit: int = 5) -> List[sqlite3.Row]:
        return self.fetchall(
            "SELECT model, COUNT(*) AS c FROM messages_history GROUP BY model ORDER BY c DESC LIMIT ?",
            (limit,),
        )
'''


# ============================================================
# models.py
# ============================================================
FILES["models.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AI Models — OpenAI Android API wrapper."""

import json
import uuid
import logging
from typing import Optional, Dict, Any, Generator

import requests

from config import AI_ENDPOINT, AI_PREPARE_ENDPOINT, AI_HEADERS, AI_TIMEOUT, SUPPORTED_MODELS, DEFAULT_MODEL

log = logging.getLogger("models")


class AIError(Exception):
    pass


def _prepare_headers(conduit_token: str) -> Dict[str, str]:
    h = AI_HEADERS.copy()
    h["Conduit-Token"] = conduit_token
    h["x-oai-convo-session-id"] = str(uuid.uuid4())
    h["x-oai-turn-trace-id"] = str(uuid.uuid4())
    h["x-openai-target-path"] = "/backend-api/f/conversation"
    return h


class AIClient:
    def __init__(self):
        self._session = requests.Session()
        self._session.headers.update(AI_HEADERS)

    def _get_conduit_token(self) -> Optional[str]:
        try:
            r = self._session.post(
                AI_PREPARE_ENDPOINT,
                json={
                    "action": "next", "messages": [], "model": "auto",
                    "history_and_training_disabled": False, "force_use_sse": False,
                    "timezone": "Africa/Cairo", "timezone_offset_min": -180,
                },
                timeout=30,
            )
            if r.status_code == 200:
                return r.json().get("conduit_token", "")
        except Exception as e:
            log.warning(f"conduit token error: {e}")
        return None

    def new_conversation_headers(self) -> Optional[Dict[str, str]]:
        token = self._get_conduit_token()
        if not token:
            return None
        return _prepare_headers(token)

    def send_message(
        self, headers: Dict[str, str], model: str, message_text: str,
        conversation_id: Optional[str] = None,
        parent_message_id: Optional[str] = None,
        streaming: bool = True,
        system_prompt: Optional[str] = None,
    ) -> Generator[Dict[str, Any], None, None]:
        if model not in SUPPORTED_MODELS:
            model = DEFAULT_MODEL

        messages = []
        if system_prompt:
            messages.append({
                "id": str(uuid.uuid4()),
                "author": {"role": "system"},
                "content": {"content_type": "text", "parts": [system_prompt]},
                "status": "finished_successfully",
            })
        messages.append({
            "id": str(uuid.uuid4()),
            "author": {"role": "user"},
            "content": {"content_type": "text", "parts": [message_text]},
            "status": "finished_successfully",
        })

        payload = {
            "action": "next", "messages": messages, "model": model,
            "parent_message_id": parent_message_id or str(uuid.uuid4()),
            "stream": bool(streaming), "timezone": "Africa/Cairo",
            "timezone_offset_min": -180,
        }
        if conversation_id:
            payload["conversation_id"] = conversation_id

        try:
            r = self._session.post(AI_ENDPOINT, headers=headers, json=payload,
                                   stream=bool(streaming), timeout=AI_TIMEOUT)
        except requests.exceptions.Timeout:
            raise AIError("انتهت مهلة الاتصال")
        except requests.exceptions.RequestException as e:
            raise AIError(f"خطأ اتصال: {str(e)[:100]}")

        if r.status_code != 200:
            raise AIError(f"ChatGPT أعاد {r.status_code}")

        full_text = ""
        last_msg_id = None
        conv_id = conversation_id

        try:
            for line in r.iter_lines(decode_unicode=True):
                if not line or not line.startswith("data: "):
                    continue
                data = line[6:]
                if data == "[DONE]":
                    break
                try:
                    event = json.loads(data)
                except json.JSONDecodeError:
                    continue
                if "conversation_id" in event and not conv_id:
                    conv_id = event["conversation_id"]
                if "message" in event and "content" in event["message"]:
                    parts = event["message"]["content"].get("parts", [])
                    if parts and parts[0] and parts[0] != full_text:
                        full_text = parts[0]
                        yield {"type": "delta", "text": full_text, "conv_id": conv_id}
                    if "id" in event["message"]:
                        last_msg_id = event["message"]["id"]
        except Exception as e:
            log.warning(f"stream parse error: {e}")

        yield {"type": "done", "full": full_text, "message_id": last_msg_id, "conv_id": conv_id}


ai_client = AIClient()
'''


# ============================================================
# utils.py
# ============================================================
FILES["utils.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilities."""

import re
import time
import threading
from datetime import datetime
from typing import List, Dict

from config import TZ, MAX_MESSAGE_LENGTH


def split_message(text: str, max_len: int = MAX_MESSAGE_LENGTH) -> List[str]:
    if len(text) <= max_len:
        return [text]
    chunks = []
    current = ""
    for line in text.split("\\n"):
        if len(current) + len(line) + 1 <= max_len:
            current = (current + "\\n" + line) if current else line
        else:
            if current:
                chunks.append(current)
            if len(line) > max_len:
                for i in range(0, len(line), max_len):
                    chunks.append(line[i:i + max_len])
                current = ""
            else:
                current = line
    if current:
        chunks.append(current)
    return chunks


_MD_SPECIAL = r"_*[]()~`>#+-=|{}.!"


def escape_md(text: str) -> str:
    return re.sub(f"([{re.escape(_MD_SPECIAL)}])", r"\\\\\\1", text)


def truncate(text: str, max_len: int = 100) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + "..."


class RateLimiter:
    def __init__(self):
        self._data: Dict[int, List[float]] = {}
        self._lock = threading.Lock()

    def check(self, user_id: int, max_per_min: int = 20) -> bool:
        now = time.time()
        with self._lock:
            ts = self._data.get(user_id, [])
            ts = [t for t in ts if now - t < 60]
            if len(ts) >= max_per_min:
                self._data[user_id] = ts
                return False
            ts.append(now)
            self._data[user_id] = ts
            return True


rate_limiter = RateLimiter()


def now_iso() -> str:
    return datetime.now(TZ).isoformat()


def today_str() -> str:
    return datetime.now(TZ).date().isoformat()


def format_xp_bar(xp: int, level: int, levels_map: Dict) -> str:
    sorted_lvls = sorted(levels_map.items())
    next_lvl = None
    for lvl, data in sorted_lvls:
        if lvl > level:
            next_lvl = (lvl, data["xp"])
            break
    if not next_lvl:
        return "🏆 أقصى مستوى"
    current_threshold = levels_map.get(level, {}).get("xp", 0)
    span = next_lvl[1] - current_threshold
    progress = xp - current_threshold
    ratio = progress / span if span > 0 else 1.0
    ratio = max(0.0, min(1.0, ratio))
    filled = int(ratio * 10)
    bar = "█" * filled + "░" * (10 - filled)
    return f"{bar} {xp}/{next_lvl[1]} XP"


def parse_int(text: str, default=None):
    try:
        return int(text.strip())
    except (ValueError, AttributeError):
        return default
'''


print("✅ تم تجهيز: config, database, models, utils")
print("⚠️ الملف مقطوع هنا — كمّل مع الرد التالي")


# ============================================================
# keyboards.py
# ============================================================
FILES["keyboards.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Keyboards — كل الأزرار."""

from typing import Dict, Any

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import CHANNEL_URL, SUPPORT_URL, SUPPORTED_MODELS, PERSONAS, DIALECTS, CHALLENGE_CATEGORIES


def main_menu_kb(user_id: int, is_admin: bool = False) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("💬 محادثة جديدة", callback_data="new_conv"),
        InlineKeyboardButton("📋 محادثاتي", callback_data="list_convs"),
        InlineKeyboardButton("🎭 شخصيتي", callback_data="persona_menu"),
        InlineKeyboardButton("🧠 ذاكرتي", callback_data="memory_menu"),
        InlineKeyboardButton("🏆 مستواي", callback_data="xp_menu"),
        InlineKeyboardButton("🔥 السلسلة", callback_data="streak_menu"),
        InlineKeyboardButton("👥 إحالاتي", callback_data="referral_menu"),
        InlineKeyboardButton("🏅 المتصدرين", callback_data="leaderboard"),
        InlineKeyboardButton("🎨 المعرض", callback_data="gallery_menu"),
        InlineKeyboardButton("🎯 التحديات", callback_data="challenges_menu"),
        InlineKeyboardButton("🚪 غرف AI", callback_data="rooms_menu"),
        InlineKeyboardButton("👥 توأمي", callback_data="twin_menu"),
        InlineKeyboardButton("🧬 تحليل شخصيتي", callback_data="dna_menu"),
        InlineKeyboardButton("🛠️ الأدوات", callback_data="tools_menu"),
        InlineKeyboardButton("⚙️ الإعدادات", callback_data="settings"),
        InlineKeyboardButton("ℹ️ معلومات", callback_data="info"),
        InlineKeyboardButton("📢 قناتنا", url=CHANNEL_URL),
        InlineKeyboardButton("📞 الدعم", url=SUPPORT_URL),
    )
    if is_admin:
        kb.add(InlineKeyboardButton("🛡️ لوحة الأدمن", callback_data="admin_panel"))
    return kb


def settings_kb(user: Dict[str, Any]) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    model_name = SUPPORTED_MODELS.get(user["model"], user["model"])
    persona_name = PERSONAS.get(user["persona"], {}).get("name", user["persona"])
    dialect_name = DIALECTS.get(user["dialect"], {}).get("name", user["dialect"])
    stream = "✅" if user["streaming_enabled"] else "❌"
    mem = "✅" if user["memory_enabled"] else "❌"
    kb.add(
        InlineKeyboardButton(f"🤖 النموذج: {model_name}", callback_data="change_model"),
        InlineKeyboardButton(f"🎭 الشخصية: {persona_name}", callback_data="persona_menu"),
        InlineKeyboardButton(f"🗣️ اللهجة: {dialect_name}", callback_data="dialect_menu"),
        InlineKeyboardButton(f"📡 التدفق: {stream}", callback_data="toggle_stream"),
        InlineKeyboardButton(f"🧠 الذاكرة: {mem}", callback_data="toggle_memory"),
        InlineKeyboardButton("🔄 إعادة تعيين", callback_data="reset_settings"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def models_kb(current: str = "auto") -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    items = list(SUPPORTED_MODELS.items())
    for i in range(0, len(items), 2):
        row = []
        for j in range(2):
            if i + j < len(items):
                code, name = items[i + j]
                mark = "✓ " if code == current else ""
                row.append(InlineKeyboardButton(mark + name, callback_data=f"set_model_{code}"))
        kb.row(*row)
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="settings"))
    return kb


def personas_kb(current: str = "friendly") -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    items = list(PERSONAS.items())
    for i in range(0, len(items), 2):
        row = []
        for j in range(2):
            if i + j < len(items):
                code, data = items[i + j]
                mark = "✓ " if code == current else ""
                row.append(InlineKeyboardButton(mark + data["name"], callback_data=f"set_persona_{code}"))
        kb.row(*row)
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="settings"))
    return kb


def dialects_kb(current: str = "egy") -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    items = list(DIALECTS.items())
    for i in range(0, len(items), 2):
        row = []
        for j in range(2):
            if i + j < len(items):
                code, data = items[i + j]
                mark = "✓ " if code == current else ""
                row.append(InlineKeyboardButton(mark + data["name"], callback_data=f"set_dialect_{code}"))
        kb.row(*row)
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="settings"))
    return kb


def xp_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🏅 المتصدرين", callback_data="leaderboard"),
        InlineKeyboardButton("🔥 سلسلتي", callback_data="streak_menu"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def streak_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    return kb


def leaderboard_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🏆 XP", callback_data="leaderboard_xp"),
        InlineKeyboardButton("🔥 Streak", callback_data="leaderboard_streak"),
        InlineKeyboardButton("👥 إحالات", callback_data="leaderboard_ref"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def referral_menu_kb(bot_username: str, user_id: int) -> InlineKeyboardMarkup:
    ref_link = f"https://t.me/{bot_username}?start=ref_{user_id}"
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(
            "📤 شارك رابطك",
            url=f"https://t.me/share/url?url={ref_link}&text=جرب البوت ده، رهيب!",
        ),
        InlineKeyboardButton("🏅 المتصدرين", callback_data="leaderboard_ref"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def gallery_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🖼️ تصفح", callback_data="gallery_browse"),
        InlineKeyboardButton("➕ إضافة", callback_data="gallery_add"),
        InlineKeyboardButton("⭐ إبداعاتي", callback_data="gallery_mine"),
        InlineKeyboardButton("🏆 الأفضل", callback_data="gallery_top"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def challenges_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🎯 التحدي الحالي", callback_data="challenges_current"),
        InlineKeyboardButton("🏆 الفائزون", callback_data="challenges_winners"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def rooms_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("➕ إنشاء غرفة", callback_data="rooms_create"),
        InlineKeyboardButton("🚪 غرفي", callback_data="rooms_mine"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def twin_menu_kb(has_twin: bool) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    if has_twin:
        kb.add(
            InlineKeyboardButton("💬 اسأل توأمك", callback_data="twin_chat"),
            InlineKeyboardButton("📤 شارك", callback_data="twin_share"),
            InlineKeyboardButton("🗑️ حذف", callback_data="twin_delete"),
        )
    else:
        kb.add(InlineKeyboardButton("🧬 درّب توأمك", callback_data="twin_train"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    return kb


def dna_menu_kb(has_analysis: bool) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    if has_analysis:
        kb.add(
            InlineKeyboardButton("🧬 تحليلي", callback_data="dna_view"),
            InlineKeyboardButton("📤 شارك التحليل", callback_data="dna_share"),
            InlineKeyboardButton("🔄 تحليل جديد", callback_data="dna_analyze"),
        )
    else:
        kb.add(InlineKeyboardButton("🧬 حلل شخصيتي", callback_data="dna_analyze"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    return kb


def tools_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🌐 ترجمة", callback_data="tool_translate"),
        InlineKeyboardButton("📄 تلخيص PDF", callback_data="tool_summarize"),
        InlineKeyboardButton("🖼️ OCR (استخراج نص)", callback_data="tool_ocr"),
        InlineKeyboardButton("🔍 بحث ويب", callback_data="tool_search"),
        InlineKeyboardButton("💻 شرح كود", callback_data="tool_explain_code"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def admin_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📊 إحصائيات", callback_data="admin_stats"),
        InlineKeyboardButton("👥 المستخدمين", callback_data="admin_users"),
        InlineKeyboardButton("🚫 المحظورين", callback_data="admin_banned"),
        InlineKeyboardButton("📢 إذاعة", callback_data="admin_broadcast"),
        InlineKeyboardButton("🎯 التحديات", callback_data="admin_challenges"),
        InlineKeyboardButton("⚙️ الإعدادات", callback_data="admin_settings"),
        InlineKeyboardButton("📝 السجل", callback_data="admin_audit"),
        InlineKeyboardButton("🔄 تحديث", callback_data="admin_panel"),
        InlineKeyboardButton("🔙 رجوع", callback_data="back_main"),
    )
    return kb


def admin_settings_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🔧 وضع الصيانة", callback_data="admin_toggle_maintenance"),
        InlineKeyboardButton("📢 الاشتراك الإجباري", callback_data="admin_toggle_forcesub"),
        InlineKeyboardButton("🧠 الذاكرة العامة", callback_data="admin_toggle_memory"),
        InlineKeyboardButton("🏆 XP", callback_data="admin_toggle_xp"),
        InlineKeyboardButton("🔥 Streak", callback_data="admin_toggle_streak"),
        InlineKeyboardButton("👥 الإحالات", callback_data="admin_toggle_referral"),
        InlineKeyboardButton("🎨 المعرض", callback_data="admin_toggle_gallery"),
        InlineKeyboardButton("🎯 التحديات", callback_data="admin_toggle_challenges"),
        InlineKeyboardButton("🚪 الغرف", callback_data="admin_toggle_rooms"),
        InlineKeyboardButton("👥 التوائم", callback_data="admin_toggle_twins"),
        InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"),
    )
    return kb
'''


# ============================================================
# handlers/__init__.py
# ============================================================
FILES["handlers/__init__.py"] = '''# handlers package
'''


# ============================================================
# handlers/user.py
# ============================================================
FILES["handlers/user.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""User handlers — start, menu, chat, onboarding."""

import logging
import threading
import uuid
from datetime import datetime
from typing import Optional

from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from config import (
    ADMIN_ID, CHANNEL_URL, BOT_NAME, TZ, MAX_MESSAGES_PER_MIN,
    SUPPORTED_MODELS, PERSONAS, DIALECTS, LEVELS, XP_PER_MESSAGE,
    STREAK_REWARDS, AI_STREAM_EDIT_THROTTLE, REFERRAL_REWARDS, XP_PER_LEVEL,
)
from models import ai_client, AIError
from utils import rate_limiter, split_message, now_iso
from keyboards import main_menu_kb, settings_kb, models_kb, personas_kb, dialects_kb

log = logging.getLogger("handler.user")

user_state = {}
_state_lock = threading.Lock()
user_conversations = {}
user_current_conv = {}

bot = None
db = None


def _build_system_prompt(user_row) -> str:
    parts = []
    persona = PERSONAS.get(user_row["persona"], PERSONAS["friendly"])
    dialect = DIALECTS.get(user_row["dialect"], DIALECTS["egy"])
    parts.append(persona["prompt"])
    parts.append(dialect["prompt"])
    if user_row["bot_name"]:
        parts.append(f"اسم المستخدم يناديك '{user_row['bot_name']}'.")
    if user_row["memory_enabled"]:
        mem = db.memory_all(user_row["user_id"])
        if mem:
            parts.append("معلومات عن المستخدم:")
            for k, v in mem.items():
                parts.append(f"- {k}: {v}")
    return "\\n".join(parts)


def _ensure_conversation(user_id: int) -> Optional[str]:
    with _state_lock:
        convs = user_conversations.get(user_id)
    if convs and user_current_conv.get(user_id) in convs:
        return user_current_conv[user_id]
    headers = ai_client.new_conversation_headers()
    if not headers:
        return None
    cid = str(uuid.uuid4())[:8]
    with _state_lock:
        user_conversations.setdefault(user_id, {})[cid] = {
            "conv_id": cid,
            "conversation_id": None,
            "parent_message_id": None,
            "headers": headers,
            "created_at": now_iso(),
            "messages_count": 0,
        }
        user_current_conv[user_id] = cid
    return cid


def cmd_start(message: Message):
    user = message.from_user
    row = db.ensure_user(user.id, user.username or "", user.first_name or "", user.last_name or "")

    if message.text and " " in message.text:
        payload = message.text.split(" ", 1)[1].strip()
        if payload.startswith("ref_") and row["referred_by"] is None:
            try:
                referrer = int(payload[4:])
                if referrer != user.id and db.get_user(referrer):
                    db.update_user(user.id, referred_by=referrer)
                    new_count = db.add_referral(referrer)
                    try:
                        reward_msg = ""
                        if new_count in REFERRAL_REWARDS:
                            reward_msg = f"\\n🎁 {REFERRAL_REWARDS[new_count]['msg']}!"
                        bot.send_message(
                            referrer,
                            f"🎉 صديقك انضم عبر رابطك!\\n👥 إجمالياتك: {new_count}{reward_msg}",
                        )
                    except Exception:
                        pass
            except Exception:
                pass

    if not row["bot_name"] and row["messages_count"] == 0:
        _start_onboarding(message.chat.id, user.id)
        return

    _show_main_menu(message.chat.id, user.id, edit_message_id=None)


def _start_onboarding(chat_id: int, user_id: int):
    user_state[user_id] = {"step": "onboarding_name", "data": {}}
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🎭 اختر شخصية", callback_data="onb_persona"),
        InlineKeyboardButton("🗣️ اختر لهجة", callback_data="onb_dialect"),
        InlineKeyboardButton("⏭️ تخطي", callback_data="onb_skip"),
    )
    bot.send_message(
        chat_id,
        "🎉 *أهلاً بيك!*\\n\\n"
        "خلينا نخصص البوت على مزاجك:\\n\\n"
        "1️⃣ ابعتلي اسم تحبني أناديك بيه\\n"
        "2️⃣ اختار شخصية\\n"
        "3️⃣ اختار لهجة\\n\\n"
        "✍️ *ابعت الاسم دلوقتي:*",
        parse_mode="Markdown",
        reply_markup=kb,
    )


def _show_main_menu(chat_id: int, user_id: int, edit_message_id: Optional[int] = None):
    row = db.get_user(user_id)
    if not row:
        return
    level_name = LEVELS.get(row["level"], {}).get("name", "🌱")
    text = (
        f"✨ *{BOT_NAME}* ✨\\n\\n"
        f"👤 {row['first_name'] or 'صديقي'}\\n"
        f"🏆 {level_name} — المستوى {row['level']}\\n"
        f"⚡ XP: *{row['xp']}*\\n"
        f"🔥 السلسلة: *{row['streak']}* يوم\\n\\n"
        f"💬 *ابعت رسالتك للبدء، أو اختار من القائمة:*"
    )
    kb = main_menu_kb(user_id, is_admin=(user_id == ADMIN_ID))
    if edit_message_id:
        try:
            bot.edit_message_text(text, chat_id, edit_message_id, parse_mode="Markdown", reply_markup=kb)
            return
        except Exception:
            pass
    bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=kb)


def _send_ai(chat_id: int, user_id: int, text: str):
    row = db.get_user(user_id)
    if not row:
        return
    conv_id = _ensure_conversation(user_id)
    if not conv_id:
        bot.send_message(chat_id, "❌ فشل الاتصال بـ AI. حاول تاني.")
        return
    with _state_lock:
        conv = user_conversations[user_id][conv_id]

    system_prompt = _build_system_prompt(row)
    streaming = bool(row["streaming_enabled"])
    model = row["model"]
    if model not in SUPPORTED_MODELS:
        model = "auto"

    try:
        bot.send_chat_action(chat_id, "typing")
    except Exception:
        pass

    full_text = ""
    sent_msg = None
    last_edit = 0.0
    conv_id_remote = conv["conversation_id"]

    try:
        for event in ai_client.send_message(
            headers=conv["headers"], model=model, message_text=text,
            conversation_id=conv["conversation_id"],
            parent_message_id=conv["parent_message_id"],
            streaming=streaming, system_prompt=system_prompt,
        ):
            if event["type"] == "delta":
                full_text = event["text"]
                if event.get("conv_id") and not conv_id_remote:
                    conv_id_remote = event["conv_id"]
                now = datetime.now(TZ).timestamp()
                if sent_msg is None:
                    sent_msg = bot.send_message(chat_id, full_text[:4000])
                    last_edit = now
                elif streaming and (now - last_edit) >= AI_STREAM_EDIT_THROTTLE and len(full_text) <= 4000:
                    try:
                        bot.edit_message_text(full_text, chat_id, sent_msg.message_id)
                        last_edit = now
                    except Exception:
                        pass
            elif event["type"] == "done":
                full_text = event["full"]
                if event.get("message_id"):
                    conv["parent_message_id"] = event["message_id"]
                if event.get("conv_id"):
                    conv_id_remote = event["conv_id"]
                conv["conversation_id"] = conv_id_remote
                break
    except AIError as e:
        bot.send_message(chat_id, f"❌ {e}")
        return
    except Exception as e:
        log.exception("AI send error")
        bot.send_message(chat_id, f"❌ خطأ: {str(e)[:100]}")
        return

    if not full_text:
        bot.send_message(chat_id, "⚠️ لم يتم استلام رد.")
        return

    chunks = split_message(full_text)
    if sent_msg is None:
        for chunk in chunks:
            bot.send_message(chat_id, chunk)
    elif len(chunks) > 1:
        try:
            bot.edit_message_text(chunks[0], chat_id, sent_msg.message_id)
        except Exception:
            pass
        import time as _t
        for chunk in chunks[1:]:
            _t.sleep(0.4)
            bot.send_message(chat_id, chunk)
    else:
        try:
            bot.edit_message_text(chunks[0], chat_id, sent_msg.message_id)
        except Exception:
            pass

    conv["messages_count"] += 1
    db.execute(
        "INSERT INTO messages_history (user_id, conv_id, user_message, bot_response, model, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, conv_id, text, full_text, model, now_iso()),
    )
    existing = db.fetchone("SELECT 1 FROM conversations WHERE conv_id = ?", (conv_id,))
    if existing:
        db.execute(
            "UPDATE conversations SET messages_count = ?, last_activity = ? WHERE conv_id = ?",
            (conv["messages_count"], now_iso(), conv_id),
        )
    else:
        db.execute(
            "INSERT INTO conversations (user_id, conv_id, model, created_at, messages_count, last_activity) VALUES (?, ?, ?, ?, ?, ?)",
            (user_id, conv_id, model, now_iso(), conv["messages_count"], now_iso()),
        )

    db.update_user(user_id, messages_count=row["messages_count"] + 1)
    if db.get_bool("xp_enabled", True):
        new_xp, new_lvl, leveled_up = db.add_xp(user_id, XP_PER_MESSAGE)
        if leveled_up:
            lvl_name = LEVELS.get(leveled_up, {}).get("name", "")
            try:
                bot.send_message(chat_id, f"🎉 *ترقية!* وصلت للمستوى {leveled_up} — {lvl_name}", parse_mode="Markdown")
            except Exception:
                pass
    if db.get_bool("streak_enabled", True):
        new_streak, is_new = db.update_streak(user_id)
        if is_new and new_streak in STREAK_REWARDS:
            reward = STREAK_REWARDS[new_streak]
            db.add_xp(user_id, reward["xp"])
            try:
                bot.send_message(chat_id, f"🔥 سلسلة *{new_streak}* أيام! {reward['msg']}", parse_mode="Markdown")
            except Exception:
                pass


def handle_text(message: Message):
    user_id = message.from_user.id
    text = (message.text or "").strip()
    if not text:
        return
    st = user_state.get(user_id)
    if st and st.get("step") == "onboarding_name":
        if len(text) > 30:
            bot.reply_to(message, "❌ الاسم طويل جداً (30 حرف بحد أقصى)")
            return
        db.update_user(user_id, bot_name=text)
        user_state[user_id]["step"] = "onboarding_done"
        bot.reply_to(message, f"✅ تمام، هبقى أناديك *{text}*\\n\\nاختار شخصية ولهجة أو تخطى.", parse_mode="Markdown")
        _start_onboarding_after_name(message.chat.id, user_id)
        return
    if text.startswith("/"):
        bot.reply_to(message, "❓ أمر غير معروف. ابعت رسالتك عادي.")
        return
    if db.get_bool("maintenance", False) and user_id != ADMIN_ID:
        bot.reply_to(message, "🔧 البوت في وضع الصيانة.")
        return
    max_pm = int(db.get_setting("max_messages_per_min", str(MAX_MESSAGES_PER_MIN)))
    if not rate_limiter.check(user_id, max_pm):
        bot.reply_to(message, "⏱️ استنى شوية، رسائل كتير.")
        return
    _send_ai(message.chat.id, user_id, text)


def _start_onboarding_after_name(chat_id: int, user_id: int):
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton("🎭 اختر شخصية", callback_data="onb_persona"),
        InlineKeyboardButton("🗣️ اختر لهجة", callback_data="onb_dialect"),
        InlineKeyboardButton("✅ خلصت", callback_data="onb_skip"),
    )
    bot.send_message(chat_id, "كمل تخصيصك:", reply_markup=kb)


def cb_back_main(call: CallbackQuery):
    _show_main_menu(call.message.chat.id, call.from_user.id, edit_message_id=call.message.message_id)
    bot.answer_callback_query(call.id)


def cb_new_conv(call: CallbackQuery):
    user_id = call.from_user.id
    headers = ai_client.new_conversation_headers()
    if not headers:
        bot.answer_callback_query(call.id, "❌ فشل الإنشاء", show_alert=True)
        return
    cid = str(uuid.uuid4())[:8]
    with _state_lock:
        user_conversations.setdefault(user_id, {})[cid] = {
            "conv_id": cid, "conversation_id": None, "parent_message_id": None,
            "headers": headers, "created_at": now_iso(), "messages_count": 0,
        }
        user_current_conv[user_id] = cid
    bot.answer_callback_query(call.id, f"✅ محادثة جديدة: {cid}")


def cb_list_convs(call: CallbackQuery):
    user_id = call.from_user.id
    with _state_lock:
        convs = list(user_conversations.get(user_id, {}).items())
    if not convs:
        bot.answer_callback_query(call.id, "📭 لا توجد محادثات", show_alert=True)
        return
    kb = InlineKeyboardMarkup(row_width=1)
    for cid, conv in convs[-10:]:
        mark = "✓ " if user_current_conv.get(user_id) == cid else ""
        kb.add(InlineKeyboardButton(f"{mark}💬 {cid} ({conv['messages_count']})", callback_data=f"select_conv_{cid}"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    try:
        bot.edit_message_text("📋 *محادثاتك:*", call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, "📋 *محادثاتك:*", parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_select_conv(call: CallbackQuery):
    cid = call.data.replace("select_conv_", "")
    user_id = call.from_user.id
    with _state_lock:
        if cid in user_conversations.get(user_id, {}):
            user_current_conv[user_id] = cid
            bot.answer_callback_query(call.id, f"✅ {cid}")
        else:
            bot.answer_callback_query(call.id, "❌ غير موجودة", show_alert=True)


def cb_info(call: CallbackQuery):
    text = (
        f"ℹ️ *{BOT_NAME}*\\n\\n"
        f"🤖 نموذج ذكاء اصطناعي متقدم\\n"
        f"🎭 شخصيات متعددة\\n"
        f"🧠 ذاكرة طويلة\\n"
        f"🏆 نظام مستويات\\n"
        f"👥 إحالات\\n"
        f"🎨 معرض إبداعات\\n"
        f"🎯 تحديات\\n"
        f"🚪 غرف AI جماعية\\n"
        f"👥 توأم رقمي\\n"
        f"🧬 تحليل شخصية\\n\\n"
        f"📢 [قناتنا]({CHANNEL_URL})"
    )
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(InlineKeyboardButton("📢 القناة", url=CHANNEL_URL))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb, disable_web_page_preview=True)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb, disable_web_page_preview=True)
    bot.answer_callback_query(call.id)


def cb_settings(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    if not row:
        return
    user_dict = dict(row)
    try:
        bot.edit_message_text("⚙️ *الإعدادات:*", call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=settings_kb(user_dict))
    except Exception:
        bot.send_message(call.message.chat.id, "⚙️ *الإعدادات:*", parse_mode="Markdown",
                         reply_markup=settings_kb(user_dict))
    bot.answer_callback_query(call.id)


def cb_change_model(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    try:
        bot.edit_message_text("🤖 *اختر النموذج:*", call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=models_kb(row["model"] if row else "auto"))
    except Exception:
        bot.send_message(call.message.chat.id, "🤖 *اختر النموذج:*", parse_mode="Markdown",
                         reply_markup=models_kb(row["model"] if row else "auto"))
    bot.answer_callback_query(call.id)


def cb_set_model(call: CallbackQuery):
    model = call.data.replace("set_model_", "")
    if model not in SUPPORTED_MODELS:
        bot.answer_callback_query(call.id, "❌ نموذج غير مدعوم", show_alert=True)
        return
    db.update_user(call.from_user.id, model=model)
    bot.answer_callback_query(call.id, f"✅ {SUPPORTED_MODELS[model]}")
    cb_settings(call)


def cb_toggle_stream(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    new_val = 0 if row["streaming_enabled"] else 1
    db.update_user(call.from_user.id, streaming_enabled=new_val)
    bot.answer_callback_query(call.id, "✅ تم التبديل")
    cb_settings(call)


def cb_toggle_memory(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    new_val = 0 if row["memory_enabled"] else 1
    db.update_user(call.from_user.id, memory_enabled=new_val)
    bot.answer_callback_query(call.id, "✅ تم التبديل")
    cb_settings(call)


def cb_reset_settings(call: CallbackQuery):
    db.update_user(call.from_user.id, model="auto", persona="friendly",
                   dialect="egy", streaming_enabled=1, memory_enabled=1)
    bot.answer_callback_query(call.id, "✅ تمت إعادة التعيين")
    cb_settings(call)


def cb_onb_persona(call: CallbackQuery):
    user_id = call.from_user.id
    user_state.setdefault(user_id, {"step": "onboarding", "data": {}})["data"]["onb_stage"] = "persona"
    try:
        bot.edit_message_text("🎭 *اختر شخصيتك:*", call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=personas_kb())
    except Exception:
        bot.send_message(call.message.chat.id, "🎭 *اختر شخصيتك:*", parse_mode="Markdown", reply_markup=personas_kb())
    bot.answer_callback_query(call.id)


def cb_onb_dialect(call: CallbackQuery):
    user_id = call.from_user.id
    user_state.setdefault(user_id, {"step": "onboarding", "data": {}})["data"]["onb_stage"] = "dialect"
    try:
        bot.edit_message_text("🗣️ *اختر لهجتك:*", call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=dialects_kb())
    except Exception:
        bot.send_message(call.message.chat.id, "🗣️ *اختر لهجتك:*", parse_mode="Markdown", reply_markup=dialects_kb())
    bot.answer_callback_query(call.id)


def cb_onb_skip(call: CallbackQuery):
    user_state.pop(call.from_user.id, None)
    _show_main_menu(call.message.chat.id, call.from_user.id, edit_message_id=call.message.message_id)
    bot.answer_callback_query(call.id, "✅")


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_message_handler(cmd_start, commands=["start"])
    bot.register_callback_query_handler(cb_back_main, func=lambda c: c.data == "back_main")
    bot.register_callback_query_handler(cb_new_conv, func=lambda c: c.data == "new_conv")
    bot.register_callback_query_handler(cb_list_convs, func=lambda c: c.data == "list_convs")
    bot.register_callback_query_handler(cb_select_conv, func=lambda c: c.data.startswith("select_conv_"))
    bot.register_callback_query_handler(cb_info, func=lambda c: c.data == "info")
    bot.register_callback_query_handler(cb_settings, func=lambda c: c.data == "settings")
    bot.register_callback_query_handler(cb_change_model, func=lambda c: c.data == "change_model")
    bot.register_callback_query_handler(cb_set_model, func=lambda c: c.data.startswith("set_model_"))
    bot.register_callback_query_handler(cb_toggle_stream, func=lambda c: c.data == "toggle_stream")
    bot.register_callback_query_handler(cb_toggle_memory, func=lambda c: c.data == "toggle_memory")
    bot.register_callback_query_handler(cb_reset_settings, func=lambda c: c.data == "reset_settings")
    bot.register_callback_query_handler(cb_onb_persona, func=lambda c: c.data == "onb_persona")
    bot.register_callback_query_handler(cb_onb_dialect, func=lambda c: c.data == "onb_dialect")
    bot.register_callback_query_handler(cb_onb_skip, func=lambda c: c.data == "onb_skip")
'''


# ============================================================
# handlers/persona.py
# ============================================================
FILES["handlers/persona.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Persona + Dialect handlers."""

import logging

from telebot.types import CallbackQuery

from config import PERSONAS, DIALECTS
from keyboards import personas_kb, dialects_kb, settings_kb

log = logging.getLogger("handler.persona")

bot = None
db = None


def _show(call: CallbackQuery, text: str, kb):
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)


def cb_persona_menu(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    _show(call, "🎭 *اختر شخصيتك:*", personas_kb(row["persona"] if row else "friendly"))
    bot.answer_callback_query(call.id)


def cb_dialect_menu(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    _show(call, "🗣️ *اختر لهجتك:*", dialects_kb(row["dialect"] if row else "egy"))
    bot.answer_callback_query(call.id)


def cb_set_persona(call: CallbackQuery):
    code = call.data.replace("set_persona_", "")
    if code not in PERSONAS:
        bot.answer_callback_query(call.id, "❌ غير مدعوم", show_alert=True)
        return
    db.update_user(call.from_user.id, persona=code)
    bot.answer_callback_query(call.id, f"✅ {PERSONAS[code]['name']}")
    row = db.get_user(call.from_user.id)
    _show(call, "⚙️ *الإعدادات:*", settings_kb(dict(row)))


def cb_set_dialect(call: CallbackQuery):
    code = call.data.replace("set_dialect_", "")
    if code not in DIALECTS:
        bot.answer_callback_query(call.id, "❌ غير مدعوم", show_alert=True)
        return
    db.update_user(call.from_user.id, dialect=code)
    bot.answer_callback_query(call.id, f"✅ {DIALECTS[code]['name']}")
    row = db.get_user(call.from_user.id)
    _show(call, "⚙️ *الإعدادات:*", settings_kb(dict(row)))


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_persona_menu, func=lambda c: c.data == "persona_menu")
    bot.register_callback_query_handler(cb_dialect_menu, func=lambda c: c.data == "dialect_menu")
    bot.register_callback_query_handler(cb_set_persona, func=lambda c: c.data.startswith("set_persona_"))
    bot.register_callback_query_handler(cb_set_dialect, func=lambda c: c.data.startswith("set_dialect_"))
'''


# ============================================================
# handlers/memory.py
# ============================================================
FILES["handlers/memory.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Memory handlers."""

import logging

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import MEMORY_MAX_ITEMS

log = logging.getLogger("handler.memory")

bot = None
db = None

state = {}


def cb_memory_menu(call: CallbackQuery):
    user_id = call.from_user.id
    mem = db.memory_all(user_id)
    if not mem:
        text = "🧠 *ذاكرتي*\\n\\n📭 لا توجد معلومات محفوظة.\\n\\nأضف معلومات عنك (اسمك، شغلك، اهتماماتك) عشان أفتكرها."
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(InlineKeyboardButton("➕ إضافة", callback_data="memory_add"),
               InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    else:
        lines = [f"🧠 *ذاكرتي* ({len(mem)}/{MEMORY_MAX_ITEMS})\\n"]
        for k, v in list(mem.items())[:10]:
            lines.append(f"• *{k}*: {v[:60]}")
        text = "\\n".join(lines)
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(InlineKeyboardButton("➕ إضافة", callback_data="memory_add"),
               InlineKeyboardButton("🗑️ حذف الكل", callback_data="memory_clear"),
               InlineKeyboardButton("🔙 رجوع", callback_data="back_main"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_memory_add(call: CallbackQuery):
    user_id = call.from_user.id
    mem = db.memory_all(user_id)
    if len(mem) >= MEMORY_MAX_ITEMS:
        bot.answer_callback_query(call.id, f"❌ وصلت للحد الأقصى ({MEMORY_MAX_ITEMS})", show_alert=True)
        return
    state[user_id] = {"step": "memory_add_key"}
    try:
        bot.edit_message_text(
            "🧠 *إضافة معلومة*\\n\\n"
            "✍️ ابعت *المفتاح* (مثل: اسمي، شغلي، مدينتي)\\n\\n"
            "أو /cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="memory_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_memory_clear(call: CallbackQuery):
    db.memory_clear(call.from_user.id)
    bot.answer_callback_query(call.id, "🗑️ تم الحذف")
    cb_memory_menu(call)


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if not text:
        return True
    if text == "/cancel":
        state.pop(user_id, None)
        bot.reply_to(message, "❌ تم الإلغاء")
        return True
    if s["step"] == "memory_add_key":
        if len(text) > 30:
            bot.reply_to(message, "❌ المفتاح طويل (30 حرف)")
            return True
        s["key"] = text
        s["step"] = "memory_add_value"
        bot.reply_to(message, f"✍️ ابعت *قيمة* \\"{text}\\":", parse_mode="Markdown")
        return True
    if s["step"] == "memory_add_value":
        if len(text) > 200:
            bot.reply_to(message, "❌ القيمة طويلة (200 حرف)")
            return True
        db.memory_set(user_id, s["key"], text)
        bot.reply_to(message, f"✅ اتحفظت: *{s['key']}*", parse_mode="Markdown")
        state.pop(user_id, None)
        return True
    return True


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_memory_menu, func=lambda c: c.data == "memory_menu")
    bot.register_callback_query_handler(cb_memory_add, func=lambda c: c.data == "memory_add")
    bot.register_callback_query_handler(cb_memory_clear, func=lambda c: c.data == "memory_clear")
'''


print("✅ تم تجهيز: keyboards, user, persona, memory")
print("⚠️ الملف مقطوع هنا — كمّل مع الرد التالي")


# ============================================================
# handlers/xp.py
# ============================================================
FILES["handlers/xp.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""XP, Levels, Streak, Leaderboard handlers."""

import logging

from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from config import LEVELS, XP_PER_MESSAGE, STREAK_REWARDS
from keyboards import xp_menu_kb, streak_menu_kb, leaderboard_kb
from utils import format_xp_bar

log = logging.getLogger("handler.xp")

bot = None
db = None


def cb_xp_menu(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    if not row:
        bot.answer_callback_query(call.id, "❌")
        return
    level_name = LEVELS.get(row["level"], {}).get("name", "🌱")
    bar = format_xp_bar(row["xp"], row["level"], LEVELS)
    rank_row = db.fetchone("SELECT COUNT(*) + 1 AS rank FROM users WHERE xp > ?", (row["xp"],))
    rank = rank_row["rank"] if rank_row else "?"
    text = (
        f"🏆 *مستواي*\\n\\n"
        f"👤 {row['first_name'] or 'صديقي'}\\n"
        f"⭐ المستوى: *{row['level']}* — {level_name}\\n"
        f"⚡ XP: *{row['xp']}*\\n"
        f"📊 {bar}\\n"
        f"🏅 ترتيبي: *#{rank}*\\n"
        f"🔥 السلسلة: *{row['streak']}* يوم\\n\\n"
        f"💡 كل رسالة = *{XP_PER_MESSAGE}* XP"
    )
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=xp_menu_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=xp_menu_kb())
    bot.answer_callback_query(call.id)


def cb_streak_menu(call: CallbackQuery):
    row = db.get_user(call.from_user.id)
    if not row:
        bot.answer_callback_query(call.id, "❌")
        return
    lines = [f"🔥 *السلسلة*\\n\\n📅 سلسلتك الحالية: *{row['streak']}* يوم\\n"]
    if row["streak"] == 0:
        lines.append("💡 ابعت رسالة كل يوم عشان تحافظ على السلسلة.")
    else:
        nxt = None
        for d in sorted(STREAK_REWARDS.keys()):
            if d > row["streak"]:
                nxt = d
                break
        if nxt:
            lines.append(f"🎯 السلسلة القادمة: *{nxt}* يوم → {STREAK_REWARDS[nxt]['msg']}")
        else:
            lines.append("👑 أنت أسطورة!")
    text = "\\n".join(lines)
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=streak_menu_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=streak_menu_kb())
    bot.answer_callback_query(call.id)


def cb_leaderboard(call: CallbackQuery):
    text = "🏅 *المتصدرين*\\n\\nاختار الترتيب:"
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=leaderboard_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=leaderboard_kb())
    bot.answer_callback_query(call.id)


def cb_leaderboard_xp(call: CallbackQuery):
    rows = db.fetchall("SELECT user_id, first_name, username, xp, level FROM users ORDER BY xp DESC LIMIT 15")
    if not rows:
        bot.answer_callback_query(call.id, "لا يوجد بعد")
        return
    lines = ["🏆 *أعلى XP*\\n"]
    medals = ["🥇", "🥈", "🥉"]
    for i, r in enumerate(rows, 1):
        medal = medals[i - 1] if i <= 3 else f"{i}."
        name = r["first_name"] or r["username"] or f"User{r['user_id']}"
        lvl = LEVELS.get(r["level"], {}).get("name", "")
        lines.append(f"{medal} {name[:20]} — {r['xp']} XP {lvl}")
    text = "\\n".join(lines)
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="leaderboard"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_leaderboard_streak(call: CallbackQuery):
    rows = db.fetchall("SELECT user_id, first_name, username, streak FROM users WHERE streak > 0 ORDER BY streak DESC LIMIT 15")
    if not rows:
        bot.answer_callback_query(call.id, "لا يوجد بعد")
        return
    lines = ["🔥 *أطول سلاسل*\\n"]
    for i, r in enumerate(rows, 1):
        name = r["first_name"] or r["username"] or f"User{r['user_id']}"
        lines.append(f"{i}. {name[:20]} — {r['streak']} يوم")
    text = "\\n".join(lines)
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="leaderboard"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_leaderboard_ref(call: CallbackQuery):
    rows = db.fetchall("SELECT user_id, first_name, username, referrals FROM users WHERE referrals > 0 ORDER BY referrals DESC LIMIT 15")
    if not rows:
        bot.answer_callback_query(call.id, "لا يوجد بعد")
        return
    lines = ["👥 *أكثر الإحالات*\\n"]
    for i, r in enumerate(rows, 1):
        name = r["first_name"] or r["username"] or f"User{r['user_id']}"
        lines.append(f"{i}. {name[:20]} — {r['referrals']} إحالة")
    text = "\\n".join(lines)
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="leaderboard"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_xp_menu, func=lambda c: c.data == "xp_menu")
    bot.register_callback_query_handler(cb_streak_menu, func=lambda c: c.data == "streak_menu")
    bot.register_callback_query_handler(cb_leaderboard, func=lambda c: c.data == "leaderboard")
    bot.register_callback_query_handler(cb_leaderboard_xp, func=lambda c: c.data == "leaderboard_xp")
    bot.register_callback_query_handler(cb_leaderboard_streak, func=lambda c: c.data == "leaderboard_streak")
    bot.register_callback_query_handler(cb_leaderboard_ref, func=lambda c: c.data == "leaderboard_ref")
'''


# ============================================================
# handlers/referral.py
# ============================================================
FILES["handlers/referral.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Referral system."""

import logging

from telebot.types import CallbackQuery

from config import REFERRAL_REWARDS
from keyboards import referral_menu_kb

log = logging.getLogger("handler.referral")

bot = None
db = None


def cb_referral_menu(call: CallbackQuery):
    user_id = call.from_user.id
    row = db.get_user(user_id)
    if not row:
        bot.answer_callback_query(call.id, "❌")
        return
    try:
        me = bot.get_me()
        bot_username = me.username
    except Exception:
        bot_username = "your_bot"

    ref_link = f"https://t.me/{bot_username}?start=ref_{user_id}"
    refs = row["referrals"]
    lines = [
        f"👥 *نظام الإحالات*\\n",
        f"🔗 *رابطك:*\\n`{ref_link}`\\n",
        f"📊 *إحصائياتك:*\\n",
        f"• إحالاتك: *{refs}*",
    ]
    next_milestone = None
    for m in sorted(REFERRAL_REWARDS.keys()):
        if m > refs:
            next_milestone = m
            break
    if next_milestone:
        remaining = next_milestone - refs
        lines.append(f"• باقي *{remaining}* للحصول على {REFERRAL_REWARDS[next_milestone]['msg']}")
    else:
        lines.append("👑 حصلت على كل المكافآت!")

    lines.append("\\n🎁 *المكافآت:*")
    for m, data in sorted(REFERRAL_REWARDS.items()):
        mark = "✅" if refs >= m else "🔒"
        lines.append(f"{mark} {m} إحالة → {data['msg']}")

    text = "\\n".join(lines)
    kb = referral_menu_kb(bot_username, user_id)
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_referral_menu, func=lambda c: c.data == "referral_menu")
'''


# ============================================================
# handlers/groups.py
# ============================================================
FILES["handlers/groups.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Group AI Rooms."""

import logging
import secrets
import string

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME
from utils import now_iso
from models import ai_client, AIError

log = logging.getLogger("handler.groups")

bot = None
db = None

state = {}


def _gen_code() -> str:
    alphabet = string.ascii_uppercase + string.digits
    while True:
        code = "".join(secrets.choice(alphabet) for _ in range(6))
        if not db.fetchone("SELECT 1 FROM rooms WHERE room_code = ?", (code,)):
            return code


def cb_rooms_menu(call: CallbackQuery):
    user_id = call.from_user.id
    mine = db.fetchall(
        "SELECT room_code, title, created_at FROM rooms WHERE owner_id = ? AND is_active = 1 ORDER BY id DESC LIMIT 5",
        (user_id,),
    )
    lines = ["🚪 *غرف AI*\\n", "💡 الغرف بتخليك تسأل AI مع أصحابك في نفس الوقت."]
    if mine:
        lines.append("\\n*غرفك:*")
        for r in mine:
            lines.append(f"• `{r['room_code']}` — {r['title']}")
    text = "\\n".join(lines)
    from keyboards import rooms_menu_kb
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=rooms_menu_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=rooms_menu_kb())
    bot.answer_callback_query(call.id)


def cb_rooms_create(call: CallbackQuery):
    user_id = call.from_user.id
    state[user_id] = {"step": "room_title"}
    try:
        bot.edit_message_text(
            "🚪 *غرفة جديدة*\\n\\n"
            "✍️ ابعت اسم الغرفة (مثال: شلة الشغل)\\n\\n"
            "أو /cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="rooms_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_rooms_mine(call: CallbackQuery):
    user_id = call.from_user.id
    rooms = db.fetchall(
        "SELECT id, room_code, title FROM rooms WHERE owner_id = ? AND is_active = 1 ORDER BY id DESC LIMIT 10",
        (user_id,),
    )
    if not rooms:
        bot.answer_callback_query(call.id, "📭 لا توجد غرف", show_alert=True)
        return
    kb = InlineKeyboardMarkup(row_width=1)
    for r in rooms:
        kb.add(InlineKeyboardButton(f"🚪 {r['title']} ({r['room_code']})", callback_data=f"room_open_{r['room_code']}"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="rooms_menu"))
    try:
        bot.edit_message_text("🚪 *غرفك:*", call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, "🚪 *غرفك:*", parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_room_open(call: CallbackQuery):
    code = call.data.replace("room_open_", "")
    room = db.fetchone("SELECT * FROM rooms WHERE room_code = ? AND is_active = 1", (code,))
    if not room:
        bot.answer_callback_query(call.id, "❌ الغرفة غير موجودة", show_alert=True)
        return
    members = db.fetchone("SELECT COUNT(*) AS c FROM room_members WHERE room_id = ?", (room["id"],))
    count = members["c"] if members else 0
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("💬 دخول", callback_data=f"room_chat_{code}"),
        InlineKeyboardButton("📤 دعوة", callback_data=f"room_invite_{code}"),
        InlineKeyboardButton("🚪 خروج", callback_data=f"room_leave_{code}"),
        InlineKeyboardButton("🔙 رجوع", callback_data="rooms_menu"),
    )
    text = (
        f"🚪 *{room['title']}*\\n\\n"
        f"🆔 الكود: `{room['room_code']}`\\n"
        f"👥 الأعضاء: {count}\\n"
        f"📅 أُنشئت: {room['created_at'][:10]}"
    )
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_room_chat(call: CallbackQuery):
    code = call.data.replace("room_chat_", "")
    room = db.fetchone("SELECT * FROM rooms WHERE room_code = ? AND is_active = 1", (code,))
    if not room:
        bot.answer_callback_query(call.id, "❌ الغرفة غير موجودة", show_alert=True)
        return
    user_id = call.from_user.id
    db.execute("INSERT OR IGNORE INTO room_members (room_id, user_id, joined_at) VALUES (?, ?, ?)",
               (room["id"], user_id, now_iso()))
    state[user_id] = {"step": "room_chat", "room_code": code}
    try:
        bot.edit_message_text(
            f"💬 *أنت في غرفة {room['title']}*\\n\\n"
            f"✍️ ابعت سؤالك، AI هيرد عليك.\\n\\n"
            f"أو /leave للخروج.",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🚪 خروج", callback_data=f"room_leave_{code}")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_room_invite(call: CallbackQuery):
    code = call.data.replace("room_invite_", "")
    room = db.fetchone("SELECT * FROM rooms WHERE room_code = ? AND is_active = 1", (code,))
    if not room:
        bot.answer_callback_query(call.id, "❌", show_alert=True)
        return
    try:
        me = bot.get_me()
        share_url = f"https://t.me/{me.username}?start=room_{code}"
    except Exception:
        share_url = ""
    kb = InlineKeyboardMarkup()
    if share_url:
        kb.add(InlineKeyboardButton(
            "📤 مشاركة الرابط",
            url=f"https://t.me/share/url?url={share_url}&text=انضم لغرفتي في {BOT_NAME}!",
        ))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data=f"room_open_{code}"))
    try:
        bot.edit_message_text(
            f"📤 *دعوة للغرفة*\\n\\n"
            f"🆔 الكود: `{room['room_code']}`\\n"
            f"شارك الرابط مع أصحابك.",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=kb,
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_room_leave(call: CallbackQuery):
    code = call.data.replace("room_leave_", "")
    room = db.fetchone("SELECT * FROM rooms WHERE room_code = ?", (code,))
    if room:
        db.execute("DELETE FROM room_members WHERE room_id = ? AND user_id = ?", (room["id"], call.from_user.id))
    state.pop(call.from_user.id, None)
    bot.answer_callback_query(call.id, "✅ خرجت")
    cb_rooms_menu(call)


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if text == "/cancel" or text == "/leave":
        state.pop(user_id, None)
        bot.reply_to(message, "✅ تم الخروج")
        return True
    if s["step"] == "room_title":
        if len(text) < 2 or len(text) > 40:
            bot.reply_to(message, "❌ اسم الغرفة 2-40 حرف")
            return True
        code = _gen_code()
        db.execute("INSERT INTO rooms (room_code, owner_id, title, created_at, is_active) VALUES (?, ?, ?, ?, 1)",
                   (code, user_id, text, now_iso()))
        room = db.fetchone("SELECT * FROM rooms WHERE room_code = ?", (code,))
        db.execute("INSERT OR IGNORE INTO room_members (room_id, user_id, joined_at) VALUES (?, ?, ?)",
                   (room["id"], user_id, now_iso()))
        state.pop(user_id, None)
        bot.reply_to(message, f"✅ *تم إنشاء الغرفة!*\\n\\n🆔 الكود: `{code}`\\n📤 شاركه مع أصحابك.", parse_mode="Markdown")
        return True
    if s["step"] == "room_chat":
        code = s["room_code"]
        room = db.fetchone("SELECT * FROM rooms WHERE room_code = ? AND is_active = 1", (code,))
        if not room:
            state.pop(user_id, None)
            bot.reply_to(message, "❌ الغرفة اتقفلت")
            return True
        db.execute("INSERT OR IGNORE INTO room_members (room_id, user_id, joined_at) VALUES (?, ?, ?)",
                   (room["id"], user_id, now_iso()))
        headers = ai_client.new_conversation_headers()
        if not headers:
            bot.reply_to(message, "❌ فشل الاتصال")
            return True
        try:
            bot.send_chat_action(message.chat.id, "typing")
            full = ""
            for event in ai_client.send_message(
                headers=headers, model="auto", message_text=text,
                streaming=False, system_prompt="أنت مساعد في غرفة جماعية، ردودك مختصرة ومفيدة.",
            ):
                if event["type"] == "done":
                    full = event["full"]
                    break
            if not full:
                bot.reply_to(message, "⚠️ لم يتم استلام رد")
                return True
            bot.reply_to(message, f"🤖 {full[:4000]}")
        except AIError as e:
            bot.reply_to(message, f"❌ {e}")
        except Exception as e:
            log.exception("room chat error")
            bot.reply_to(message, f"❌ {str(e)[:100]}")
        return True
    return True


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_rooms_menu, func=lambda c: c.data == "rooms_menu")
    bot.register_callback_query_handler(cb_rooms_create, func=lambda c: c.data == "rooms_create")
    bot.register_callback_query_handler(cb_rooms_mine, func=lambda c: c.data == "rooms_mine")
    bot.register_callback_query_handler(cb_room_open, func=lambda c: c.data.startswith("room_open_"))
    bot.register_callback_query_handler(cb_room_chat, func=lambda c: c.data.startswith("room_chat_"))
    bot.register_callback_query_handler(cb_room_invite, func=lambda c: c.data.startswith("room_invite_"))
    bot.register_callback_query_handler(cb_room_leave, func=lambda c: c.data.startswith("room_leave_"))
'''


# ============================================================
# handlers/gallery.py
# ============================================================
FILES["handlers/gallery.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gallery."""

import logging

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from utils import now_iso, truncate
from keyboards import gallery_menu_kb

log = logging.getLogger("handler.gallery")

bot = None
db = None

state = {}


def cb_gallery_menu(call: CallbackQuery):
    user_id = call.from_user.id
    total = db.fetchone("SELECT COUNT(*) AS c FROM gallery")["c"]
    mine = db.fetchone("SELECT COUNT(*) AS c FROM gallery WHERE user_id = ?", (user_id,))["c"]
    text = (
        f"🎨 *المعرض*\\n\\n"
        f"📊 إجمالي الإبداعات: *{total}*\\n"
        f"⭐ إبداعاتك: *{mine}*\\n\\n"
        f"💡 شارك أفضل ردود AI، قصص، أكواد، صور."
    )
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=gallery_menu_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=gallery_menu_kb())
    bot.answer_callback_query(call.id)


def _show_items(call: CallbackQuery, rows, title: str):
    user_id = call.from_user.id
    kb = InlineKeyboardMarkup(row_width=1)
    text = title + "\\n\\n"
    for r in rows:
        title_str = truncate(r["title"], 40)
        content_str = truncate(r["content"], 80)
        text += f"*{title_str}*\\n{content_str}\\n❤️ {r['likes']} | 🏷️ {r['category']}\\n\\n"
        already = db.fetchone("SELECT 1 FROM gallery_likes WHERE user_id = ? AND item_id = ?", (user_id, r["id"]))
        if already:
            kb.add(InlineKeyboardButton(f"✅ {title_str[:15]} (❤️ {r['likes']})", callback_data=f"gal_unlike_{r['id']}"))
        else:
            kb.add(InlineKeyboardButton(f"❤️ {title_str[:15]}", callback_data=f"gal_like_{r['id']}"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="gallery_menu"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)


def cb_gallery_browse(call: CallbackQuery):
    rows = db.fetchall("SELECT * FROM gallery ORDER BY id DESC LIMIT 5")
    if not rows:
        bot.answer_callback_query(call.id, "📭 لا توجد إبداعات بعد", show_alert=True)
        return
    _show_items(call, rows, "🖼️ *أحدث الإبداعات*")


def cb_gallery_top(call: CallbackQuery):
    rows = db.fetchall("SELECT * FROM gallery ORDER BY likes DESC, id DESC LIMIT 5")
    if not rows:
        bot.answer_callback_query(call.id, "📭 لا توجد إبداعات بعد", show_alert=True)
        return
    _show_items(call, rows, "🏆 *الأفضل*")


def cb_gallery_mine(call: CallbackQuery):
    user_id = call.from_user.id
    rows = db.fetchall("SELECT * FROM gallery WHERE user_id = ? ORDER BY id DESC LIMIT 5", (user_id,))
    if not rows:
        bot.answer_callback_query(call.id, "📭 لا توجد إبداعات لك بعد", show_alert=True)
        return
    _show_items(call, rows, "⭐ *إبداعاتي*")


def cb_gallery_like(call: CallbackQuery):
    item_id = int(call.data.replace("gal_like_", ""))
    user_id = call.from_user.id
    item = db.fetchone("SELECT * FROM gallery WHERE id = ?", (item_id,))
    if not item:
        bot.answer_callback_query(call.id, "❌")
        return
    try:
        db.execute("INSERT INTO gallery_likes (user_id, item_id) VALUES (?, ?)", (user_id, item_id))
        db.execute("UPDATE gallery SET likes = likes + 1 WHERE id = ?", (item_id,))
        bot.answer_callback_query(call.id, "❤️")
    except Exception:
        bot.answer_callback_query(call.id, "✅ سبق الإعجاب")
    cb_gallery_browse(call)


def cb_gallery_unlike(call: CallbackQuery):
    item_id = int(call.data.replace("gal_unlike_", ""))
    user_id = call.from_user.id
    try:
        db.execute("DELETE FROM gallery_likes WHERE user_id = ? AND item_id = ?", (user_id, item_id))
        db.execute("UPDATE gallery SET likes = MAX(0, likes - 1) WHERE id = ?", (item_id,))
        bot.answer_callback_query(call.id, "✅ ألغيت الإعجاب")
    except Exception:
        bot.answer_callback_query(call.id, "❌")
    cb_gallery_browse(call)


def cb_gallery_add(call: CallbackQuery):
    user_id = call.from_user.id
    mine = db.fetchone("SELECT COUNT(*) AS c FROM gallery WHERE user_id = ?", (user_id,))["c"]
    if mine >= 20:
        bot.answer_callback_query(call.id, "❌ وصلت للحد الأقصى (20)", show_alert=True)
        return
    state[user_id] = {"step": "gallery_title"}
    try:
        bot.edit_message_text(
            "➕ *إضافة إبداع*\\n\\n"
            "✍️ ابعت *عنوان* الإبداع (2-60 حرف)\\n\\n"
            "أو /cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="gallery_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_gallery_category(call: CallbackQuery):
    cat = call.data.replace("gal_cat_", "")
    user_id = call.from_user.id
    s = state.get(user_id)
    if not s or "title" not in s or "content" not in s:
        bot.answer_callback_query(call.id, "❌ انتهت الجلسة", show_alert=True)
        return
    db.execute(
        "INSERT INTO gallery (user_id, title, content, category, likes, created_at) VALUES (?, ?, ?, ?, 0, ?)",
        (user_id, s["title"], s["content"], cat, now_iso()),
    )
    state.pop(user_id, None)
    bot.answer_callback_query(call.id, "✅ تم النشر")
    try:
        bot.edit_message_text(
            f"✅ *تم النشر!*\\n\\n📌 {s['title']}\\n🏷️ {cat}",
            call.message.chat.id, call.message.message_id,
            parse_mode="Markdown", reply_markup=gallery_menu_kb(),
        )
    except Exception:
        pass


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if text == "/cancel":
        state.pop(user_id, None)
        bot.reply_to(message, "❌ تم الإلغاء")
        return True
    if s["step"] == "gallery_title":
        if len(text) < 2 or len(text) > 60:
            bot.reply_to(message, "❌ العنوان 2-60 حرف")
            return True
        s["title"] = text
        s["step"] = "gallery_content"
        bot.reply_to(message, "✍️ ابعت *المحتوى* (حتى 2000 حرف):", parse_mode="Markdown")
        return True
    if s["step"] == "gallery_content":
        if len(text) < 10:
            bot.reply_to(message, "❌ المحتوى قصير جداً (10 أحرف على الأقل)")
            return True
        if len(text) > 2000:
            bot.reply_to(message, "❌ المحتوى طويل (2000 حرف بحد أقصى)")
            return True
        s["content"] = text
        s["step"] = "gallery_category"
        kb = InlineKeyboardMarkup(row_width=2)
        for cat in ["story", "code", "poem", "idea", "other"]:
            kb.add(InlineKeyboardButton(cat, callback_data=f"gal_cat_{cat}"))
        bot.reply_to(message, "🏷️ اختار التصنيف:", reply_markup=kb)
        return True
    return True


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_gallery_menu, func=lambda c: c.data == "gallery_menu")
    bot.register_callback_query_handler(cb_gallery_browse, func=lambda c: c.data == "gallery_browse")
    bot.register_callback_query_handler(cb_gallery_top, func=lambda c: c.data == "gallery_top")
    bot.register_callback_query_handler(cb_gallery_mine, func=lambda c: c.data == "gallery_mine")
    bot.register_callback_query_handler(cb_gallery_like, func=lambda c: c.data.startswith("gal_like_"))
    bot.register_callback_query_handler(cb_gallery_unlike, func=lambda c: c.data.startswith("gal_unlike_"))
    bot.register_callback_query_handler(cb_gallery_add, func=lambda c: c.data == "gallery_add")
    bot.register_callback_query_handler(cb_gallery_category, func=lambda c: c.data.startswith("gal_cat_"))
'''


# ============================================================
# handlers/challenges.py
# ============================================================
FILES["handlers/challenges.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Challenges."""

import logging
from datetime import datetime

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import TZ
from utils import now_iso, truncate
from keyboards import challenges_menu_kb

log = logging.getLogger("handler.challenges")

bot = None
db = None

state = {}


def _get_active_challenge():
    now = datetime.now(TZ).isoformat()
    return db.fetchone(
        "SELECT * FROM challenges WHERE is_active = 1 AND start_at <= ? AND end_at >= ? ORDER BY id DESC LIMIT 1",
        (now, now),
    )


def cb_challenges_menu(call: CallbackQuery):
    active = _get_active_challenge()
    if active:
        text = (
            f"🎯 *التحدي الحالي*\\n\\n"
            f"🏷️ {active['title']}\\n"
            f"📂 التصنيف: {active['category']}\\n"
            f"📅 ينتهي: {active['end_at'][:10]}\\n\\n"
            f"📝 {active['description']}\\n\\n"
            f"💡 شارك إبداعك وخلي الناس تصوت!"
        )
    else:
        text = "🎯 *التحديات*\\n\\n📭 لا يوجد تحدٍ نشط حالياً."
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=challenges_menu_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=challenges_menu_kb())
    bot.answer_callback_query(call.id)


def cb_challenges_current(call: CallbackQuery):
    active = _get_active_challenge()
    if not active:
        bot.answer_callback_query(call.id, "📭 لا يوجد تحدٍ نشط", show_alert=True)
        return
    user_id = call.from_user.id
    entry = db.fetchone(
        "SELECT * FROM challenge_entries WHERE challenge_id = ? AND user_id = ?",
        (active["id"], user_id),
    )
    entries_count = db.fetchone(
        "SELECT COUNT(*) AS c FROM challenge_entries WHERE challenge_id = ?", (active["id"],)
    )["c"]

    lines = [
        f"🎯 *{active['title']}*\\n",
        f"📂 {active['category']}",
        f"📝 {active['description']}\\n",
        f"👥 المشاركات: {entries_count}",
        f"📅 ينتهي: {active['end_at'][:10]}\\n",
    ]
    kb = InlineKeyboardMarkup(row_width=1)
    if entry:
        lines.append(f"✅ أنت مشارك بالفعل\\n📝 {truncate(entry['content'], 100)}")
        kb.add(InlineKeyboardButton("🗳️ شوف المشاركات", callback_data=f"chal_entries_{active['id']}"))
    else:
        lines.append("💡 شارك إبداعك الآن!")
        kb.add(InlineKeyboardButton("✍️ شارك", callback_data=f"chal_join_{active['id']}"))
        kb.add(InlineKeyboardButton("🗳️ شوف المشاركات", callback_data=f"chal_entries_{active['id']}"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="challenges_menu"))

    try:
        bot.edit_message_text("\\n".join(lines), call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, "\\n".join(lines), parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_chal_join(call: CallbackQuery):
    challenge_id = int(call.data.replace("chal_join_", ""))
    user_id = call.from_user.id
    ch = db.fetchone("SELECT * FROM challenges WHERE id = ?", (challenge_id,))
    if not ch or not ch["is_active"]:
        bot.answer_callback_query(call.id, "❌", show_alert=True)
        return
    already = db.fetchone(
        "SELECT 1 FROM challenge_entries WHERE challenge_id = ? AND user_id = ?", (challenge_id, user_id)
    )
    if already:
        bot.answer_callback_query(call.id, "✅ أنت مشارك بالفعل", show_alert=True)
        return
    state[user_id] = {"step": "chal_entry", "challenge_id": challenge_id}
    try:
        bot.edit_message_text(
            f"✍️ *شارك في: {ch['title']}*\\n\\n"
            f"ابعت إبداعك (حتى 1500 حرف)\\n\\n"
            f"أو /cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="challenges_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_chal_entries(call: CallbackQuery):
    challenge_id = int(call.data.replace("chal_entries_", ""))
    rows = db.fetchall(
        "SELECT * FROM challenge_entries WHERE challenge_id = ? ORDER BY votes DESC, id ASC LIMIT 10",
        (challenge_id,),
    )
    if not rows:
        bot.answer_callback_query(call.id, "📭 لا توجد مشاركات بعد", show_alert=True)
        return
    user_id = call.from_user.id
    text = "🗳️ *المشاركات*\\n\\n"
    kb = InlineKeyboardMarkup(row_width=1)
    for r in rows:
        author = db.get_user(r["user_id"])
        name = author["first_name"] if author else f"User{r['user_id']}"
        already_voted = db.fetchone(
            "SELECT 1 FROM challenge_votes WHERE user_id = ? AND entry_id = ?", (user_id, r["id"])
        )
        mark = "✅" if already_voted else "👍"
        text += f"*{name[:15]}* — {r['votes']} صوت\\n"
        text += f"{truncate(r['content'], 80)}\\n\\n"
        kb.add(InlineKeyboardButton(
            f"{mark} {name[:12]} ({r['votes']})", callback_data=f"chal_vote_{r['id']}"
        ))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="challenges_current"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_chal_vote(call: CallbackQuery):
    entry_id = int(call.data.replace("chal_vote_", ""))
    user_id = call.from_user.id
    entry = db.fetchone("SELECT * FROM challenge_entries WHERE id = ?", (entry_id,))
    if not entry:
        bot.answer_callback_query(call.id, "❌", show_alert=True)
        return
    if entry["user_id"] == user_id:
        bot.answer_callback_query(call.id, "❌ ما ينفعش تصوت لنفسك", show_alert=True)
        return
    try:
        db.execute("INSERT INTO challenge_votes (user_id, entry_id) VALUES (?, ?)", (user_id, entry_id))
        db.execute("UPDATE challenge_entries SET votes = votes + 1 WHERE id = ?", (entry_id,))
        bot.answer_callback_query(call.id, "👍")
    except Exception:
        bot.answer_callback_query(call.id, "✅ سبق التصويت")
    cb_chal_entries(call)


def cb_challenges_winners(call: CallbackQuery):
    rows = db.fetchall(
        "SELECT ce.*, c.title AS ch_title FROM challenge_entries ce JOIN challenges c ON c.id = ce.challenge_id WHERE c.is_active = 0 ORDER BY ce.votes DESC LIMIT 10"
    )
    if not rows:
        bot.answer_callback_query(call.id, "📭 لا يوجد فائزون بعد", show_alert=True)
        return
    text = "🏆 *الفائزون*\\n\\n"
    for r in rows:
        author = db.get_user(r["user_id"])
        name = author["first_name"] if author else f"User{r['user_id']}"
        text += f"🥇 {name[:15]} — {r['votes']} صوت\\n"
        text += f"🎯 {r['ch_title']}\\n"
        text += f"📝 {truncate(r['content'], 80)}\\n\\n"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="challenges_menu"))
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if text == "/cancel":
        state.pop(user_id, None)
        bot.reply_to(message, "❌ تم الإلغاء")
        return True
    if s["step"] == "chal_entry":
        if len(text) < 10:
            bot.reply_to(message, "❌ المحتوى قصير جداً")
            return True
        if len(text) > 1500:
            bot.reply_to(message, "❌ المحتوى طويل (1500 حرف)")
            return True
        try:
            db.execute(
                "INSERT INTO challenge_entries (challenge_id, user_id, content, votes, created_at) VALUES (?, ?, ?, 0, ?)",
                (s["challenge_id"], user_id, text, now_iso()),
            )
            state.pop(user_id, None)
            bot.reply_to(message, "✅ *تمت المشاركة!*\\n\\nالناس هتصوت لك.", parse_mode="Markdown")
        except Exception as e:
            log.exception("challenge entry error")
            bot.reply_to(message, f"❌ خطأ: {str(e)[:100]}")
        return True
    return True


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_challenges_menu, func=lambda c: c.data == "challenges_menu")
    bot.register_callback_query_handler(cb_challenges_current, func=lambda c: c.data == "challenges_current")
    bot.register_callback_query_handler(cb_chal_join, func=lambda c: c.data.startswith("chal_join_"))
    bot.register_callback_query_handler(cb_chal_entries, func=lambda c: c.data.startswith("chal_entries_"))
    bot.register_callback_query_handler(cb_chal_vote, func=lambda c: c.data.startswith("chal_vote_"))
    bot.register_callback_query_handler(cb_challenges_winners, func=lambda c: c.data == "challenges_winners")
'''


print("✅ تم تجهيز: xp, referral, groups, gallery, challenges")
print("⚠️ الملف مقطوع هنا — كمّل مع الرد التالي (الأخير)")


# ============================================================
# handlers/dna.py
# ============================================================
FILES["handlers/dna.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DNA — تحليل شخصية من محادثات المستخدم."""

import logging

from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from utils import now_iso
from models import ai_client, AIError
from keyboards import dna_menu_kb

log = logging.getLogger("handler.dna")

bot = None
db = None

DNA_PROMPT = """حلل شخصية المستخدم ده بناءً على محادثاته مع AI.

المحادثات:
{conversations}

اعمل تحليل مختصر (200-300 كلمة) بأسلوب ممتع، بالعامية المصرية، مقسم لكذا جزء:
1. 🎯 نمط التفكير
2. 💡 الاهتمامات
3. 🗣️ أسلوب التواصل
4. ⚡ نقاط القوة
5. 🌟 جملة تعريفية

ما تذكرش إنك AI، اتكلم كأنك حد بيفهم فيه الشخصية. كن إيجابي ومشجع."""


def _get_analysis(user_id: int):
    return db.memory_get(user_id, "_dna_analysis")


def _save_analysis(user_id: int, text: str):
    db.memory_set(user_id, "_dna_analysis", text)
    db.memory_set(user_id, "_dna_analysis_at", now_iso())


def cb_dna_menu(call: CallbackQuery):
    user_id = call.from_user.id
    analysis = _get_analysis(user_id)
    text = (
        f"🧬 *تحليل شخصيتي*\\n\\n"
        f"💡 خليني أحلل شخصيتك من محادثاتك معايا!\\n"
        f"هستخدم آخر 50 رسالة عشان أفهمك.\\n\\n"
        f"🔒 *خصوصية:* التحليل بيتحفظ في حسابك بس."
    )
    if analysis:
        text += f"\\n\\n✅ *عندك تحليل بالفعل*"
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=dna_menu_kb(bool(analysis)))
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=dna_menu_kb(bool(analysis)))
    bot.answer_callback_query(call.id)


def cb_dna_view(call: CallbackQuery):
    user_id = call.from_user.id
    analysis = _get_analysis(user_id)
    if not analysis:
        bot.answer_callback_query(call.id, "❌ لا يوجد تحليل", show_alert=True)
        return
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🔄 تحليل جديد", callback_data="dna_analyze"),
        InlineKeyboardButton("📤 شارك", callback_data="dna_share"),
        InlineKeyboardButton("🔙 رجوع", callback_data="dna_menu"),
    )
    try:
        bot.edit_message_text(f"🧬 *تحليلك:*\\n\\n{analysis[:4000]}",
                              call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, f"🧬 *تحليلك:*\\n\\n{analysis[:4000]}",
                         parse_mode="Markdown", reply_markup=kb)
    bot.answer_callback_query(call.id)


def cb_dna_analyze(call: CallbackQuery):
    user_id = call.from_user.id
    rows = db.fetchall(
        "SELECT user_message, bot_response FROM messages_history WHERE user_id = ? ORDER BY id DESC LIMIT 50",
        (user_id,),
    )
    if len(rows) < 5:
        bot.answer_callback_query(call.id, "❌ محتاج 5 رسايل على الأقل", show_alert=True)
        return
    try:
        bot.edit_message_text("🧬 *جاري التحليل...*\\n\\n⏳ ممكن ياخد شوية.",
                              call.message.chat.id, call.message.message_id, parse_mode="Markdown")
    except Exception:
        pass
    bot.answer_callback_query(call.id)

    convs_text = []
    for r in reversed(rows):
        convs_text.append(f"المستخدم: {r['user_message'][:300]}")
        convs_text.append(f"AI: {r['bot_response'][:300]}")
    convs_str = "\\n".join(convs_text[:100])
    prompt = DNA_PROMPT.format(conversations=convs_str)

    headers = ai_client.new_conversation_headers()
    if not headers:
        bot.send_message(call.from_user.id, "❌ فشل الاتصال")
        return
    try:
        full = ""
        for event in ai_client.send_message(
            headers=headers, model="gpt-4o-mini", message_text=prompt, streaming=False,
        ):
            if event["type"] == "done":
                full = event["full"]
                break
        if not full:
            bot.send_message(call.from_user.id, "⚠️ فشل التحليل")
            return
        _save_analysis(user_id, full)
        kb = InlineKeyboardMarkup(row_width=2)
        kb.add(
            InlineKeyboardButton("🔄 تحليل جديد", callback_data="dna_analyze"),
            InlineKeyboardButton("📤 شارك", callback_data="dna_share"),
            InlineKeyboardButton("🔙 رجوع", callback_data="dna_menu"),
        )
        bot.send_message(call.from_user.id, f"🧬 *تحليلك:*\\n\\n{full[:4000]}",
                         parse_mode="Markdown", reply_markup=kb)
    except AIError as e:
        bot.send_message(call.from_user.id, f"❌ {e}")
    except Exception as e:
        log.exception("DNA analysis error")
        bot.send_message(call.from_user.id, f"❌ {str(e)[:100]}")


def cb_dna_share(call: CallbackQuery):
    user_id = call.from_user.id
    analysis = _get_analysis(user_id)
    if not analysis:
        bot.answer_callback_query(call.id, "❌ لا يوجد تحليل", show_alert=True)
        return
    text = f"🧬 *تحليلي الشخصي*:\\n\\n{analysis[:500]}"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📤 شارك التحليل", url="https://t.me/share/url?url=https://t.me&text=تحليلي"))
    bot.answer_callback_query(call.id)
    bot.send_message(user_id, "📤 *شارك تحليلك:*", parse_mode="Markdown", reply_markup=kb)


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_dna_menu, func=lambda c: c.data == "dna_menu")
    bot.register_callback_query_handler(cb_dna_view, func=lambda c: c.data == "dna_view")
    bot.register_callback_query_handler(cb_dna_analyze, func=lambda c: c.data == "dna_analyze")
    bot.register_callback_query_handler(cb_dna_share, func=lambda c: c.data == "dna_share")
'''


# ============================================================
# handlers/twins.py
# ============================================================
FILES["handlers/twins.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Twins — توأم رقمي."""

import logging
import secrets
import string

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from utils import now_iso
from models import ai_client, AIError
from keyboards import twin_menu_kb

log = logging.getLogger("handler.twins")

bot = None
db = None

state = {}


def _gen_slug() -> str:
    alphabet = string.ascii_lowercase + string.digits
    while True:
        slug = "".join(secrets.choice(alphabet) for _ in range(8))
        if not db.fetchone("SELECT 1 FROM twins WHERE share_slug = ?", (slug,)):
            return slug


def _get_twin(user_id: int):
    return db.fetchone("SELECT * FROM twins WHERE user_id = ?", (user_id,))


def cb_twin_menu(call: CallbackQuery):
    user_id = call.from_user.id
    twin = _get_twin(user_id)
    if twin:
        text = (
            f"👥 *توأمك الرقمي*\\n\\n"
            f"✅ مدرب على *{twin['samples_count']}* رسالة\\n"
            f"📅 آخر تدريب: {twin['trained_at'][:10]}\\n\\n"
            f"💬 اسأل توأمك، هو بيرد بأسلوبك.\\n"
            f"📤 أو شاركه مع أصحابك."
        )
    else:
        text = (
            f"👥 *توأم رقمي*\\n\\n"
            f"💡 ده نسخة مصغرة منك، بتتعلم من محادثاتك.\\n\\n"
            f"🎯 لما تدرّبه:\\n"
            f"• يرد بأسلوبك\\n"
            f"• يعرف اهتماماتك\\n"
            f"• يقدر يشارك مع أصحابك\\n\\n"
            f"⏱️ التدريب ياخد 30 ثانية."
        )
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=twin_menu_kb(bool(twin)))
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=twin_menu_kb(bool(twin)))
    bot.answer_callback_query(call.id)


def cb_twin_train(call: CallbackQuery):
    user_id = call.from_user.id
    rows = db.fetchall("SELECT user_message FROM messages_history WHERE user_id = ? ORDER BY id DESC LIMIT 100", (user_id,))
    if len(rows) < 10:
        bot.answer_callback_query(call.id, "❌ محتاج 10 رسايل على الأقل", show_alert=True)
        return
    try:
        bot.edit_message_text("🧬 *جاري تدريب توأمك...*\\n\\n⏳ ممكن ياخد شوية.",
                              call.message.chat.id, call.message.message_id, parse_mode="Markdown")
    except Exception:
        pass
    bot.answer_callback_query(call.id)

    samples = "\\n".join(r["user_message"][:200] for r in rows[:50])
    prompt = f"""حلل أسلوب كتابة المستخدم ده من رسائله:

{samples[:3000]}

اكتب "شخصية" مختصرة (150-200 كلمة) تصف:
1. أسلوب الكتابة
2. الكلمات المفتاحية
3. المواضيع المفضلة
4. طريقة التفكير

خليها بصيغة "المستخدم ده..."، وكن دقيق."""
    headers = ai_client.new_conversation_headers()
    if not headers:
        bot.send_message(user_id, "❌ فشل الاتصال")
        return
    try:
        full = ""
        for event in ai_client.send_message(
            headers=headers, model="gpt-4o-mini", message_text=prompt, streaming=False,
        ):
            if event["type"] == "done":
                full = event["full"]
                break
        if not full:
            bot.send_message(user_id, "⚠️ فشل التدريب")
            return
        twin = _get_twin(user_id)
        if twin:
            db.execute("UPDATE twins SET personality = ?, trained_at = ?, samples_count = ? WHERE user_id = ?",
                       (full, now_iso(), len(rows), user_id))
        else:
            slug = _gen_slug()
            db.execute("INSERT INTO twins (user_id, personality, trained_at, samples_count, share_slug) VALUES (?, ?, ?, ?, ?)",
                       (user_id, full, now_iso(), len(rows), slug))
        bot.send_message(
            user_id,
            f"✅ *تم تدريب توأمك!*\\n\\n📊 دربته على *{len(rows)}* رسالة\\n🎯 دلوقتي اسأله أي حاجة.",
            parse_mode="Markdown", reply_markup=twin_menu_kb(True),
        )
    except AIError as e:
        bot.send_message(user_id, f"❌ {e}")
    except Exception as e:
        log.exception("Twin training error")
        bot.send_message(user_id, f"❌ {str(e)[:100]}")


def cb_twin_chat(call: CallbackQuery):
    user_id = call.from_user.id
    twin = _get_twin(user_id)
    if not twin:
        bot.answer_callback_query(call.id, "❌ لا يوجد توأم", show_alert=True)
        return
    state[user_id] = {"step": "twin_chat"}
    try:
        bot.edit_message_text(
            "💬 *اسأل توأمك*\\n\\n✍️ ابعت سؤالك، توأمك هيرد بأسلوبك.\\n\\n/cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="twin_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_twin_share(call: CallbackQuery):
    user_id = call.from_user.id
    twin = _get_twin(user_id)
    if not twin:
        bot.answer_callback_query(call.id, "❌ لا يوجد توأم", show_alert=True)
        return
    try:
        me = bot.get_me()
        url = f"https://t.me/{me.username}?start=twin_{twin['share_slug']}"
    except Exception:
        url = ""
    kb = InlineKeyboardMarkup()
    if url:
        kb.add(InlineKeyboardButton("📤 مشاركة", url=f"https://t.me/share/url?url={url}&text=اسأل توأمي الرقمي!"))
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="twin_menu"))
    try:
        bot.edit_message_text(
            f"📤 *شارك توأمك*\\n\\n🔗 الرابط:\\n`{url}`\\n\\nأي حد يفتح الرابط يقدر يسأل توأمك.",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=kb,
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_twin_delete(call: CallbackQuery):
    user_id = call.from_user.id
    db.execute("DELETE FROM twins WHERE user_id = ?", (user_id,))
    bot.answer_callback_query(call.id, "🗑️ تم الحذف")
    cb_twin_menu(call)


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if text == "/cancel":
        state.pop(user_id, None)
        bot.reply_to(message, "❌ تم الإلغاء")
        return True
    if s["step"] == "twin_chat":
        twin = _get_twin(user_id)
        if not twin:
            state.pop(user_id, None)
            bot.reply_to(message, "❌ لا يوجد توأم")
            return True
        headers = ai_client.new_conversation_headers()
        if not headers:
            bot.reply_to(message, "❌ فشل الاتصال")
            return True
        prompt = f"""أنت الآن تمثل شخصاً بناءً على تحليل شخصيته:

{twin['personality']}

رد على الرسالة التالية بنفس أسلوبه (مختصر، 2-4 جمل):

{text}"""
        try:
            bot.send_chat_action(message.chat.id, "typing")
            full = ""
            for event in ai_client.send_message(
                headers=headers, model="gpt-4o-mini", message_text=prompt, streaming=False,
            ):
                if event["type"] == "done":
                    full = event["full"]
                    break
            if not full:
                bot.reply_to(message, "⚠️ لم يتم استلام رد")
                return True
            bot.reply_to(message, f"👥 *توأمك:*\\n\\n{full[:4000]}", parse_mode="Markdown")
        except AIError as e:
            bot.reply_to(message, f"❌ {e}")
        except Exception as e:
            log.exception("Twin chat error")
            bot.reply_to(message, f"❌ {str(e)[:100]}")
        return True
    return True


def handle_twin_start(message: Message) -> bool:
    if not message.text or " " not in message.text:
        return False
    payload = message.text.split(" ", 1)[1].strip()
    if not payload.startswith("twin_"):
        return False
    slug = payload[5:]
    twin = db.fetchone("SELECT * FROM twins WHERE share_slug = ?", (slug,))
    if not twin:
        return False
    owner = db.get_user(twin["user_id"])
    owner_name = owner["first_name"] if owner else "صاحبك"
    bot.send_message(
        message.chat.id,
        f"👥 *توأم {owner_name}*\\n\\n✍️ ابعت سؤالك، وهيرد بأسلوب {owner_name}.\\n\\n/cancel للخروج.",
        parse_mode="Markdown",
    )
    state[message.from_user.id] = {"step": "twin_chat_public", "twin_user_id": twin["user_id"]}
    return True


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_twin_menu, func=lambda c: c.data == "twin_menu")
    bot.register_callback_query_handler(cb_twin_train, func=lambda c: c.data == "twin_train")
    bot.register_callback_query_handler(cb_twin_chat, func=lambda c: c.data == "twin_chat")
    bot.register_callback_query_handler(cb_twin_share, func=lambda c: c.data == "twin_share")
    bot.register_callback_query_handler(cb_twin_delete, func=lambda c: c.data == "twin_delete")
'''


# ============================================================
# handlers/tools.py
# ============================================================
FILES["handlers/tools.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tools — أدوات متعددة."""

import io
import logging
from typing import Optional

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from models import ai_client, AIError
from keyboards import tools_menu_kb

log = logging.getLogger("handler.tools")

bot = None
db = None

state = {}
MAX_INPUT = 3000


def _ai_short(prompt: str, model: str = "gpt-4o-mini") -> Optional[str]:
    headers = ai_client.new_conversation_headers()
    if not headers:
        return None
    try:
        full = ""
        for ev in ai_client.send_message(headers=headers, model=model, message_text=prompt, streaming=False):
            if ev["type"] == "done":
                full = ev["full"]
                break
        return full or None
    except AIError as e:
        log.warning(f"_ai_short error: {e}")
        return None


def cb_tools_menu(call: CallbackQuery):
    text = (
        f"🛠️ *الأدوات*\\n\\n"
        f"🌐 *ترجمة* — ترجم أي نص\\n"
        f"📄 *تلخيص PDF* — ارفع PDF ولخصه\\n"
        f"🖼️ *OCR* — استخرج نص من صورة\\n"
        f"🔍 *بحث ويب* — ابحث في الإنترنت\\n"
        f"💻 *شرح كود* — اشرح أي كود\\n"
    )
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=tools_menu_kb())
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=tools_menu_kb())
    bot.answer_callback_query(call.id)


def cb_tool_translate(call: CallbackQuery):
    state[call.from_user.id] = {"step": "translate_input"}
    try:
        bot.edit_message_text(
            "🌐 *ترجمة*\\n\\n✍️ ابعت النص اللي عايز تترجمه.\\n\\n/cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="tools_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_tool_summarize(call: CallbackQuery):
    state[call.from_user.id] = {"step": "pdf_upload"}
    try:
        bot.edit_message_text(
            "📄 *تلخيص PDF*\\n\\n📤 ارفع ملف PDF (حتى 10MB).\\n\\n/cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="tools_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_tool_ocr(call: CallbackQuery):
    state[call.from_user.id] = {"step": "ocr_upload"}
    try:
        bot.edit_message_text(
            "🖼️ *استخراج نص (OCR)*\\n\\n📤 ارفع صورة فيها نص.\\n\\n/cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="tools_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_tool_search(call: CallbackQuery):
    state[call.from_user.id] = {"step": "search_input"}
    try:
        bot.edit_message_text(
            "🔍 *بحث ويب*\\n\\n✍️ ابعت سؤالك.\\n\\n/cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="tools_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def cb_tool_explain_code(call: CallbackQuery):
    state[call.from_user.id] = {"step": "code_input"}
    try:
        bot.edit_message_text(
            "💻 *شرح كود*\\n\\n✍️ ابعت الكود اللي عايز تشرحه.\\n\\n/cancel للإلغاء",
            call.message.chat.id, call.message.message_id, parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="tools_menu")]]),
        )
    except Exception:
        pass
    bot.answer_callback_query(call.id)


def handle_document(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    if s["step"] != "pdf_upload":
        return False
    doc = message.document
    if not doc or not doc.file_name.lower().endswith(".pdf"):
        bot.reply_to(message, "❌ ارفع PDF بس")
        return True
    if doc.file_size > 10 * 1024 * 1024:
        bot.reply_to(message, "❌ الملف كبير (10MB حد أقصى)")
        return True
    try:
        bot.send_message(message.chat.id, "📄 جاري قراءة PDF...")
        file_info = bot.get_file(doc.file_id)
        downloaded = bot.download_file(file_info.file_path)
        text = _extract_pdf_text(downloaded)
        if not text or len(text) < 50:
            bot.reply_to(message, "❌ PDF فاضي أو نصه قليل (ممكن يكون صور)")
            state.pop(user_id, None)
            return True
        text = text[:6000]
        bot.send_message(message.chat.id, "🤖 جاري التلخيص...")
        summary = _ai_short(f"لخص النص التالي بالعربية في 5-7 نقاط واضحة:\\n\\n{text}")
        state.pop(user_id, None)
        if summary:
            bot.send_message(message.chat.id, f"📄 *الملخص:*\\n\\n{summary[:4000]}", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "⚠️ فشل التلخيص")
    except Exception as e:
        log.exception("PDF processing error")
        bot.reply_to(message, f"❌ خطأ: {str(e)[:100]}")
        state.pop(user_id, None)
    return True


def _extract_pdf_text(data: bytes) -> str:
    try:
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(data))
        out = []
        for page in reader.pages[:20]:
            try:
                out.append(page.extract_text() or "")
            except Exception:
                pass
        return "\\n".join(out)
    except ImportError:
        log.warning("pypdf غير مثبت")
        return ""
    except Exception as e:
        log.warning(f"PDF extract error: {e}")
        return ""


def handle_photo(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    if s["step"] != "ocr_upload":
        return False
    try:
        bot.send_message(message.chat.id, "🖼️ جاري استخراج النص...")
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        downloaded = bot.download_file(file_info.file_path)
        text = _extract_text_from_image(downloaded)
        state.pop(user_id, None)
        if text and text.strip():
            bot.send_message(message.chat.id, f"📝 *النص المستخرج:*\\n\\n`{text[:3500]}`", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "❌ مقدرتش أستخرج نص.\\n\\n💡 جرب صورة أوضح.")
    except Exception as e:
        log.exception("OCR error")
        bot.reply_to(message, f"❌ خطأ: {str(e)[:100]}")
        state.pop(user_id, None)
    return True


def _extract_text_from_image(data: bytes) -> str:
    try:
        from PIL import Image
        import pytesseract
        img = Image.open(io.BytesIO(data))
        return pytesseract.image_to_string(img, lang="ara+eng")
    except ImportError:
        log.warning("PIL/pytesseract غير مثبت")
        return ""
    except Exception as e:
        log.warning(f"OCR error: {e}")
        return ""


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if text == "/cancel":
        state.pop(user_id, None)
        bot.reply_to(message, "❌ تم الإلغاء")
        return True
    if s["step"] == "translate_input":
        if not text:
            return True
        lang = "العربية" if not _is_arabic(text) else "الإنجليزية"
        bot.send_message(message.chat.id, "🌐 جاري الترجمة...")
        result = _ai_short(f"ترجم النص التالي إلى {lang} بدقة، واكتب الترجمة فقط:\\n\\n{text[:MAX_INPUT]}")
        state.pop(user_id, None)
        if result:
            bot.send_message(message.chat.id, f"🌐 *الترجمة:*\\n\\n{result[:4000]}", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "⚠️ فشلت الترجمة")
        return True
    if s["step"] == "search_input":
        if not text:
            return True
        bot.send_message(message.chat.id, "🔍 جاري البحث...")
        result = _ai_short(f"ابحث في معرفتك عن إجابة دقيقة ومحدثة للسؤال التالي:\\n\\n{text[:500]}")
        state.pop(user_id, None)
        if result:
            bot.send_message(message.chat.id, f"🔍 *النتيجة:*\\n\\n{result[:4000]}", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "⚠️ فشل البحث")
        return True
    if s["step"] == "code_input":
        if not text:
            return True
        bot.send_message(message.chat.id, "💻 جاري التحليل...")
        result = _ai_short(f"اشرح الكود التالي بالعربية (اللغة، الوظيفة، الأخطاء، اقتراحات):\\n\\n{text[:MAX_INPUT]}")
        state.pop(user_id, None)
        if result:
            bot.send_message(message.chat.id, f"💻 *الشرح:*\\n\\n{result[:4000]}", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "⚠️ فشل الشرح")
        return True
    return True


def _is_arabic(text: str) -> bool:
    arabic_chars = sum(1 for c in text if "\\u0600" <= c <= "\\u06FF")
    return arabic_chars > len(text) * 0.3


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_callback_query_handler(cb_tools_menu, func=lambda c: c.data == "tools_menu")
    bot.register_callback_query_handler(cb_tool_translate, func=lambda c: c.data == "tool_translate")
    bot.register_callback_query_handler(cb_tool_summarize, func=lambda c: c.data == "tool_summarize")
    bot.register_callback_query_handler(cb_tool_ocr, func=lambda c: c.data == "tool_ocr")
    bot.register_callback_query_handler(cb_tool_search, func=lambda c: c.data == "tool_search")
    bot.register_callback_query_handler(cb_tool_explain_code, func=lambda c: c.data == "tool_explain_code")
'''


# ============================================================
# handlers/admin.py
# ============================================================
FILES["handlers/admin.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Admin Panel."""

import logging
from datetime import datetime, timedelta

from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID, TZ, CHALLENGE_CATEGORIES
from utils import truncate
from keyboards import admin_menu_kb, admin_settings_kb

log = logging.getLogger("handler.admin")

bot = None
db = None

state = {}


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


def _guard(call: CallbackQuery) -> bool:
    if not is_admin(call.from_user.id):
        bot.answer_callback_query(call.id, "⛔ للمالك فقط", show_alert=True)
        return False
    return True


def _show(call: CallbackQuery, text: str, kb):
    try:
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                              parse_mode="Markdown", reply_markup=kb)
    except Exception:
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)


def cb_admin_panel(call: CallbackQuery):
    if not _guard(call):
        return
    s = db.stats()
    text = (
        f"🛡️ *لوحة الأدمن*\\n\\n"
        f"👥 المستخدمون: *{s['total_users']}*\\n"
        f"🆕 اليوم: *{s['today_users']}*\\n"
        f"🚫 المحظورون: *{s['banned']}*\\n\\n"
        f"💬 الرسائل: *{s['total_messages']}*\\n"
        f"📅 اليوم: *{s['today_messages']}*\\n"
        f"🗂️ المحادثات: *{s['total_conversations']}*\\n"
        f"📌 المحفوظات: *{s['total_prompts']}*\\n"
        f"🎨 المعرض: *{s['total_gallery']}*\\n"
        f"👥 التوائم: *{s['total_twins']}*\\n"
        f"🚪 الغرف: *{s['total_rooms']}*\\n"
    )
    _show(call, text, admin_menu_kb())
    bot.answer_callback_query(call.id)


def cb_admin_stats(call: CallbackQuery):
    if not _guard(call):
        return
    s = db.stats()
    top_models = db.top_models(5)
    text = f"📊 *إحصائيات تفصيلية*\\n\\n"
    for k, v in s.items():
        text += f"• {k}: *{v}*\\n"
    if top_models:
        text += "\\n🤖 *النماذج:*\\n"
        for m in top_models:
            text += f"• {m['model']}: {m['c']}\\n"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"))
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def cb_admin_users(call: CallbackQuery):
    if not _guard(call):
        return
    rows = db.fetchall(
        "SELECT user_id, first_name, username, xp, level, messages_count, is_banned FROM users ORDER BY last_seen DESC LIMIT 20"
    )
    if not rows:
        bot.answer_callback_query(call.id, "لا يوجد مستخدمون", show_alert=True)
        return
    text = "👥 *آخر 20 مستخدم*\\n\\n"
    for r in rows:
        status = "🚫" if r["is_banned"] else "🟢"
        name = r["first_name"] or r["username"] or f"User{r['user_id']}"
        text += f"{status} `{r['user_id']}` — {name[:15]} — L{r['level']} — 💬{r['messages_count']}\\n"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"))
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def cb_admin_banned(call: CallbackQuery):
    if not _guard(call):
        return
    rows = db.fetchall("SELECT user_id, reason, banned_at FROM bans ORDER BY banned_at DESC LIMIT 20")
    if not rows:
        bot.answer_callback_query(call.id, "لا يوجد محظورون", show_alert=True)
        return
    text = "🚫 *المحظورون*\\n\\n"
    for r in rows:
        text += f"`{r['user_id']}` — {truncate(r['reason'], 30)} — {r['banned_at'][:10]}\\n"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"))
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def cb_admin_broadcast(call: CallbackQuery):
    if not _guard(call):
        return
    state[call.from_user.id] = {"step": "broadcast"}
    text = (
        "📢 *إذاعة*\\n\\n"
        "✍️ ابعت الرسالة اللي عايز تبعتها لكل المستخدمين.\\n\\n"
        "أو /cancel للإلغاء."
    )
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("❌ إلغاء", callback_data="admin_panel"))
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def _do_broadcast(admin_id: int, text: str):
    users = db.fetchall("SELECT user_id FROM users WHERE is_banned = 0")
    ok, fail = 0, 0
    for u in users:
        try:
            bot.send_message(u["user_id"], text)
            ok += 1
        except Exception:
            fail += 1
    db.audit(admin_id, "broadcast", "", f"{ok}/{len(users)}")
    bot.send_message(admin_id, f"✅ الإذاعة خلصت\\n✔️ {ok}\\n❌ {fail}")


def cb_admin_challenges(call: CallbackQuery):
    if not _guard(call):
        return
    active = db.fetchone("SELECT * FROM challenges WHERE is_active = 1 ORDER BY id DESC LIMIT 1")
    if active:
        text = (
            f"🎯 *التحدي الحالي*\\n\\n"
            f"🏷️ {active['title']}\\n"
            f"📂 {active['category']}\\n"
            f"📅 {active['start_at'][:10]} → {active['end_at'][:10]}\\n\\n"
        )
        kb = InlineKeyboardMarkup(row_width=1)
        kb.add(
            InlineKeyboardButton("🏁 إنهاء التحدي", callback_data=f"admin_chal_end_{active['id']}"),
            InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"),
        )
    else:
        text = "🎯 *إدارة التحديات*\\n\\nمفيش تحدٍ نشط."
        kb = InlineKeyboardMarkup(row_width=1)
        kb.add(
            InlineKeyboardButton("➕ إنشاء تحدي", callback_data="admin_chal_create"),
            InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"),
        )
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def cb_admin_chal_create(call: CallbackQuery):
    if not _guard(call):
        return
    state[call.from_user.id] = {"step": "chal_create_title"}
    text = "➕ *تحدي جديد*\\n\\n✍️ ابعت *عنوان* التحدي.\\n\\n/cancel للإلغاء"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("❌ إلغاء", callback_data="admin_challenges"))
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def cb_admin_chal_end(call: CallbackQuery):
    if not _guard(call):
        return
    cid = int(call.data.replace("admin_chal_end_", ""))
    db.execute("UPDATE challenges SET is_active = 0 WHERE id = ?", (cid,))
    db.audit(call.from_user.id, "chal_end", str(cid))
    bot.answer_callback_query(call.id, "✅ انتهى")
    cb_admin_challenges(call)


def cb_admin_settings(call: CallbackQuery):
    if not _guard(call):
        return
    _show(call, "⚙️ *الإعدادات:*", admin_settings_kb())
    bot.answer_callback_query(call.id)


def _toggle_setting(key: str):
    v = db.get_setting(key, "0")
    db.set_setting(key, "0" if v == "1" else "1")


def cb_admin_toggle_maintenance(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("maintenance")
    db.audit(call.from_user.id, "toggle_maintenance")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_forcesub(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("force_sub")
    db.audit(call.from_user.id, "toggle_forcesub")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_memory(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("memory_enabled_global")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_xp(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("xp_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_streak(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("streak_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_referral(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("referral_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_gallery(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("gallery_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_challenges(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("challenges_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_rooms(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("rooms_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_toggle_twins(call: CallbackQuery):
    if not _guard(call):
        return
    _toggle_setting("twins_enabled")
    bot.answer_callback_query(call.id, "✅")
    cb_admin_settings(call)


def cb_admin_audit(call: CallbackQuery):
    if not _guard(call):
        return
    rows = db.fetchall("SELECT * FROM audit_log ORDER BY id DESC LIMIT 20")
    if not rows:
        bot.answer_callback_query(call.id, "لا يوجد سجل", show_alert=True)
        return
    text = "📝 *آخر الأحداث*\\n\\n"
    for r in rows:
        text += f"• {r['action']} — {r['target'] or '-'} — {r['timestamp'][:19]}\\n"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel"))
    _show(call, text, kb)
    bot.answer_callback_query(call.id)


def cmd_ban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split(maxsplit=2)
    if len(parts) < 2:
        bot.reply_to(message, "الاستخدام: `/ban <user_id> [سبب]`", parse_mode="Markdown")
        return
    try:
        target = int(parts[1])
        reason = parts[2] if len(parts) > 2 else "بدون سبب"
        db.ban(target, reason, message.from_user.id)
        db.audit(message.from_user.id, "ban", str(target), reason)
        bot.reply_to(message, f"✅ تم حظر `{target}`", parse_mode="Markdown")
    except ValueError:
        bot.reply_to(message, "❌ ID غير صحيح")


def cmd_unban(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split()
    if len(parts) < 2:
        bot.reply_to(message, "الاستخدام: `/unban <user_id>`", parse_mode="Markdown")
        return
    try:
        target = int(parts[1])
        db.unban(target)
        db.audit(message.from_user.id, "unban", str(target))
        bot.reply_to(message, f"✅ تم فك الحظر عن `{target}`", parse_mode="Markdown")
    except ValueError:
        bot.reply_to(message, "❌ ID غير صحيح")


def cmd_broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(message, "الاستخدام: `/broadcast <النص>`", parse_mode="Markdown")
        return
    bot.reply_to(message, "⏳ جاري الإذاعة...")
    _do_broadcast(message.from_user.id, parts[1])


def handle_text(message: Message) -> bool:
    user_id = message.from_user.id
    if not is_admin(user_id):
        return False
    if user_id not in state:
        return False
    s = state[user_id]
    text = (message.text or "").strip()
    if text == "/cancel":
        state.pop(user_id, None)
        bot.reply_to(message, "❌ تم الإلغاء")
        return True
    if s["step"] == "broadcast":
        state.pop(user_id, None)
        bot.reply_to(message, "⏳ جاري الإذاعة...")
        _do_broadcast(user_id, text)
        return True
    if s["step"] == "chal_create_title":
        if len(text) < 3 or len(text) > 80:
            bot.reply_to(message, "❌ العنوان 3-80 حرف")
            return True
        s["title"] = text
        s["step"] = "chal_create_desc"
        bot.reply_to(message, "📝 ابعت *الوصف*:", parse_mode="Markdown")
        return True
    if s["step"] == "chal_create_desc":
        if len(text) < 10:
            bot.reply_to(message, "❌ الوصف قصير جداً")
            return True
        s["description"] = text
        s["step"] = "chal_create_cat"
        kb = InlineKeyboardMarkup(row_width=2)
        for cat in CHALLENGE_CATEGORIES:
            kb.add(InlineKeyboardButton(cat, callback_data=f"chal_admin_cat_{cat}"))
        bot.reply_to(message, "🏷️ اختار التصنيف:", reply_markup=kb)
        return True
    if s["step"] == "chal_create_days":
        try:
            days = int(text)
            if days < 1 or days > 30:
                raise ValueError
        except ValueError:
            bot.reply_to(message, "❌ رقم من 1-30")
            return True
        start = datetime.now(TZ)
        end = start + timedelta(days=days)
        db.execute(
            "INSERT INTO challenges (category, title, description, start_at, end_at, is_active) VALUES (?, ?, ?, ?, ?, 1)",
            (s["category"], s["title"], s["description"], start.isoformat(), end.isoformat()),
        )
        state.pop(user_id, None)
        bot.reply_to(message, f"✅ تم إنشاء التحدي لمدة {days} يوم")
        return True
    return True


def cb_admin_chal_category(call: CallbackQuery):
    if not _guard(call):
        return
    cat = call.data.replace("chal_admin_cat_", "")
    if cat not in CHALLENGE_CATEGORIES:
        bot.answer_callback_query(call.id, "❌", show_alert=True)
        return
    s = state.get(call.from_user.id)
    if not s:
        return
    s["category"] = cat
    s["step"] = "chal_create_days"
    bot.answer_callback_query(call.id, f"✅ {cat}")
    bot.send_message(call.from_user.id, "📅 ابعت مدة التحدي (بالأيام، 1-30):")


def register(bot_instance, db_instance):
    global bot, db
    bot = bot_instance
    db = db_instance
    bot.register_message_handler(cmd_ban, commands=["ban"])
    bot.register_message_handler(cmd_unban, commands=["unban"])
    bot.register_message_handler(cmd_broadcast, commands=["broadcast"])
    bot.register_callback_query_handler(cb_admin_panel, func=lambda c: c.data == "admin_panel")
    bot.register_callback_query_handler(cb_admin_stats, func=lambda c: c.data == "admin_stats")
    bot.register_callback_query_handler(cb_admin_users, func=lambda c: c.data == "admin_users")
    bot.register_callback_query_handler(cb_admin_banned, func=lambda c: c.data == "admin_banned")
    bot.register_callback_query_handler(cb_admin_broadcast, func=lambda c: c.data == "admin_broadcast")
    bot.register_callback_query_handler(cb_admin_challenges, func=lambda c: c.data == "admin_challenges")
    bot.register_callback_query_handler(cb_admin_chal_create, func=lambda c: c.data == "admin_chal_create")
    bot.register_callback_query_handler(cb_admin_chal_end, func=lambda c: c.data.startswith("admin_chal_end_"))
    bot.register_callback_query_handler(cb_admin_chal_category, func=lambda c: c.data.startswith("chal_admin_cat_"))
    bot.register_callback_query_handler(cb_admin_settings, func=lambda c: c.data == "admin_settings")
    bot.register_callback_query_handler(cb_admin_toggle_maintenance, func=lambda c: c.data == "admin_toggle_maintenance")
    bot.register_callback_query_handler(cb_admin_toggle_forcesub, func=lambda c: c.data == "admin_toggle_forcesub")
    bot.register_callback_query_handler(cb_admin_toggle_memory, func=lambda c: c.data == "admin_toggle_memory")
    bot.register_callback_query_handler(cb_admin_toggle_xp, func=lambda c: c.data == "admin_toggle_xp")
    bot.register_callback_query_handler(cb_admin_toggle_streak, func=lambda c: c.data == "admin_toggle_streak")
    bot.register_callback_query_handler(cb_admin_toggle_referral, func=lambda c: c.data == "admin_toggle_referral")
    bot.register_callback_query_handler(cb_admin_toggle_gallery, func=lambda c: c.data == "admin_toggle_gallery")
    bot.register_callback_query_handler(cb_admin_toggle_challenges, func=lambda c: c.data == "admin_toggle_challenges")
    bot.register_callback_query_handler(cb_admin_toggle_rooms, func=lambda c: c.data == "admin_toggle_rooms")
    bot.register_callback_query_handler(cb_admin_toggle_twins, func=lambda c: c.data == "admin_toggle_twins")
    bot.register_callback_query_handler(cb_admin_audit, func=lambda c: c.data == "admin_audit")
'''


# ============================================================
# jobs/__init__.py
# ============================================================
FILES["jobs/__init__.py"] = '''from . import daily, weekly

__all__ = ["daily", "weekly"]
'''


# ============================================================
# jobs/daily.py
# ============================================================
FILES["jobs/daily.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Daily jobs — إشعارات + تذكير streak."""

import logging
import threading
import time
from datetime import datetime, timedelta

from config import TZ

log = logging.getLogger("job.daily")


def _send(bot, chat_id: int, text: str):
    try:
        bot.send_message(chat_id, text, parse_mode="Markdown")
        return True
    except Exception:
        return False


def run_once(bot, db):
    if db.get_bool("maintenance", False):
        log.info("Maintenance mode — skip daily")
        return
    now = datetime.now(TZ)
    yesterday = (now.date() - timedelta(days=1)).isoformat()
    rows = db.fetchall(
        "SELECT user_id, streak, last_streak_date FROM users WHERE streak > 0 AND last_streak_date = ? AND is_banned = 0",
        (yesterday,),
    )
    for r in rows:
        _send(bot, r["user_id"],
              f"🔥 *متكسرش السلسلة!*\\n\\nسلسلتك *{r['streak']}* يوم — ابعت رسالة النهاردة!")
    three_days_ago = (now - timedelta(days=3)).isoformat()
    rows = db.fetchall(
        "SELECT user_id, first_name FROM users WHERE last_seen < ? AND is_banned = 0 AND messages_count > 0 ORDER BY last_seen DESC LIMIT 100",
        (three_days_ago,),
    )
    for r in rows:
        name = r["first_name"] or "صديقي"
        _send(bot, r["user_id"],
              f"👋 *وحشتنا يا {name}!*\\n\\nعندك محادثات جديدة مستنياك.")
    notifs = db.fetchall("SELECT * FROM notifications WHERE is_sent = 0 LIMIT 100")
    for n in notifs:
        if _send(bot, n["user_id"], n["message"]):
            db.execute("UPDATE notifications SET is_sent = 1, sent_at = ? WHERE id = ?",
                       (datetime.now(TZ).isoformat(), n["id"]))
    log.info(f"✅ Daily run done")


def start(bot, db, interval_hours: int = 6):
    def loop():
        time.sleep(60)
        while True:
            try:
                run_once(bot, db)
            except Exception as e:
                log.exception(f"daily job error: {e}")
            time.sleep(interval_hours * 3600)
    t = threading.Thread(target=loop, daemon=True, name="daily-job")
    t.start()
    log.info(f"✅ Daily job started")
'''


# ============================================================
# jobs/weekly.py
# ============================================================
FILES["jobs/weekly.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Weekly jobs — leaderboard + auto-challenge."""

import logging
import threading
import time
from datetime import datetime, timedelta

from config import TZ

log = logging.getLogger("job.weekly")

CHALLENGE_TEMPLATES = {
    "story": {"title": "📖 أفضل قصة قصيرة", "description": "اكتب قصة قصيرة (10-15 سطر) بأي موضوع."},
    "code": {"title": "💻 أفضل كود", "description": "شارك كود مفيد مع شرح مختصر."},
    "poem": {"title": "📜 أفضل قصيدة", "description": "اكتب قصيدة (5-10 أبيات)."},
    "idea": {"title": "💡 أفضل فكرة", "description": "شارك فكرة مشروع مبتكر في 5 أسطر."},
    "riddle": {"title": "🧩 أفضل لغز", "description": "اكتب لغز ذكي مع الحل."},
}


def _close_expired_challenges(db, bot):
    now = datetime.now(TZ).isoformat()
    expired = db.fetchall("SELECT * FROM challenges WHERE is_active = 1 AND end_at < ?", (now,))
    for ch in expired:
        db.execute("UPDATE challenges SET is_active = 0 WHERE id = ?", (ch["id"],))
        winner = db.fetchone(
            "SELECT * FROM challenge_entries WHERE challenge_id = ? ORDER BY votes DESC, id ASC LIMIT 1",
            (ch["id"],),
        )
        if winner:
            db.add_xp(winner["user_id"], 500)
            try:
                bot.send_message(winner["user_id"],
                                 f"🏆 *مبروك! فزت في التحدي!*\\n\\n🎯 {ch['title']}\\n👥 أصواتك: {winner['votes']}\\n🎁 +500 XP",
                                 parse_mode="Markdown")
            except Exception:
                pass


def _create_weekly_challenge(db):
    now = datetime.now(TZ)
    active = db.fetchone("SELECT 1 FROM challenges WHERE is_active = 1 LIMIT 1")
    if active:
        return
    week_num = int(now.strftime("%W"))
    cats = list(CHALLENGE_TEMPLATES.keys())
    cat = cats[week_num % len(cats)]
    template = CHALLENGE_TEMPLATES[cat]
    end = now + timedelta(days=7)
    db.execute(
        "INSERT INTO challenges (category, title, description, start_at, end_at, is_active) VALUES (?, ?, ?, ?, ?, 1)",
        (cat, template["title"], template["description"], now.isoformat(), end.isoformat()),
    )
    log.info(f"✅ Created weekly challenge: {cat}")


def run_once(bot, db):
    if db.get_bool("maintenance", False):
        return
    try:
        _close_expired_challenges(db, bot)
        _create_weekly_challenge(db)
        log.info("✅ Weekly run done")
    except Exception as e:
        log.exception(f"weekly job error: {e}")


def start(bot, db, interval_hours: int = 24):
    def loop():
        time.sleep(120)
        while True:
            try:
                run_once(bot, db)
            except Exception as e:
                log.exception(f"weekly loop error: {e}")
            time.sleep(interval_hours * 3600)
    t = threading.Thread(target=loop, daemon=True, name="weekly-job")
    t.start()
    log.info(f"✅ Weekly job started")
'''


# ============================================================
# main.py
# ============================================================
FILES["main.py"] = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ell Hoot AI Bot v6.0 — Entrypoint."""

import sys
import logging
import time

import telebot
from telebot.types import Message, BotCommand

from config import BOT_TOKEN, ADMIN_ID, LOG_LEVEL, LOG_FILE, BOT_NAME, CHANNEL_URL, DB_PATH
from database import Database

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(str(LOG_FILE), encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger("main")

log.info("=" * 60)
log.info(f"🚀 {BOT_NAME} v6.0")
log.info(f"👤 Admin ID: {ADMIN_ID}")
log.info("=" * 60)

db = Database(DB_PATH)
bot = telebot.TeleBot(BOT_TOKEN, parse_mode="Markdown")


def text_router(message: Message):
    from handlers import twins, memory, gallery, challenges, tools, admin, user
    if admin.handle_text(message):
        return
    if tools.handle_text(message):
        return
    if gallery.handle_text(message):
        return
    if challenges.handle_text(message):
        return
    if twins.handle_text(message):
        return
    if memory.handle_text(message):
        return
    user.handle_text(message)


def photo_router(message: Message):
    from handlers import tools
    if tools.handle_photo(message):
        return
    bot.reply_to(message, "📷 للأسف مش بعرف أعالج الصور في الوضع ده.")


def document_router(message: Message):
    from handlers import tools
    if tools.handle_document(message):
        return
    bot.reply_to(message, "📎 للأسف مش بعرف أعالج الملفات في الوضع ده.")


def register_all():
    from handlers import (
        user, persona, memory, xp, referral, groups,
        gallery, challenges, dna, twins, tools, admin,
    )
    user.register(bot, db)
    persona.register(bot, db)
    memory.register(bot, db)
    xp.register(bot, db)
    referral.register(bot, db)
    groups.register(bot, db)
    gallery.register(bot, db)
    challenges.register(bot, db)
    dna.register(bot, db)
    twins.register(bot, db)
    tools.register(bot, db)
    admin.register(bot, db)
    bot.register_message_handler(text_router, content_types=["text"], func=lambda m: True)
    bot.register_message_handler(photo_router, content_types=["photo"])
    bot.register_message_handler(document_router, content_types=["document"])
    log.info("✅ All handlers registered")


def start_jobs():
    from jobs import daily, weekly
    daily.start(bot, db, interval_hours=6)
    weekly.start(bot, db, interval_hours=24)


def cmd_start_wrapper(message: Message):
    from handlers import user, twins
    if message.text and " " in message.text:
        payload = message.text.split(" ", 1)[1].strip()
        if payload.startswith("twin_"):
            twins.handle_twin_start(message)
            return
    user.cmd_start(message)


def cmd_menu(message: Message):
    from handlers import user
    row = db.get_user(message.from_user.id)
    if not row:
        bot.reply_to(message, "استخدم /start الأول")
        return
    user._show_main_menu(message.chat.id, message.from_user.id)


def cmd_id(message: Message):
    bot.reply_to(message, f"🆔 `{message.from_user.id}`", parse_mode="Markdown")


def cmd_help(message: Message):
    text = (
        f"❓ *مساعدة*\\n\\n"
        f"*/start* — القائمة الرئيسية\\n"
        f"*/menu* — عرض القائمة\\n"
        f"*/id* — عرض ID\\n"
        f"*/cancel* — إلغاء عملية\\n\\n"
        f"💬 *أو ابعت رسالتك عادي.*\\n\\n"
        f"📢 القناة: {CHANNEL_URL}"
    )
    bot.reply_to(message, text, parse_mode="Markdown", disable_web_page_preview=True)


def setup_commands():
    try:
        bot.set_my_commands([
            BotCommand("start", "بدء البوت"),
            BotCommand("menu", "القائمة"),
            BotCommand("id", "ID الخاص بي"),
            BotCommand("help", "مساعدة"),
        ])
        log.info("✅ Commands set")
    except Exception as e:
        log.warning(f"set_my_commands: {e}")


def run():
    log.info("🚀 Registering handlers...")
    register_all()
    bot.register_message_handler(cmd_start_wrapper, commands=["start"])
    bot.register_message_handler(cmd_menu, commands=["menu"])
    bot.register_message_handler(cmd_id, commands=["id"])
    bot.register_message_handler(cmd_help, commands=["help"])
    log.info("🚀 Starting jobs...")
    start_jobs()
    log.info("🚀 Setting commands...")
    setup_commands()
    log.info("✅ Bot is running. Polling...")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except KeyboardInterrupt:
            log.info("⛔ Stopped by user")
            break
        except Exception as e:
            log.error(f"Polling error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    run()
'''


# ============================================================
# requirements.txt
# ============================================================
FILES["requirements.txt"] = '''pyTelegramBotAPI==4.20.0
requests==2.32.3
pypdf==5.1.0
Pillow==11.0.0
pytesseract==0.3.13
python-dotenv==1.0.1
'''


# ============================================================
# Dockerfile
# ============================================================
FILES["Dockerfile"] = '''FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \\
    tesseract-ocr \\
    tesseract-ocr-ara \\
    tesseract-ocr-eng \\
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data /app/logs

ENV PYTHONUNBUFFERED=1
ENV DATA_DIR=/app/data
ENV LOGS_DIR=/app/logs

CMD ["python", "main.py"]
'''


# ============================================================
# railway.json
# ============================================================
FILES["railway.json"] = '''{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "numReplicas": 1,
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
'''


# ============================================================
# .env.example
# ============================================================
FILES[".env.example"] = '''# BOT
BOT_TOKEN=123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
ADMIN_ID=123456789

# IDENTITY
BOT_NAME=Ell Hoot AI
CHANNEL_USERNAME=@Ell_Hoot
CHANNEL_URL=https://t.me/Ell_Hoot
SUPPORT_URL=https://t.me/Ell_Hoot

# LIMITS
MAX_MESSAGES_PER_MIN=20
MAX_MESSAGE_LENGTH=4000
MEMORY_MAX_ITEMS=20

# TZ
TZ_OFFSET=3

# LOGGING
LOG_LEVEL=INFO
DEBUG=0
'''


# ============================================================
# Procfile
# ============================================================
FILES["Procfile"] = "worker: python main.py\n"


# ============================================================
# README.md
# ============================================================
FILES["README.md"] = r"""# 🤖 Ell Hoot AI Bot v6.0

بوت ذكاء اصطناعي متكامل على Telegram.

## الميزات
- 💬 محادثات غير محدودة
- 🎭 شخصيات + لهجات
- 🧠 ذاكرة طويلة
- 🏆 XP + Streak + Leaderboard
- 👥 إحالات + مكافآت
- 🎨 معرض إبداعات
- 🎯 تحديات أسبوعية
- 🚪 غرف AI جماعية
- 👥 توأم رقمي
- 🧬 تحليل شخصية
- 🛠️ أدوات (ترجمة/تلخيص/OCR/بحث)
- 🛡️ لوحة أدمن كاملة

## التشغيل على Railway

1. ارفع الكود على GitHub
2. على Railway: New Project -> Deploy from GitHub
3. أضف Variables (BOT_TOKEN, ADMIN_ID)
4. أضف Volume على /app/data
5. Deploy

## Docker محلياً

docker build -t ell-hoot .
docker run -d --name ell-hoot -e BOT_TOKEN=... -e ADMIN_ID=... -v $(pwd)/data:/app/data ell-hoot

## Python مباشرة

pip install -r requirements.txt
export BOT_TOKEN=YOUR_TOKEN
export ADMIN_ID=YOUR_ID
python main.py

## Admin Commands

- /ban <user_id> [سبب] — حظر
- /unban <user_id> — فك حظر
- /broadcast <text> — إذاعة

## القناة

[@Ell_Hoot](https://t.me/Ell_Hoot)
"""

    

# ============================================================
# BUILD LOOP
# ============================================================
def main():
    print("=" * 60)
    print("🚀 بناء Ell Hoot AI Bot v6.0")
    print("=" * 60)
    print(f"📦 إجمالي الملفات: {len(FILES)}")
    print()

    BASE.mkdir(parents=True, exist_ok=True)
    (BASE / "data").mkdir(exist_ok=True)
    (BASE / "logs").mkdir(exist_ok=True)

    for path, content in FILES.items():
        full = BASE / path
        full.parent.mkdir(parents=True, exist_ok=True)
        try:
            full.write_text(content, encoding="utf-8")
            print(f"✅ {path}")
        except Exception as e:
            print(f"❌ {path}: {e}")

    print()
    print("=" * 60)
    print(f"🎉 تم بناء المشروع في: {BASE.resolve()}")
    print("=" * 60)
    print()
    print("📋 الخطوات التالية:")
    print(f"   cd {BASE}")
    print("   pip install -r requirements.txt")
    print("   export BOT_TOKEN=...")
    print("   export ADMIN_ID=...")
    print("   python main.py")
    print()
    print("🚀 للنشر على Railway:")
    print("   git init && git add . && git commit -m 'init'")
    print("   git remote add origin <your-repo>")
    print("   git push -u origin main")


if __name__ == "__main__":
    main()    
