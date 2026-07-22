# Использование

```python
from src.parser import parse_line
from src.report import summarize

records = [parse_line(line) for line in open("app.log")]
print(summarize(records))
```
