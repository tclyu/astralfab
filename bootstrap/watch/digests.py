#!/usr/bin/env python3
"""Read-only body-digest watch.

Prints one row per tracker issue: number, title, state, SHA-256 over the exact
UTF-8 bytes of the body, byte count, and the tracker's updated_at. An acceptance
comment quotes a digest from this table; a later run whose digest differs for an
accepted body means the body was edited after acceptance and must be re-accepted
(Authorization doctrine). This tool detects; it never reverts.

Usage: python3 digests.py [--repo OWNER/NAME]
Compare runs with your diff tool of choice; output is stable and sorted.
"""

import argparse
import hashlib
import json
import subprocess


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="tclyu/astralfab")
    opts = ap.parse_args()

    out = subprocess.run(
        ["gh", "api", f"repos/{opts.repo}/issues?state=all&per_page=100", "--paginate"],
        capture_output=True, text=True, check=True).stdout
    issues = [i for i in json.loads(out) if "pull_request" not in i]

    print("| # | title | state | body-sha256 | bytes | updated_at |")
    print("| --- | --- | --- | --- | --- | --- |")
    for i in sorted(issues, key=lambda x: x["number"]):
        body = (i["body"] or "").encode("utf-8")
        digest = hashlib.sha256(body).hexdigest()
        print(f"| {i['number']} | {i['title']} | {i['state']} "
              f"| `{digest}` | {len(body)} | {i['updated_at']} |")


if __name__ == "__main__":
    main()
