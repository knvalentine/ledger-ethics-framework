# Roadmap to a Practical “Ledger-Balanced Life” Framework

> Version 0.1   —  2025-07-11  
> Maintainers: *open for volunteers*

---

## Motivation

The *ledger-ethics* Lean repository provides a rigorous **specification** for an ethics ledger, but it remains mathematically incomplete (`sorry`s).  This roadmap describes how to turn the *existing* ideas into a **usable lifestyle & tooling suite** while the formal proofs mature.

---

## Phase 0 • Groundwork (Weeks 0–2)

| Task | Owner | Deliverables |
|------|-------|--------------|
| 0.1  Collect and summarize core concepts: recognition debt, eight-beat virtues, curvature heuristics | Ethics Lead | `CONCEPTS_SUMMARY.md` |
| 0.2  Define MVP user stories (individual, team, open-source community) | Product | `USER_STORIES.md` |
| 0.3  Select lightweight storage format (Markdown, CSV, or SQLite) for personal ledger entries | Engineering | Decision doc |
| 0.4  Draft a **glossary** mapping Lean identifiers → plain-English terms | Documentation | `GLOSSARY.md` |

---

## Phase I • Prototype CLI Ledger (Weeks 3–6)

1. Minimal command-line tool (`ledgercli`)
   * `add`   — record action/benefit/debt/virtue
   * `balance` — show net recognition balance
   * `export` — output CSV/JSON for analysis
2. Implement file-based storage (one YAML per day).
3. Continuous integration: unit tests, style checks.
4. Publish v0.1 on GitHub + Homebrew tap / PyPI.

*Dependencies*: Phase 0 completion.

---

## Phase II • Virtue Budgeting Dashboard (Weeks 7–10)

* React / Svelte web UI reading the same data store.
* Radial chart of virtue allocation vs. budget.
* Weekly email summary (GH Actions or cron).
* OAuth login for optional cloud sync (Supabase).

---

## Phase III • Social Ledger & API (Weeks 11–16)

1. **Ledger Adapter API**
   * REST/GraphQL endpoints mirroring Lean’s `LedgerAdapter.lean` signatures.
   * Auth: JWT + scoped tokens.
2. Team workspaces
   * Shared recognition pool
   * Role-based permissions (viewer, editor, auditor).
3. Federation sketch (ActivityPub or Matrix) for inter-ledger interoperability.

---

## Phase IV • Curvature-Aware Recommendations (Weeks 17–22)

* Heuristic engine tagging entries with “environmental curvature.”
* Suggest extra deliberation or peer-review for high-curvature tasks.
* Initial model: TF-IDF complexity + rate-of-change metric.
* Later: integrate formal proofs once `Curvature.lean` is complete.

---

## Phase V • Formal Proof Hooks (Weeks 23–30)

* Bidirectional link: each ledger rule points to Lean theorem ID.
* CI check: fails build if referenced theorem still contains `sorry`.
* Generate human-readable proof sketches in docs/ from Lean.

---

## Phase VI • Pilot Programs (Weeks 31–40)

* **Individual Beta**: 10 users, daily journaling, feedback form.
* **Open-Source Project Pilot**: track PR reviews & contributions.
* **Org-level Trial**: small nonprofit balances recognition across teams.

Metrics:
* User retention & engagement
* Recognition balance variance
* Subjective well-being survey

---

## Phase VII • Governance & Ecosystem (Weeks 41–52)

* Community charter & code of conduct.
* Plugin marketplace (importers for GitHub, JIRA, Slack, etc.).
* Funding model: donation pool weighted by recognition credits.
* Annual audit tying practical ledger stats to updated Lean proofs.

---

## Long-Term Milestones

| Year | Goal |
|------|------|
| 1    | 1000 active users; 75 % proofs complete |
| 2    | Inter-ledger federation spec v1.0; zero-`sorry` core modules |
| 3    | Recognized by standards body as reference model for responsible AI & governance |

---

## Appendices

### A. Initial Data Schema (YAML)
```yaml
- date: 2025-07-11
  agent: "Alice"
  action: "Reviewed PR #42"
  value: 3   # recognition credits
  virtue: "Transparency"
  settlement: "pending"
```

### B. Tooling Stack Choices
* **CLI**   Python + Typer or Rust + Clap
* **Dashboard**   TypeScript + SvelteKit
* **API**   FastAPI + PostgreSQL or Elixir + Phoenix

### C. Risk Register
| Risk | Mitigation |
|------|------------|
| Over-engineering before fit | Tight six-week sprints, MVP first |
| Mathematical spec drifts | fortnightly sync between dev & theorem-provers |
| User privacy concerns | local-first storage; end-to-end encryption roadmap |

---

## Updated Architecture Overview (2025-07-11)

The practical framework now follows a **two-layer model** that cleanly separates formal specification (Lean proofs) from pragmatic tooling used day-to-day.

```
┌──────────────────────────┐       ┌──────────────────────────────┐
│  Spec Layer (Lean 4)     │       │  Application Layer (Python)  │
│  vendor/ledger-ethics    │──────►│  CLI · API · Dashboard       │
└──────────────────────────┘       └──────────────────────────────┘
```

* Spec layer: remains untouched, updated weekly by an automated GH Action.
* Application layer: imports concepts, exposes usable commands and UIs.

### Directory Layout
```
ledger-ethics-framework/
├── cli/                 # `ledgercli` Typer commands
├── server/              # FastAPI service (later phase)
├── ui/                  # SvelteKit dashboard (later phase)
├── adapters/            # Lean-bridge helpers (proof status, glossary)
├── data/                # YAML → SQLite storage layers
├── tests/               # pytest suite
├── docs/                # MkDocs site
├── vendor/ledger-ethics # Git submodule (spec layer)
└── .github/workflows/   # CI + auto-update workflow
```

### Technology Stack
* **Python 3.11**  + Typer (CLI) • Pydantic (models) • FastAPI (API)
* **Storage**  YAML files → SQLite/Postgres migration path
* **Frontend** SvelteKit + Tailwind (Phase II)
* **Lean integration** shelling out to `lake` for proof status checks
* **CI** GitHub Actions: lint (ruff), tests, auto-update submodule PR bot

### Automated Submodule Refresh
A weekly workflow (`update-ledger-ethics.yml`) already keeps the
`vendor/ledger-ethics` submodule current by opening an automated PR.

---

## Immediate Action Items (Phase 0 Extension)

| ID | Task | Owner | Status |
|----|------|-------|--------|
| 0.5 | Scaffold Python package (`cli/`, `data/`, etc.) | Engineering | ▢ |
| 0.6 | Add Poetry/requirements, lint & test GH Action  | Engineering | ▢ |
| 0.7 | Draft Pydantic models for YAML schema            | Engineering | ▢ |
| 0.8 | Implement `ledgercli add` command + unit test    | Engineering | ▢ |
| 0.9 | Document glossary mapping Lean ➜ plain English   | Docs        | ▢ |

These items will bring the repo to a point where CI is green and the
framework can record a basic ledger entry end-to-end.

---

*Document updated automatically by the assistant on 2025-07-11.* 