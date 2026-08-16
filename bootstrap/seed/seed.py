#!/usr/bin/env python3
"""Seed the family tracker from a local template packet.

The packet is a directory of NN-slug.md files in the format documented by
TEMPLATE.md beside this script. It is local input, never committed: issue
content lives on the tracker (persistence doctrine).

Behavior, by doctrine (Method, Identity):
- verifies the acting login before any mutation and stops on mismatch;
- never blind-creates: existing titles are discovered first and reused;
- every write is read back; a created body must byte-match its template;
- wires the sub-issue hierarchy idempotently;
- mutates nothing else, and never edits an existing issue.

Usage: python3 seed.py --templates DIR [--repo OWNER/NAME] [--expect-login LOGIN] [--dry-run]
"""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def gh(args, inp=None):
    res = subprocess.run(["gh"] + args, capture_output=True, text=True, input=inp)
    if res.returncode != 0:
        raise RuntimeError(f"gh {' '.join(args)} failed: {res.stderr.strip()}")
    return res.stdout


def gh_json(args, payload=None):
    inp = json.dumps(payload) if payload is not None else None
    if payload is not None:
        args = args + ["--input", "-"]
    out = gh(args, inp=inp)
    return json.loads(out) if out.strip() else None


def parse_template(path):
    text = path.read_text(encoding="utf-8")
    header, _, body = text.partition("\n---\n")
    meta = {}
    for line in header.splitlines():
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip()
    labels = [] if meta.get("labels", "-") in ("-", "") else [
        s.strip() for s in meta["labels"].split(",")]
    parent = None if meta.get("parent", "-") in ("-", "") else meta["parent"]
    return {
        "title": meta["title"],
        "parent": parent,
        "labels": labels,
        "milestone": meta.get("milestone") or None,
        "body": body,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--templates", required=True,
                    help="local packet directory of NN-slug.md files (see TEMPLATE.md)")
    ap.add_argument("--repo", default="tclyu/astralfab")
    ap.add_argument("--expect-login", default="tclyu-automation")
    ap.add_argument("--dry-run", action="store_true")
    opts = ap.parse_args()

    login = gh(["api", "user", "--jq", ".login"]).strip()
    if login != opts.expect_login:
        sys.exit(f"STOP: acting login is {login!r}, expected {opts.expect_login!r}")

    paths = sorted(Path(opts.templates).glob("*.md"))
    if not paths:
        sys.exit(f"STOP: no templates found in {opts.templates!r}")
    templates = [parse_template(p) for p in paths]

    existing = {}
    for issue in gh_json(["api", f"repos/{opts.repo}/issues?state=all&per_page=100",
                          "--paginate"]) or []:
        if "pull_request" not in issue:
            existing[issue["title"]] = issue

    milestones = {m["title"]: m["number"]
                  for m in gh_json(["api", f"repos/{opts.repo}/milestones?state=all"]) or []}

    failures = []
    rows = []
    for t in templates:
        if t["title"] in existing:
            issue = existing[t["title"]]
            status = "existing"
            if issue["body"] != t["body"]:
                status = "existing-BODY-DIFFERS"
                failures.append(f"{t['title']}: live body differs from template; not touched")
        elif opts.dry_run:
            issue = {"number": 0, "id": 0, "body": t["body"]}
            status = "would-create"
        else:
            payload = {"title": t["title"], "body": t["body"]}
            if t["labels"]:
                payload["labels"] = t["labels"]
            if t["milestone"] and t["milestone"] in milestones:
                payload["milestone"] = milestones[t["milestone"]]
            issue = gh_json(["api", "-X", "POST", f"repos/{opts.repo}/issues"], payload)
            back = gh_json(["api", f"repos/{opts.repo}/issues/{issue['number']}"])
            status = "created"
            if back["body"] != t["body"]:
                status = "created-READBACK-MISMATCH"
                failures.append(f"{t['title']}: read-back body does not match template")
            issue = back
        existing[t["title"]] = issue
        rows.append((t["title"], issue["number"], status))

    edges = []
    for t in templates:
        if not t["parent"] or opts.dry_run:
            continue
        parent = existing[t["parent"]]
        child = existing[t["title"]]
        subs = gh_json(["api", f"repos/{opts.repo}/issues/{parent['number']}/sub_issues"]) or []
        if any(s["id"] == child["id"] for s in subs):
            edges.append((t["parent"], t["title"], "present"))
        else:
            gh_json(["api", "-X", "POST",
                     f"repos/{opts.repo}/issues/{parent['number']}/sub_issues"],
                    {"sub_issue_id": child["id"]})
            subs = gh_json(["api", f"repos/{opts.repo}/issues/{parent['number']}/sub_issues"]) or []
            ok = any(s["id"] == child["id"] for s in subs)
            edges.append((t["parent"], t["title"], "added" if ok else "ADD-FAILED"))
            if not ok:
                failures.append(f"sub-issue edge {t['parent']} -> {t['title']} not present after add")

    print(f"actor: {login}  repo: {opts.repo}  dry-run: {opts.dry_run}")
    print("\nissue                     number  status")
    for title, number, status in rows:
        print(f"{title:<25} #{number:<6} {status}")
        body = existing[title]["body"].encode("utf-8")
        digest = hashlib.sha256(body).hexdigest()
        print(f"{'':<25} sha256 {digest}  bytes {len(body)}")
    print("\nhierarchy edges:")
    for parent, child, status in edges:
        print(f"  {parent} -> {child}: {status}")

    if failures:
        print("\nFAILURES:", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        sys.exit(1)
    print("\nall verified")


if __name__ == "__main__":
    main()
