"""
Build script for Tenqiva website.
Reads .env file, replaces {{PLACEHOLDERS}} in src/ templates,
and outputs final HTML to docs/ for GitHub Pages.

Usage: python build.py
"""

import os
import shutil

SRC_DIR = "src"
OUT_DIR = "docs"
ENV_FILE = ".env"


def load_env(path):
    """Read key=value pairs from .env file."""
    config = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config


def build():
    if not os.path.exists(ENV_FILE):
        print(f"ERROR: {ENV_FILE} not found.")
        print(f"Copy .env.example to .env and fill in your details:")
        print(f"  cp .env.example .env")
        return

    config = load_env(ENV_FILE)
    print(f"Loaded {len(config)} config values from {ENV_FILE}")

    # Clean and create output directory
    if os.path.exists(OUT_DIR):
        # Preserve CNAME if it exists
        cname_path = os.path.join(OUT_DIR, "CNAME")
        cname_content = None
        if os.path.exists(cname_path):
            with open(cname_path, "r") as f:
                cname_content = f.read()
        shutil.rmtree(OUT_DIR)
    else:
        cname_content = None

    os.makedirs(OUT_DIR, exist_ok=True)

    # Write CNAME
    with open(os.path.join(OUT_DIR, "CNAME"), "w") as f:
        f.write(cname_content if cname_content else "tenqiva.com\n")

    # Process each HTML file
    for filename in os.listdir(SRC_DIR):
        if not filename.endswith(".html"):
            continue

        src_path = os.path.join(SRC_DIR, filename)
        out_path = os.path.join(OUT_DIR, filename)

        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()

        for key, value in config.items():
            content = content.replace("{{" + key + "}}", value)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"  Built: {out_path}")

    print(f"\nDone! Site ready in {OUT_DIR}/")
    print("Commit and push to deploy on GitHub Pages.")


if __name__ == "__main__":
    build()
