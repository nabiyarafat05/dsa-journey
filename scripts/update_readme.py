from pathlib import Path
import json
from datetime import datetime

root = Path(__file__).resolve().parent.parent

# Load stats
with open(root / "data" / "stats.json", "r") as f:
    stats = json.load(f)

total = stats["total"]
topics = stats["topics"]

goal = 500
filled = int((total / goal) * 20)
filled = min(filled, 20)

progress = "█" * filled + "░" * (20 - filled)

dashboard = f"""## 📊 Live DSA Dashboard

📈 **Problems Solved:** {total}/{goal}

Progress

{progress}

### 📚 Topics
"""

if topics:
    for topic, count in sorted(topics.items()):
        dashboard += f"- {topic}: {count}\n"
else:
    dashboard += "- No topics yet\n"

dashboard += f"""

🕒 Last Updated: {datetime.now().strftime('%d %b %Y %H:%M')}
"""

readme = root / "README.md"
content = readme.read_text(encoding="utf-8")

start = "<!-- DSA_DASHBOARD_START -->"
end = "<!-- DSA_DASHBOARD_END -->"

before = content.split(start)[0]
after = content.split(end)[1]

new_content = before + start + "\n\n" + dashboard + "\n\n" + end + after

readme.write_text(new_content, encoding="utf-8")

print("README updated!")
