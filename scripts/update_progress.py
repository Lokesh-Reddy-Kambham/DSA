import re
from pathlib import Path


def count_python_files(topic_dir: Path) -> int:
    return sum(1 for file in topic_dir.rglob("*.py") if file.is_file())


def parse_topic_order(readme_text: str) -> list[str]:
    planned_section = re.search(
        r"## Planned Topics[^\r\n]*\r?\n(.*?)(?:\r?\n## |\Z)",
        readme_text,
        re.DOTALL,
    )
    if not planned_section:
        return []

    topics: list[str] = []
    for line in planned_section.group(1).splitlines():
        line = line.strip()
        if line.startswith("- "):
            topics.append(line[2:].strip())
    return topics


def build_progress_block(repo_root: Path, topic_order: list[str]) -> str:
    available_dirs = {
        path.name: path
        for path in repo_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    }

    counts: dict[str, int] = {}
    excluded_dirs = {"scripts", "__pycache__"}

    for topic in topic_order:
        topic_path = available_dirs.get(topic)
        if topic_path:
            count = count_python_files(topic_path)
            if count > 0:
                counts[topic] = count

    # Include folders that already have problems but are not yet listed
    # in the planned section (e.g., newly added topic directories).
    for folder_name, folder_path in sorted(available_dirs.items()):
        if folder_name in excluded_dirs or folder_name in counts:
            continue
        count = count_python_files(folder_path)
        if count > 0:
            counts[folder_name] = count

    total = sum(counts.values())

    lines = [f"- Total problems solved: {total}"]
    lines.extend(f"- {topic}: {count}" for topic, count in counts.items())
    lines.append("")
    lines.append("I will keep this section updated as I add more problems.")
    lines.append("")
    return "\n".join(lines)


def update_readme(repo_root: Path) -> None:
    readme_path = repo_root / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")

    topic_order = parse_topic_order(readme_text)
    new_progress = build_progress_block(repo_root, topic_order)

    updated = re.sub(
        r"(## Progress Tracker[^\r\n]*\r?\n)([\s\S]*?)(\r?\n## )",
        rf"\1{new_progress}\3",
        readme_text,
    )

    if updated == readme_text:
        raise RuntimeError("Could not locate '## Progress Tracker' section in README.md")

    readme_path.write_text(updated, encoding="utf-8")
    print("README.md progress tracker updated.")


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    update_readme(root)
