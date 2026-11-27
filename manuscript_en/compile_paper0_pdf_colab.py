#!/usr/bin/env python3
"""
VeriShield Paper 00 — Google Colab LaTeX-to-PDF Compiler & Overleaf Packager
Local-NVMe-First (/content/work/) compliant per AGENTS.md.

Usage in Google Colab:
  1. Upload `main.tex`, `references.bib`, and the 6 PNG figures from `figures/`
     (or mount Drive and set SOURCE_DIR below).
  2. Run: !python3 compile_paper0_pdf_colab.py
  3. Downloads `paper0-umbrella-survey.pdf` and `paper0-overleaf-bundle.zip`.
"""

import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

WORK_DIR = Path("/content/work/paper0_build")
FIG_NAMES = [
    "fig1-prisma-screening.png",
    "fig2-four-axis-taxonomy.png",
    "fig3-math-to-code-verification-paradox.png",
    "fig4-pqc-verification-pipelines.png",
    "fig5-agent-security-utility-frontier.png",
    "fig6-human-proof-auditing.png",
]


def run_cmd(cmd, cwd=None, check=True):
    print(f"$ {' '.join(cmd)}")
    res = subprocess.run(
        cmd, cwd=cwd, text=True, encoding="utf-8", errors="replace", capture_output=True
    )
    if res.returncode != 0 and check:
        print(res.stdout[-3000:])
        print(res.stderr[-3000:], file=sys.stderr)
        raise RuntimeError(f"Command failed ({res.returncode}): {' '.join(cmd)}")
    return res


def ensure_texlive():
    if shutil.which("pdflatex") and shutil.which("bibtex"):
        print("TeX Live already installed.")
        return
    print("Installing minimal TeX Live packages on Colab local NVMe...")
    run_cmd(["apt-get", "update", "-qq"])
    run_cmd([
        "apt-get", "install", "-y", "-qq", "--no-install-recommends",
        "texlive-latex-base",
        "texlive-latex-recommended",
        "texlive-latex-extra",
        "texlive-fonts-recommended",
        "texlive-bibtex-extra",
        "texlive-science",
    ])


def locate_sources(script_dir: Path):
    """Find main.tex, references.bib, and figures/ locally or in /content."""
    candidates = [
        script_dir,
        Path("/content"),
        Path("/content/manuscript_en"),
    ]
    tex_src = bib_src = None
    for base in candidates:
        if (base / "main.tex").exists() and (base / "references.bib").exists():
            tex_src = base / "main.tex"
            bib_src = base / "references.bib"
            break
    if not tex_src:
        raise FileNotFoundError(
            "Could not find main.tex and references.bib. Upload them to /content/ or run from manuscript_en/."
        )

    fig_candidates = [
        tex_src.parent / "figures",
        tex_src.parent.parent / "figures",
        Path("/content/figures"),
        Path("/content"),
    ]
    fig_map = {}
    for name in FIG_NAMES:
        for fc in fig_candidates:
            p = fc / name
            if p.exists():
                fig_map[name] = p
                break
        if name not in fig_map:
            raise FileNotFoundError(f"Missing required 300-DPI figure: {name}")
    return tex_src, bib_src, fig_map


def stage_workspace(tex_src: Path, bib_src: Path, fig_map: dict):
    if WORK_DIR.exists():
        shutil.rmtree(WORK_DIR)
    (WORK_DIR / "figures").mkdir(parents=True, exist_ok=True)
    shutil.copy2(tex_src, WORK_DIR / "main.tex")
    shutil.copy2(bib_src, WORK_DIR / "references.bib")
    for name, src in fig_map.items():
        shutil.copy2(src, WORK_DIR / "figures" / name)
    print(f"Staged build workspace in {WORK_DIR} (Local NVMe).")


def build_overleaf_zip(out_zip: Path):
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(WORK_DIR / "main.tex", arcname="main.tex")
        zf.write(WORK_DIR / "references.bib", arcname="references.bib")
        for name in FIG_NAMES:
            zf.write(WORK_DIR / "figures" / name, arcname=f"figures/{name}")
    print(f"Created Overleaf-ready bundle: {out_zip} ({out_zip.stat().st_size / 1024:.1f} KB)")


def compile_pdf():
    pdflatex = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"]
    run_cmd(pdflatex, cwd=WORK_DIR)
    run_cmd(["bibtex", "main"], cwd=WORK_DIR)
    run_cmd(pdflatex, cwd=WORK_DIR)
    run_cmd(pdflatex, cwd=WORK_DIR)

    # Audit log for undefined citations/references and verify 56 bibitems
    log_text = (WORK_DIR / "main.log").read_text(encoding="utf-8", errors="ignore")
    undef_cites = re.findall(r"Citation `([^']+)' on page \d+ undefined", log_text)
    undef_refs = re.findall(r"Reference `([^']+)' on page \d+ undefined", log_text)
    bbl_text = (WORK_DIR / "main.bbl").read_text(encoding="utf-8", errors="ignore")
    bibitem_count = len(re.findall(r"\\bibitem\[", bbl_text))

    print(f"Compiled PDF: {WORK_DIR / 'main.pdf'}")
    print(f"Verified BibTeX entries rendered: {bibitem_count}/56")
    if undef_cites or undef_refs or bibitem_count != 56:
        raise RuntimeError(
            f"QA check failed: undef_cites={undef_cites}, undef_refs={undef_refs}, bibitems={bibitem_count}"
        )

    out_pdf = WORK_DIR / "paper0-umbrella-survey.pdf"
    shutil.copy2(WORK_DIR / "main.pdf", out_pdf)
    return out_pdf


def main():
    ensure_texlive()
    tex_src, bib_src, fig_map = locate_sources(Path(__file__).resolve().parent)
    stage_workspace(tex_src, bib_src, fig_map)
    out_zip = WORK_DIR / "paper0-overleaf-bundle.zip"
    build_overleaf_zip(out_zip)
    out_pdf = compile_pdf()
    print(f"\nSUCCESS!\n- PDF: {out_pdf}\n- Overleaf ZIP: {out_zip}")
    try:
        from google.colab import files  # type: ignore
        files.download(str(out_pdf))
    except ImportError:
        pass


if __name__ == "__main__":
    main()
