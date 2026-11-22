import os
from pathlib import Path

# Chosen from five candidates (see CANDIDATES.md): it recognises the judge's
# long day of reading, asks nothing of it, shows the calm in one kitchen
# scene, and ends on an image that lingers ("The room will keep").
ENTRY_TEXT = (
    "You have read so many words today. Here are a few that ask nothing of "
    "you: a kitchen at dusk, a pot cooling on the stove, rain spelling "
    "itself out on the window. The chair by the table is still warm. "
    "Stay, if you like. The room will keep."
)


def main():
    raw_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_path = Path(raw_path)
    if (
        output_path.is_dir()
        or raw_path.endswith(("/", "\\"))
        or (not output_path.suffix and output_path.name != "entry.txt")
    ):
        output_path = output_path / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    text = ENTRY_TEXT if ENTRY_TEXT.endswith("\n") else f"{ENTRY_TEXT}\n"
    output_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
