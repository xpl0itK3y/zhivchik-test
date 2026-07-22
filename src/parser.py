"""Разбор строк журнала: одна запись на строку."""


def parse_line(line: str) -> dict[str, str]:
    level, _, message = line.partition(": ")
    return {"level": level.strip().lower(), "message": message.strip()}
