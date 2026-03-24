#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

**Ctrl + S** save karo.

---

Ab `runtime.txt` bhi banao — same tarah root mein right click → New File → `runtime.txt` → yeh likho:
```
python-3.11.0