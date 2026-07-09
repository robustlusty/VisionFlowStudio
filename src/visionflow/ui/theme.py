from pathlib import Path


def load_stylesheet():

    css = Path(__file__).parent / "styles.qss"

    if css.exists():

        return css.read_text(encoding="utf-8")

    return ""