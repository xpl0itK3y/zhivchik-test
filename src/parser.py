"""Разбор строк журнала: одна запись на строку."""


def parse_line(line: str) -> dict[str, str]:
    level, separator, message = line.partition(": ")
    if not separator:
        # Строка без разделителя — это само сообщение без уровня.
        return {"level": "info", "message": line.strip()}
    return {"level": level.strip().lower(), "message": message.strip()}
