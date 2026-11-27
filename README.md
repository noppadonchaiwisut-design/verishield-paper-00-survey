# Paper 00: Neuro-Symbolic Formal Verification Umbrella Survey (2024–2026)

- **ชื่อบทความ (ไทย):** การพิสูจน์เชิงรูปนัยแบบนิวโร-ซิมโบลิกในยุคเอเจนต์ให้เหตุผล (2024–2026): จากการพิสูจน์ทฤษฎีอัตโนมัติสู่ AI Agent ที่ปลอดภัยอย่างพิสูจน์ได้และโครงสร้างพื้นฐานสำคัญหลังควอนตัม
- **Title (English):** Neuro-Symbolic Formal Verification in the Era of Reasoning Agents (2024–2026): From Automated Theorem Proving to Provably Safe AI Agents and Post-Quantum Critical Infrastructure
- **ผู้วิจัย (Author):** นพดล ชัยวิสูตร (Noppadon Chaiwisut) | Independent Researcher, Thailand | ORCID: `0009-0005-2881-8458`
- **สถานะปัจจุบัน (Status):** **`PASS QA (Step 4C Complete)`** — ครบทั้งฉบับภาษาไทย 100% (Step 4A), ภาพ `300 DPI` 6 ภาพ (`.png` + `.svg`), ฉบับภาษาอังกฤษ + LaTeX 2 คอลัมน์ (`manuscript_en/paper0_en.md`, `main.tex`, `references.bib`, `compile_paper0_pdf_colab.py`), ไฟล์ PDF (`manuscript_en/paper0-umbrella-survey.pdf`), แพ็กเกจ Overleaf Bundle (`manuscript_en/paper0-overleaf-bundle.zip`), `CITATION.cff`, และสัญญาอนุญาต `LICENSE` (`CC BY 4.0`) เรียบร้อยแล้ว

## โครงสร้างไฟล์ในโฟลเดอร์ (Directory Structure)

| ไฟล์ / โฟลเดอร์ | รายละเอียด |
| :--- | :--- |
| `paper-00-umbrella-survey.md` | ต้นฉบับภาษาไทย 100% (UCAI Style: อ้างอิง `[1]–[56]` พร้อม URL จริงคลิกได้ + ตารางสอบทานพิกัด PDF ข้ามสมุดโน้ต) |
| `manuscript_en/paper0_en.md` | ต้นฉบับภาษาอังกฤษ 100% (Step 4B — ล็อกตัวเลข ตาราง และอ้างอิง `[1]–[56]` ตรงกับฉบับไทยทุกจุด) |
| `manuscript_en/main.tex` | ต้นฉบับ LaTeX 2 คอลัมน์ (`hyperref` ลิงก์สีน้ำเงิน, `natbib` + `unsrtnat`, ใช้ภาพ 300 DPI ร่วมจาก `../figures/`) |
| `manuscript_en/references.bib` | ฐานข้อมูลบรรณานุกรม BibTeX ครบ 56 รายการ ลำดับตรง `[1]–[56]` 100% พร้อม URL จริงคลิกได้ |
| `manuscript_en/compile_paper0_pdf_colab.py` | สคริปต์คอมไพล์ PDF บน Google Colab (`/content/work/` ตามกฎ Local-NVMe-First) และแพ็กชุดอัปโหลด Overleaf `.zip` |
| `manuscript_en/paper0-overleaf-bundle.zip` | แพ็กเกจพร้อมคอมไพล์ (รวม `main.tex`, `references.bib`, `compile_paper0_pdf_colab.py` และภาพ `300 DPI` ทั้ง 6 ภาพ) |
| `manuscript_en/paper0-umbrella-survey.pdf` | ไฟล์ PDF 2 คอลัมน์ฉบับภาษาอังกฤษที่คอมไพล์จาก LaTeX |
| `generate_paper0_figures.py` | สคริปต์ Python วาดภาพ `2200+ px` (`300 DPI`, `.png` + `.svg`) ป้ายอังกฤษล้วนครบทั้ง 6 ภาพ พร้อมแพ็ก `.zip` อัตโนมัติบน Colab |
| `paper-00-umbrella-survey-1-notebooklm.md` | บันทึกตรวจสอบต้นฉบับ PDF จาก NotebookLM สมุดโน้ตที่ 1 (RQ1 + RQ3) |
| `paper-00-umbrella-survey-2-notebooklm.md` | บันทึกตรวจสอบต้นฉบับ PDF จาก NotebookLM สมุดโน้ตที่ 2 (RQ2a + RQ2b) |
| `figures/fig1-prisma-screening.png` | ภาพที่ 1: คลังวรรณกรรม PRISMA-2020 ($N=56$) และกระบวนการสอบทาน |
| `figures/fig2-four-axis-taxonomy.png` | ภาพที่ 2: อนุกรมวิธานหลายมิติ 4 แกน และโหมดความล้มเหลว 4 ประการ |
| `figures/fig3-math-to-code-verification-paradox.png` | ภาพที่ 3: ความย้อนแย้ง Math-to-Code (`miniF2F` vs. `VERINA` / `SHADOWBENCH` / `VeriBench`) |
| `figures/fig4-pqc-verification-pipelines.png` | ภาพที่ 4: เปรียบเทียบสายพาน PQC (`SymCrypt`, `Libcrux`, `AlphaProof Code`) และผลตรวจ `libcrux` |
| `figures/fig5-agent-security-utility-frontier.png` | ภาพที่ 5: ขอบเขตความมั่นคงกับอรรถประโยชน์บน AgentDojo และช่องโหว่โปรโตคอล |
| `figures/fig6-human-proof-auditing.png` | ภาพที่ 6: สถาปัตยกรรมการตรวจสอบโดยมนุษย์ (`Expr` vs. `InfoTree` + ประตูตรวจสเปกเชิงกลไก) |
| `CITATION.cff` | ข้อมูลเมตาการอ้างอิงมาตรฐานพร้อม ORCID ผู้วิจัย |
| `LICENSE` | สัญญาอนุญาตเปิดสาธารณะ Creative Commons Attribution 4.0 International (`CC BY 4.0`) |
