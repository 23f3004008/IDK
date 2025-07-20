import json
import sys
from pathlib import Path

def compare_json(a, b, path=""):
    differences = []

    if type(a) != type(b):
        differences.append(path)
        return differences

    if not isinstance(a, dict) and not isinstance(a, list):
        if a != b:
            differences.append(path)
        return differences

    if isinstance(a, dict):
        all_keys = set(a.keys()) | set(b.keys())
        for key in all_keys:
            new_path = f"{path}.{key}" if path else key
            differences.extend(compare_json(a.get(key), b.get(key), new_path))
        return differences

    if isinstance(a, list):
        max_len = max(len(a), len(b))
        for i in range(max_len):
            new_path = f"{path}[{i}]"
            item_a = a[i] if i < len(a) else None
            item_b = b[i] if i < len(b) else None
            differences.extend(compare_json(item_a, item_b, new_path))
        return differences

    return differences

if __name__ == "__main__":
    a = json.loads(Path("a.json").read_text())
    b = json.loads(Path("b.json").read_text())

    diff_paths = compare_json(a, b)
    for p in diff_paths:
        print(p)
