# docs/

Facilitator-facing material — not part of the student `lab/` tree.

```
curriculum/         Week-by-week curriculum plan and camp implementation requirements
facilitator-notes/  Day-by-day running notes, gotchas, per-session tips, kit test checklist
assembly/           Robot assembly instructions and Pi connection guide (images/ has assembly photos)
setup-scripts/      Helper scripts for deploying to and copying files onto kit Pis
```

All documents are Markdown so they render on GitHub and stay diffable. `curriculum/Step_Up_To_STEM_AI_Curriculum_Plan.md` is marked as a confidential draft by its author — check before sharing outside the team.

Before using the deploy scripts, copy `setup-scripts/kits.txt.example` to `setup-scripts/kits.txt` and fill in your camp's actual kit names/IPs (`kits.txt` is gitignored since it's specific to each camp's local network).

`ADAS_AI_Lab_Camp_Documentation.docx` is a single combined Word copy of everything above (curriculum, facilitator notes, checklist, assembly guides), generated with `pandoc` for anyone who wants one downloadable/printable file instead of browsing folders. The Markdown files are the source of truth — regenerate the `.docx` after editing them:

```bash
cd summer26-adasai
TMPFILE=$(mktemp /tmp/combined_docs_XXXX.md)
cat docs/curriculum/Step_Up_To_STEM_AI_Curriculum_Plan.md \
    "docs/curriculum/AI-Powered Adaptive Robotics Camp_ Implementation Requirements.md" \
    docs/facilitator-notes/Facilitator_Notes.md \
    docs/facilitator-notes/Kit_Test_Checklist.md \
    docs/assembly/Yahboom_G1_Assembly_Tips_for_Helpers.md \
    docs/assembly/Connecting_to_Your_Pi.md > "$TMPFILE"
pandoc "$TMPFILE" -o docs/ADAS_AI_Lab_Camp_Documentation.docx \
    --resource-path=.:docs/assembly:docs/assembly/images \
    --toc --toc-depth=2 -M title="ADAS AI Lab — Camp Documentation"
rm "$TMPFILE"
```
