#!/usr/bin/env python3
"""Strip secrets from text before it is written to an Obsidian vault.

Usage:
    from redact import redact
    safe = redact(raw_text, emails=False)

Catches common secret shapes (API keys, tokens, bearer headers, .env values,
private keys). Not a security boundary on its own — it is a last-line filter
so agent output does not accidentally persist credentials to disk.
"""
import re

_PATTERNS = [
    (re.compile(r'sk-[A-Za-z0-9\-_]{16,}'), '[REDACTED_API_KEY]'),
    (re.compile(r'(?i)bearer\s+[A-Za-z0-9\-_\.=]{16,}'), 'Bearer [REDACTED_TOKEN]'),
    (re.compile(r'(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*["\']?[A-Za-z0-9\-_\.]{8,}["\']?'),
     r'\1=[REDACTED]'),
    (re.compile(r'AKIA[0-9A-Z]{16}'), '[REDACTED_AWS_KEY]'),
    (re.compile(r'ghp_[A-Za-z0-9]{20,}'), '[REDACTED_GH_TOKEN]'),
    (re.compile(r'-----BEGIN [A-Z ]*PRIVATE KEY-----.*?-----END [A-Z ]*PRIVATE KEY-----',
                re.DOTALL), '[REDACTED_PRIVATE_KEY]'),
]
_EMAIL = re.compile(r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}')


def redact(text: str, emails: bool = False) -> str:
    for pat, repl in _PATTERNS:
        text = pat.sub(repl, text)
    if emails:
        text = _EMAIL.sub('[REDACTED_EMAIL]', text)
    return text


if __name__ == '__main__':
    import sys
    data = sys.stdin.read()
    sys.stdout.write(redact(data, emails='--emails' in sys.argv))
