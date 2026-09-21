import sys
from pathlib import Path

profile = Path("student_profile.md")
hello = Path("hello.py")

errors = []

if not profile.exists():
    errors.append("Missing student_profile.md")
else:
    text = profile.read_text(encoding="utf-8", errors="ignore")
    required = ["Name", "Course", "Date"]
    for item in required:
        if item.lower() not in text.lower():
            errors.append(f"student_profile.md missing: {item}")

if not hello.exists():
    errors.append("Missing hello.py")
else:
    text = hello.read_text(encoding="utf-8", errors="ignore")
    if "Hello, GitHub!" not in text:
        errors.append("hello.py missing Hello, GitHub! print statement")

if errors:
    print("Assignment incomplete.")
    for e in errors:
        print("- " + e)
    sys.exit(1)
else:
    print("Assignment complete.")
    sys.exit(0)