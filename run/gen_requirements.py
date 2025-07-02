import os
import re
import subprocess


def list_empty_directories(path):
    """List all empty directories in the given path."""
    empty_dirs = []
    for root, dirs, files in os.walk(path):
        if not dirs and not files:
            empty_dirs.append(root)
    return empty_dirs


def main():
    with open("run/index.html") as f:
        html = f.read()
    with open("downloads/web/simple/index.html") as f:
        html += f.read()
    old = re.findall(r'<a href="(.+?)/">', html)

    result = subprocess.run(
        "uv pip install --dry-run -r run/requirements.in.txt".split(),
        capture_output=True,
        text=True,
    )
    new = re.findall(r"\+ (.+?)==", result.stderr)
    packages = sorted(set(new) - set(old))
    for package in packages:
        print(package)


if __name__ == "__main__":
    main()
