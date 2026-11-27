"""Generate 6 English publication-grade (300 DPI, 2200+ px) PNG & SVG figures for Paper 00.

Run on Google Colab (single cell) or local Python 3.10+ with matplotlib:
    python generate_paper0_figures.py

If executed in Google Colab, this script automatically packages the generated
figures into `/content/work/paper0_figures.zip` for download into
`papers/paper-00-umbrella-survey/figures/`.
"""
from pathlib import Path
import zipfile
import matplotlib.pyplot as plt
import matplotlib.patches as patches

SCRIPT_DIR = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
OUT = SCRIPT_DIR / "figures" if (SCRIPT_DIR / "paper-00-umbrella-survey.md").exists() or "__file__" in globals() else Path("/content/work/figures")
OUT.mkdir(parents=True, exist_ok=True)

DPI = 300  # 300 DPI publication-grade resolution (3600+ px wide at 12+ in figsize)
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#cbd5e1",
    "axes.linewidth": 0.9,
    "savefig.facecolor": "white",
})


def save_both(fig: plt.Figure, stem: str) -> None:
    """Save figure as high-resolution PNG and vector SVG."""
    fig.savefig(OUT / f"{stem}.png", dpi=DPI, bbox_inches="tight", pad_inches=0.18)
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight", pad_inches=0.18)
    plt.close(fig)


def fig1_prisma() -> None:
    """Figure 1: PRISMA-2020 Systematic Corpus (N=56) & Provenance Audit Flow."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 6.2), gridspec_kw={"width_ratios": [1.32, 1.0]})
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "Figure 1: PRISMA-2020 Verified Corpus (N = 56) & Cross-PDF Audit Flow",
        fontsize=13, fontweight="bold", y=0.98, color="#0f172a",
    )
    fig.text(
        0.5, 0.92,
        "39 Full-Text PDF Audited (Dual-Notebook Verified) + 6 NIST/OWASP Standards + 11 Peer-Reviewed Anchors | Cutoff: Nov 26, 2026",
        ha="center", fontsize=8.8, color="#475569",
    )

    pillars = [
        "Pillar D (RQ3):\nSpec Integrity & InfoTree",
        "Pillar C (RQ2b):\nAgent Runtime & Protocols",
        "Pillar B (RQ2a):\nPQC, HW & Quantum QKD",
        "Pillar A (RQ1):\nLean 4 ATP & Kernel Gates",
    ]
    full_pdf = [9, 12, 5, 13]    # Sum = 39
    standards = [0, 1, 5, 0]    # Sum = 6
    anchors = [2, 1, 5, 3]      # Sum = 11
    totals = [11, 14, 15, 16]   # Sum = 56
    y = list(range(len(pillars)))

    ax1.barh(y, full_pdf, color="#0f766e", height=0.52, label="Full-Text PDF Audited (n=39)")
    ax1.barh(y, standards, left=full_pdf, color="#2563eb", height=0.52, label="NIST / OWASP Standards (n=6)")
    left_anc = [a + b for a, b in zip(full_pdf, standards)]
    ax1.barh(y, anchors, left=left_anc, color="#64748b", height=0.52, label="Foundational Anchors (n=11)")

    for i, (fp, st, an, tot) in enumerate(zip(full_pdf, standards, anchors, totals)):
        if fp:
            ax1.text(fp / 2, i, str(fp), va="center", ha="center", color="white", fontweight="bold", fontsize=9)
        if st:
            ax1.text(fp + st / 2, i, str(st), va="center", ha="center", color="white", fontweight="bold", fontsize=9)
        if an:
            ax1.text(fp + st + an / 2, i, str(an), va="center", ha="center", color="white", fontweight="bold", fontsize=9)
        ax1.text(tot + 0.35, i, f"{tot} works", va="center", ha="left", fontsize=9, fontweight="bold", color="#0f172a")

    ax1.set_yticks(y)
    ax1.set_yticklabels(pillars, fontsize=8.8)
    ax1.set_xlim(0, 20.5)
    ax1.set_xlabel("Verified Works (Count)", fontsize=9, color="#334155", labelpad=6)
    ax1.set_title("A. Verified Corpus by Pillar & Provenance Tier (N = 56)", fontsize=10.3, fontweight="bold", loc="left", pad=10)
    ax1.legend(
        loc="upper center", bbox_to_anchor=(0.48, -0.20), ncol=3,
        frameon=True, fontsize=7.6, columnspacing=0.9, handletextpad=0.4,
    )
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    fig.text(
        0.04, 0.03,
        "2025–2026 Acceleration: 82.1% of corpus (46/56 works) published in 2025–2026 (30 works in 2026 alone).",
        fontsize=8.2, fontweight="bold", color="#991b1b",
        bbox=dict(boxstyle="round,pad=0.38", facecolor="#fef2f2", edgecolor="#fecaca"),
    )

    ax2.axis("off")
    ax2.set_title("B. PRISMA-2020 Dual-Notebook Grounding Flow", fontsize=10.3, fontweight="bold", loc="left", pad=10)
    boxes = [
        ("1. Systematic Search (7 Sources + Standards)\narXiv, IEEE, ACM, USENIX/NDSS, IACR, NIST/OWASP", "#eff6ff", "#3b82f6", 0.78),
        ("2. Strict EC1–EC4 Exclusion Gate\nDropped general agent surveys & secondary blogs", "#fff7ed", "#f97316", 0.54),
        ("3. Cross-Notebook Full-PDF Audit (NB1 U NB2)\nPinned page/Table/Fig; fixed 7 numeric discrepancies", "#ecfdf5", "#10b981", 0.30),
        ("Verified Corpus (N = 56 Primary Works)\n39 Full-PDF Audited | 6 Standards | 11 Anchors", "#0f172a", "#0f172a", 0.06),
    ]
    for idx, (txt, bg, ec, ypos) in enumerate(boxes):
        fg = "white" if idx == 3 else "#0f172a"
        rect = patches.FancyBboxPatch((0.03, ypos), 0.94, 0.16, boxstyle="round,pad=0.02", facecolor=bg, edgecolor=ec, linewidth=1.4)
        ax2.add_patch(rect)
        ax2.text(0.50, ypos + 0.08, txt, ha="center", va="center", fontsize=7.8, color=fg, fontweight="bold" if idx == 3 else "normal")
        if idx < 3:
            ax2.annotate("", xy=(0.50, boxes[idx + 1][3] + 0.18), xytext=(0.50, ypos - 0.01),
                         arrowprops=dict(arrowstyle="->", color="#475569", lw=1.5))

    fig.subplots_adjust(left=0.17, right=0.98, top=0.80, bottom=0.25, wspace=0.24)
    save_both(fig, "fig1-prisma-screening")


def fig2_taxonomy() -> None:
    """Figure 2: Four-Axis Multi-Dimensional Taxonomy & Structural Failure Traps."""
    fig, ax = plt.subplots(figsize=(12.2, 5.8))
    fig.patch.set_facecolor("white")
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.1)

    ax.text(5, 5.82, "Figure 2: Four-Axis Multi-Dimensional Taxonomy & Structural Failure Traps", ha="center", fontsize=13, fontweight="bold", color="#0f172a")
    ax.text(5, 5.50, "Bridging Lean 4 ATP, Post-Quantum Cryptography, Runtime Agent Security, and Human Proof Auditing (N = 56)", ha="center", fontsize=8.9, color="#475569")

    axes_info = [
        (4.25, "Axis 4: Human Auditability & Specification Integrity",
         "VacQ (268 defects) | SA-PASS (98.8% agree) | claimcheck (87.9–93.1%) | InfoTree (Paperproof)",
         "#fffbeb", "#d97706"),
        (3.05, "Axis 3: Trust Boundary (TCB) & Runtime Policy Enforcement",
         "Lean4Lean (1 bug) | AXLE (0.97s) | Comparator | IFC (CaMeL, FIDES, RTBAS, ACE) | Cedar",
         "#eff6ff", "#2563eb"),
        (1.85, "Axis 2: Security Verification Targets (Dual-Layer Assurance)",
         "Math/Code -> PQC Rust/Lean (SymCrypt, Libcrux) -> AArch64 (Signal) -> HW & QKD -> Agent/A2A",
         "#ecfdf5", "#059669"),
        (0.65, "Axis 1: Neuro-Symbolic Proof Synthesis & Search Architecture",
         "Stepwise RL (Pantograph) -> GRPO (DeepSeek-V2) -> Self-Corr (Goedel-V2) -> Blueprint DAG / Seed 1.5",
         "#f8fafc", "#475569"),
    ]
    for ypos, title, sub, bg, ec in axes_info:
        rect = patches.FancyBboxPatch((0.20, ypos), 6.42, 0.90, boxstyle="round,pad=0.06", facecolor=bg, edgecolor=ec, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(3.41, ypos + 0.58, title, ha="center", va="center", fontsize=9.5, fontweight="bold", color="#0f172a")
        ax.text(3.41, ypos + 0.24, sub, ha="center", va="center", fontsize=7.4, color="#334155")

    for y_from, y_to in [(1.60, 1.82), (2.80, 3.02), (4.00, 4.22)]:
        ax.annotate("", xy=(3.41, y_to), xytext=(3.41, y_from), arrowprops=dict(arrowstyle="->", color="#475569", lw=1.6))

    trap = patches.FancyBboxPatch((6.88, 0.65), 2.90, 4.50, boxstyle="round,pad=0.08", facecolor="#fff1f2", edgecolor="#be123c", linewidth=1.6)
    ax.add_patch(trap)
    ax.text(8.275, 4.90, "Observed Failure Modes (2026)", ha="center", fontsize=9.8, fontweight="bold", color="#9f1239")
    traps = [
        "1. Benchmark Saturation Illusion\nMath <=99.6% vs. Code TE1 <=15.6%\nSA-PASS 11.2% | Surface-B 1.9%",
        "2. Verification Theatre & Cheats\nLibcrux: 13 bugs, 58.4% SMT, NEON 0%\nVERINA cheat 48.5–71.4% | nat_dec 5.6%",
        "3. Contextual & Protocol Gaps\nCI no-boundary breach <=65%\nAgentThread 69.8% | A2ABreak 11 bugs",
        "4. Spec & Toolchain Fragmentation\nHuman spec error 16.4%–38.5%\n268 VacQ defects | Toolchain drift",
    ]
    for i, t in enumerate(traps):
        ax.text(8.275, 4.02 - i * 0.94, t, ha="center", va="center", fontsize=7.9, color="#1e293b",
                bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="#fecdd3"))

    save_both(fig, "fig2-four-axis-taxonomy")


def fig3_paradox() -> None:
    """Figure 3: The Math-to-Code & Semantic Verification Paradox."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.2, 5.4), gridspec_kw={"width_ratios": [1.0, 1.25]})
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "Figure 3: The Math-to-Code Verification Paradox (Competition Math vs. Software & Research Semantics)",
        fontsize=12.6, fontweight="bold", y=0.98, color="#0f172a",
    )

    # Panel A: miniF2F-test progress
    provers = [
        "ReProver (Pass@1)",
        "Pantograph DSP GPT-4o",
        "Kimina-Prover 72B (@8192)",
        "DeepSeek-Prover-V2 (@8192)",
        "Goedel-Prover-V2 32B SC",
        "Goedel-Architect (@1)",
        "Seed-Prover 1.0 (Medium)",
    ]
    scores = [26.5, 28.4, 80.74, 88.9, 90.4, 99.2, 99.6]
    cols = ["#94a3b8", "#64748b", "#3b82f6", "#2563eb", "#1d4ed8", "#0f766e", "#047857"]
    y = range(len(provers))
    ax1.barh(y, scores, color=cols, height=0.56)
    for i, s in enumerate(scores):
        ax1.text(s + 1.2, i, f"{s:.1f}%" if s != 80.74 else "80.7%", va="center", fontsize=8.4, fontweight="bold", color="#0f172a")
    ax1.set_yticks(list(y))
    ax1.set_yticklabels(provers, fontsize=8.4)
    ax1.set_xlim(0, 115)
    ax1.set_xlabel("miniF2F-test Pass Rate (%)", fontsize=8.8)
    ax1.set_title("A. Math Benchmarks Approach Saturation", fontsize=10.2, fontweight="bold", loc="left")
    ax1.text(
        0.00, -0.22,
        "PutnamBench: Seed-Prover 1.5 = 87.9% (580/660); Goedel-Architect (+NL) = 88.8% (597/672).",
        transform=ax1.transAxes, fontsize=7.9, fontweight="bold", color="#0f766e",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#ecfdf5", edgecolor="#a7f3d0"),
    )

    # Panel B: Syntactic/Compile vs Semantic/Verified reality gap
    benchmarks = [
        "VERINA\n(OpenAI o3)",
        "SHADOWBENCH\n(Opus 4.8 +\nNumina)",
        "VeriBench\n(Codex\nGPT-5.4)",
        "Three-Surface\n(Dafny\nOpus 4.7)",
    ]
    syntactic = [41.2, 61.8, 100.0, 99.1]   # Code & Spec (17-2505.23135) / Compile / IC1 / Surface A
    semantic = [3.2, 11.2, 10.2, 1.9]       # End-to-End Verified (17-2505.23135) / SA-PASS / TE1 / Surface B
    gaps = ["-38.0 pp\n(E2E: 3.2%)", "-50.6 pp", "-89.8 pp\n(TE1<=15.6%)", "~50x drop\n(ensures 5.3%)"]

    x = list(range(len(benchmarks)))
    ax2.bar([i - 0.19 for i in x], syntactic, width=0.36, color="#94a3b8", label="Syntactic / Compile / Surface A")
    ax2.bar([i + 0.19 for i in x], semantic, width=0.36, color="#dc2626", label="Verified Proof / Semantic Equivalence")
    for i in x:
        ax2.text(i - 0.19, syntactic[i] + 2.0, f"{syntactic[i]:.1f}%", ha="center", fontsize=8.3, fontweight="bold", color="#334155")
        ax2.text(i + 0.19, semantic[i] + 2.0, f"{semantic[i]:.1f}%", ha="center", fontsize=8.3, fontweight="bold", color="#991b1b")
        ax2.text(i + 0.19, semantic[i] + 15.0, gaps[i], ha="center", fontsize=7.5, fontweight="bold", color="#b91c1c",
                 bbox=dict(boxstyle="round,pad=0.22", facecolor="#fef2f2", edgecolor="#fecaca"))

    ax2.set_xticks(x)
    ax2.set_xticklabels(benchmarks, fontsize=8.0)
    ax2.set_ylim(0, 134)
    ax2.set_ylabel("Success / Equivalence Rate (%)", fontsize=8.8)
    ax2.set_title("B. Severe Collapse on Software & Semantic Alignment", fontsize=10.2, fontweight="bold", loc="left")
    ax2.legend(fontsize=8.0, loc="upper right", frameon=True)

    for ax in (ax1, ax2):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    plt.tight_layout(rect=[0, 0.05, 1, 0.92])
    save_both(fig, "fig3-math-to-code-verification-paradox")


def fig4_pqc_pipelines() -> None:
    """Figure 4: Comparative PQC Verification Pipelines, Libcrux Audit & TCB Boundaries."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 5.2), gridspec_kw={"width_ratios": [1.35, 1.0]})
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "Figure 4: PQC Verification Pipelines, Trust Boundaries & Libcrux Audit Breakdown",
        fontsize=12.6, fontweight="bold", y=0.98, color="#0f172a",
    )

    ax1.axis("off")
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 6)
    ax1.set_title("A. Three PQC Verification Architectures & TCB Scope", fontsize=10.2, fontweight="bold", loc="left")

    cards = [
        (4.15, "1. SymCrypt + Charon/Aeneas (Ho et al., 2026)",
         "Rust (16,680 LOC) -> LLBC -> Lean 4 (237,160 LOC; Spec 2,827 LOC)\n4.7x–5.6x faster HPKE than libcrux | TCB: rustc + Aeneas + SIMD\nOut-of-Scope: Constant-Time / Side-Channel Resistance",
         "#eff6ff", "#2563eb"),
        (2.20, "2. Libcrux + hax Audit (Kobeissi, IACR 2026/192)",
         "Rust (20,808 LOC) -> hax THIR -> F* (138 mods: 127 Z3, 9 ADMIT, 2 SLOW)\n13 Vulnerabilities (9 Unverified V1–V9 + 4 Type V V10–V13)\nARM64 NEON (792 LOC) = 0% Verified | Impairs Signal PQ, hpke-rs, OpenMLS",
         "#fef2f2", "#dc2626"),
        (0.25, "3. AlphaProof Code (Chaudhuri et al., 2026) & QKD/HW Extensions",
         "Unmodified libsignal -> rustc -> AArch64 ELF -> Lean 4 (~6.5M LOC proofs)\nRemoves rustc from TCB (26K LOC TCB); 10 Q(tr,K) queries + 2 planted bugs\nPlus: BB84 Finite-Key QKD in Lean 4 (T0 axioms) & PQC HW 779,945 soak cycles",
         "#ecfdf5", "#059669"),
    ]
    for ypos, title, body, bg, ec in cards:
        r = patches.FancyBboxPatch((0.15, ypos), 9.70, 1.62, boxstyle="round,pad=0.08", facecolor=bg, edgecolor=ec, linewidth=1.5)
        ax1.add_patch(r)
        ax1.text(0.40, ypos + 1.28, title, ha="left", va="center", fontsize=9.1, fontweight="bold", color="#0f172a")
        ax1.text(0.40, ypos + 0.56, body, ha="left", va="center", fontsize=7.9, color="#334155")

    # Panel B: Libcrux ML-KEM + Intrinsics LOC breakdown (Table 5, Kobeissi 2026/192)
    cats = [
        "SMT-Verified\n(Z3 Checked)",
        "Admitted\n(--admit_smt)",
        "Opaque\n(Axioms)",
        "Unextracted\n(Never in F*)",
    ]
    locs = [12149, 3004, 2457, 3198]
    pcts = [58.4, 14.4, 11.8, 15.4]
    bcols = ["#0f766e", "#f97316", "#eab308", "#dc2626"]
    y = range(len(cats))
    ax2.barh(y, pcts, color=bcols, height=0.52)
    for i, (loc, pct) in enumerate(zip(locs, pcts)):
        ax2.text(pct + 1.2, i, f"{pct:.1f}% ({loc:,} LOC)", va="center", fontsize=8.3, fontweight="bold", color="#0f172a")
    ax2.set_yticks(list(y))
    ax2.set_yticklabels(cats, fontsize=8.4)
    ax2.set_xlim(0, 88)
    ax2.set_xlabel("Share of 20,808 Rust LOC (%)", fontsize=8.8)
    ax2.set_title("B. Libcrux Verification Coverage (2026/192 Table 5)", fontsize=10.2, fontweight="bold", loc="left")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.text(
        0.02, -0.18,
        "41.6% of libcrux-ml-kem + intrinsics (8,659 LOC) lacks SMT proofs; NEON 792 LOC = 0%.",
        transform=ax2.transAxes, fontsize=8.0, fontweight="bold", color="#991b1b",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#fef2f2", edgecolor="#fecaca"),
    )

    plt.tight_layout(rect=[0, 0.05, 1, 0.92])
    save_both(fig, "fig4-pqc-verification-pipelines")


def fig5_agent_frontier() -> None:
    """Figure 5: Runtime Agent Security-Utility Frontier & Protocol Audits."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.4, 5.2), gridspec_kw={"width_ratios": [1.18, 1.0]})
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "Figure 5: Runtime Agent Security–Utility Frontier (AgentDojo) & Cross-Protocol Risks",
        fontsize=12.6, fontweight="bold", y=0.98, color="#0f172a",
    )

    # Panel A: Controlled GPT-4o-mini cohort from DRIFT Table 1 & 3 (neurips2025-drift.pdf)
    pts = [
        ("CaMeL\n(0.0% ASR, 35.4% UA\nBU 39.4% | ~7.4x tok)", 0.0, 35.4, "#2563eb", (1.6, -2.5)),
        ("DRIFT\n(1.29% ASR, 47.91% UA\nBU 58.48% | 1.89x tok)", 1.29, 47.91, "#0f766e", (2.2, 1.8)),
        ("Progent\n(9.4% ASR, 45.6% UA\nBU 54.7%)", 9.4, 45.6, "#f97316", (1.5, -7.0)),
        ("Undefended\n(30.7% ASR, 48.3% UA\nBU 63.6% | 0.82M tok)", 30.7, 48.3, "#dc2626", (-10.5, 2.5)),
    ]
    # Pareto line CaMeL -> DRIFT
    ax1.plot([0.0, 1.29], [35.4, 47.91], linestyle="--", color="#0f766e", lw=1.6, label="Empirical Security–Utility Frontier")
    for label, asr, ua, col, (dx, dy) in pts:
        ax1.scatter([asr], [ua], s=110, color=col, zorder=5, edgecolors="white", linewidth=1.2)
        ax1.annotate(
            label, xy=(asr, ua), xytext=(asr + dx, ua + dy),
            fontsize=7.8, fontweight="bold", color="#0f172a",
            bbox=dict(boxstyle="round,pad=0.25", facecolor="#f8fafc", edgecolor=col, lw=1.0),
            arrowprops=dict(arrowstyle="-", color="#94a3b8", lw=0.8),
        )
    ax1.set_xlim(-2, 36)
    ax1.set_ylim(28, 57.5)
    ax1.set_xlabel("Attack Success Rate — ASR (%) [Lower is Safer]", fontsize=8.8)
    ax1.set_ylabel("Utility Under Attack — UA (%) [Higher is Better]", fontsize=8.8)
    ax1.set_title("A. AgentDojo Controlled Cohort (GPT-4o-mini, DRIFT Table 1)", fontsize=10.0, fontweight="bold", loc="left")
    ax1.grid(alpha=0.25, linestyle=":")
    ax1.legend(loc="lower right", fontsize=8.0)

    # Panel B: Cross-Benchmark Security & Protocol Audits
    metrics = [
        "ACE INJECAGENT Security\n(1,054 tests | Util 83.5%)",
        "FIDES* Tool Attack Defense\n(0 injections; o3 +15.9%)",
        "Progent AgentDojo Defense\n(ASR 39.9% -> 1.0%)",
        "A2ABreak Spec F1\n(11 std bugs, Prec 73.3%)",
        "AgentThread Cross-Boundary\nCounterexamples (30/43)",
        "CI No-Boundary Violation\n(GPT-5.2; PG2 AUROC 0.59)",
    ]
    vals = [100.0, 100.0, 99.0, 84.6, 69.8, 65.0]
    mcols = ["#0f766e", "#059669", "#0284c7", "#f59e0b", "#ea580c", "#dc2626"]
    y = range(len(metrics))
    ax2.barh(y, vals, color=mcols, height=0.54)
    for i, v in enumerate(vals):
        lbl = f"{v:.1f}% defense" if i < 3 else (f"{v:.1f}% F1" if i == 3 else f"{v:.1f}% failure")
        ax2.text(v + 1.2, i, lbl, va="center", fontsize=8.0, fontweight="bold", color="#0f172a")
    ax2.set_yticks(list(y))
    ax2.set_yticklabels(metrics, fontsize=7.9)
    ax2.set_xlim(0, 128)
    ax2.set_xlabel("Rate / Score (%)", fontsize=8.8)
    ax2.set_title("B. Deterministic IFC Defenses vs. Protocol/CI Gaps", fontsize=10.0, fontweight="bold", loc="left")

    for ax in (ax1, ax2):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.92])
    save_both(fig, "fig5-agent-security-utility-frontier")


def fig6_auditing() -> None:
    """Figure 6: Human Proof Auditing Architecture (Expr vs. InfoTree + Mechanical Gates)."""
    fig, ax = plt.subplots(figsize=(12.2, 5.4))
    fig.patch.set_facecolor("white")
    ax.axis("off")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6.2)

    ax.text(6, 5.92, "Figure 6: Human-Auditable Formal Verification Architecture (Expr vs. InfoTree & Spec Gates)",
            ha="center", fontsize=12.6, fontweight="bold", color="#0f172a")
    ax.text(6, 5.60, "Restoring semantic auditability over 237K–6.5M LOC proofs via Lean 4 InfoTree visualization and automated specification linters",
            ha="center", fontsize=8.8, color="#475569")

    # Left Track: Legacy Expr (#explode)
    left_box = patches.FancyBboxPatch((0.25, 2.75), 3.4, 2.55, boxstyle="round,pad=0.08", facecolor="#fef2f2", edgecolor="#dc2626", linewidth=1.6)
    ax.add_patch(left_box)
    ax.text(1.95, 5.02, "Legacy Track: Kernel Expr (#explode)", ha="center", fontsize=9.4, fontweight="bold", color="#991b1b")
    l_steps = [
        "1. Lean 4 Kernel Term (Expr)\nRaw lambda abstractions & applications",
        "2. Abstraction Erasure\nDistinct proof tactics collapse identically",
        "3. Massive Fitch Table\nOpaque to security auditors on large code",
    ]
    for i, s in enumerate(l_steps):
        ax.text(1.95, 4.35 - i * 0.65, s, ha="center", va="center", fontsize=7.9, color="#1e293b",
                bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor="#fecaca"))

    # Right Track: Modern InfoTree Visualization
    right_box = patches.FancyBboxPatch((4.05, 2.75), 7.70, 2.55, boxstyle="round,pad=0.08", facecolor="#ecfdf5", edgecolor="#059669", linewidth=1.6)
    ax.add_patch(right_box)
    ax.text(7.90, 5.02, "Modern Track: Snapshot.infoTree + Gentzen Visualization", ha="center", fontsize=9.6, fontweight="bold", color="#065f46")

    r_cards = [
        (4.22, "Snapshot.infoTree\nPre/post Hypotheses\n& Goals per tactic"),
        (6.82, "Paperproof / LeanTree\nBetterParser (Lean RPC)\n-> 1-to-1 Gentzen Tree"),
        (9.42, "ProofWidgets4 UI\nHypotheses down, Goals up\nNested scope boxes"),
    ]
    for xp, txt in r_cards:
        r = patches.FancyBboxPatch((xp, 3.15), 2.15, 1.45, boxstyle="round,pad=0.05", facecolor="white", edgecolor="#10b981", linewidth=1.3)
        ax.add_patch(r)
        ax.text(xp + 1.075, 3.88, txt, ha="center", va="center", fontsize=7.4, fontweight="bold", color="#0f172a")
    ax.annotate("", xy=(6.76, 3.88), xytext=(6.43, 3.88), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.8))
    ax.annotate("", xy=(9.36, 3.88), xytext=(9.03, 3.88), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.8))

    # Bottom Mechanical Spec-Integrity Gates
    gate_box = patches.FancyBboxPatch((0.25, 0.30), 11.50, 2.05, boxstyle="round,pad=0.08", facecolor="#eff6ff", edgecolor="#2563eb", linewidth=1.6)
    ax.add_patch(gate_box)
    ax.text(6.0, 2.08, "Automated Mechanical Specification-Integrity Gates (Bridging to Human Audit)", ha="center", fontsize=9.6, fontweight="bold", color="#1e3a8a")

    gates = [
        (0.45, "VacQ + mpmathx\n(Beyond LLM Judge)\n268 confirmed defects\nin ProofNet / RLM25"),
        (2.70, "SA-PASS Equivalence\n(SHADOWBENCH)\n98.8% human agreement\nvs. 17.8% compile rate"),
        (4.95, "claimcheck\nBlind Back-Translation\nMacro Recall: Lean 87.9%\nIsabelle 91.3%, Dafny 93.1%"),
        (7.20, "Three-Surface & Harness\nCatches 25.7% empty JML;\nSurface-B drops ~50x;\nCodex 0.30 -> 0.49"),
        (9.45, "ICML Linter & T0 Audit\n398 certified issues (Div/0);\nAXLE 0.97s; ProofGate T0;\nFlags C1–C6 / sorry / nat_dec"),
    ]
    for xp, txt in gates:
        g = patches.FancyBboxPatch((xp, 0.50), 2.10, 1.30, boxstyle="round,pad=0.05", facecolor="white", edgecolor="#60a5fa", linewidth=1.2)
        ax.add_patch(g)
        ax.text(xp + 1.05, 1.15, txt, ha="center", va="center", fontsize=7.6, color="#0f172a")

    ax.annotate("", xy=(7.90, 2.72), xytext=(7.90, 2.38), arrowprops=dict(arrowstyle="<->", color="#1d4ed8", lw=1.8))
    save_both(fig, "fig6-human-proof-auditing")


if __name__ == "__main__":
    fig1_prisma()
    fig2_taxonomy()
    fig3_paradox()
    fig4_pqc_pipelines()
    fig5_agent_frontier()
    fig6_auditing()
    print(f"Generated 6 English 300-DPI figure pairs (.png + .svg) in: {OUT}")

    # Auto-package zip when running on Colab for 1-click download
    if Path("/content").exists():
        zip_path = Path("/content/work/paper0_figures.zip")
        zip_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in sorted(OUT.glob("*")):
                zf.write(p, arcname=p.name)
        print(f"Packaged zip for download: {zip_path}")
        try:
            from google.colab import files
            files.download(str(zip_path))
        except Exception:
            pass
