from datetime import datetime
from pathlib import Path

from app.config import settings
from app.schemas.review import Report


def export_report_markdown(report: Report, title: str = "business-plan") -> Path:
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe = "".join(c if c.isalnum() or c in "-_" else "_" for c in title)[:60]
    path = settings.output_dir / f"{safe}_{stamp}.md"
    path.write_text(report.markdown, encoding="utf-8")
    return path
