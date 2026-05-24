#!/usr/bin/env python3
"""Stage Gate G_D validation: P3, P4, P4', P5, P6, P7, P9, P10."""
import os
import re
import sys
from pathlib import Path

ROOT = Path("/Users/jahguo/Workspace/meritoken")
DOCS = ROOT / "docs"
LANGS = ["de", "es", "fr", "ru"]
EN = "en"
ZH = "zh-CN"

EXPECTED_FILES = {
    "README.md", "glossary.md", "00-readers-guide.md",
    "01-meritoken-overview.md", "02-meritoken-technical.md",
    "03-meritoken-social.md", "04-meritoken-usage.md",
    "05-meritoken-credential.md", "06-meritoken-deep-cases.md",
    "07-related-projects.md",
}

RESERVED_TERMS = ["ifay", "agent", "phase", "credential", "GMC", "Fay"]

ILLUSTRATION_DIR = DOCS / ZH / "blueprint" / "illustration"
ILLUSTRATION_FILES = set(p.name for p in ILLUSTRATION_DIR.iterdir())

report_lines = []
errors = []

def log(msg):
    report_lines.append(msg)
    print(msg)

def err(lang, prop, msg):
    e = f"FAIL [{lang}] {prop}: {msg}"
    errors.append(e)
    report_lines.append(e)
    print(e)

def count_substr(text, substr):
    if not substr:
        return 0
    count = 0
    start = 0
    while True:
        i = text.find(substr, start)
        if i == -1:
            return count
        count += 1
        start = i + 1

def count_term_ci(text, term):
    pattern = r'\b' + re.escape(term) + r'\b'
    return len(re.findall(pattern, text, re.IGNORECASE))

def get_image_refs(text):
    refs = []
    refs.extend(re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text))
    refs.extend(re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text))
    return refs

def get_heading_sequence(text):
    seq = []
    in_code = False
    for line in text.splitlines():
        s = line.lstrip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r'^(#{1,6})\s+', line)
        if m:
            seq.append(len(m.group(1)))
    return seq

log("="*70)
log("Stage Gate G_D Validation Report")
log("="*70)

for lang in LANGS:
    log(f"\n--- Language: {lang} ---")
    bp_dir = DOCS / lang / "blueprint"
    if not bp_dir.is_dir():
        err(lang, "P5", f"blueprint dir missing at {bp_dir}")
        continue

    # P5
    actual = set(p.name for p in bp_dir.iterdir() if p.is_file() and p.suffix == ".md")
    if actual != EXPECTED_FILES:
        missing = EXPECTED_FILES - actual
        extra = actual - EXPECTED_FILES
        err(lang, "P5", f"file set mismatch. missing={missing}, extra={extra}")
    else:
        log(f"P5 PASS: 10 files present, set matches zh-CN")

    # P7
    illust = bp_dir / "illustration"
    if illust.exists() and illust.is_dir():
        err(lang, "P7", f"illustration/ subdir exists at {illust}")
    else:
        log(f"P7 PASS: no illustration/ subdir")

    # P9
    md_files = [p.name for p in bp_dir.iterdir() if p.is_file() and p.suffix == ".md"]
    M = sum(1 for f in md_files if re.match(r'^0[1-6]-meritoken-', f))
    O_files = sum(1 for f in md_files if re.match(r'^00-readers-guide', f) or re.match(r'^07-related-projects', f))
    cnt07 = sum(1 for f in md_files if re.match(r'^07-related-', f))
    p9_ok = (M == 6) and (O_files == 2) and (M >= O_files) and (M >= 3) and (cnt07 == 1)
    if not p9_ok:
        err(lang, "P9", f"M={M}, O={O_files}, cnt07={cnt07}")
    else:
        log(f"P9 PASS: M=6, O=2, cnt07=1")

    # Per-file checks
    for fname in sorted(EXPECTED_FILES):
        fpath = bp_dir / fname
        if not fpath.exists():
            continue
        text = fpath.read_text(encoding="utf-8")
        en_path = DOCS / EN / "blueprint" / fname
        en_text = en_path.read_text(encoding="utf-8") if en_path.exists() else ""

        # P3
        refs = get_image_refs(text)
        for ref in refs:
            if ref.startswith("http://") or ref.startswith("https://") or ref.startswith("#"):
                continue
            ref_clean = ref.split("#")[0].split("?")[0]
            if not ref_clean.startswith("../../zh-CN/blueprint/illustration/"):
                err(lang, "P3", f"{fname}: image ref does not start with required prefix: {ref}")
                continue
            filename = ref_clean[len("../../zh-CN/blueprint/illustration/"):]
            if filename not in ILLUSTRATION_FILES:
                err(lang, "P3", f"{fname}: image file not found: {filename}")

        # P4
        if en_text:
            for term in RESERVED_TERMS:
                lc = count_term_ci(text, term)
                ec = count_term_ci(en_text, term)
                if lc < ec:
                    err(lang, "P4", f"{fname}: term '{term}' count {lc} < en {ec}")

        # P4'
        if en_text:
            mc_l = count_substr(text, "MeriToken")
            mc_e = count_substr(en_text, "MeriToken")
            if fname != "glossary.md":
                if mc_l < mc_e:
                    err(lang, "P4'", f"{fname}: MeriToken count {mc_l} < en {mc_e}")
        if fname != "glossary.md":
            zh_count = count_substr(text, "美誉值") + count_substr(text, "美譽值")
            if zh_count != 0:
                err(lang, "P4'", f"{fname}: zh local term occurs {zh_count} times in non-glossary file")

        # P6
        if en_text:
            seq_l = get_heading_sequence(text)
            seq_e = get_heading_sequence(en_text)
            if seq_l != seq_e:
                err(lang, "P6", f"{fname}: heading sequence mismatch. en_len={len(seq_e)} lang_len={len(seq_l)}")

    # P10
    glossary_path = bp_dir / "glossary.md"
    if glossary_path.exists():
        gtext = glossary_path.read_text(encoding="utf-8")
        required_urls = [
            "https://ifay.ai/docs/ifay",
            "https://ifay.ai/docs/agent",
            "https://ifay.ai/docs/gmc",
            "https://ifay.ai/docs/fay",
        ]
        for url in required_urls:
            if gtext.count(url) < 1:
                err(lang, "P10", f"glossary.md missing URL: {url}")
    related_path = bp_dir / "07-related-projects.md"
    if related_path.exists():
        rtext = related_path.read_text(encoding="utf-8")
        ifay_urls = re.findall(r'https://ifay\.ai/[^\s)\]"\']*', rtext)
        if len(ifay_urls) < 4:
            err(lang, "P10", f"07-related-projects.md has only {len(ifay_urls)} ifay.ai URLs (need >=4)")
        else:
            log(f"P10 partial [{lang}]: 07-related-projects.md has {len(ifay_urls)} ifay.ai URLs")

log("\n" + "="*70)
if errors:
    log(f"RESULT: {len(errors)} failure(s)")
    sys.exit(1)
else:
    log("RESULT: ALL PROPERTIES PASS for de, es, fr, ru")
    sys.exit(0)
