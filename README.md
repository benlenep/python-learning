# python-learning

A public record of me learning Python for data science, coming from an R background in actuarial modelling, forecasting and retention analysis.

The plan runs from 5 October to 31 December 2026 and is built around five milestones. Each one produces something you can open and check, rather than a course certificate.

## Why this repository exists

I already work in R for forecasting, lapse modelling and pipeline automation. This project translates those skills into Python and adds the engineering habits that data science roles expect: version control, testing, automated checks and deployment.

Everything here uses public or simulated data.

## Milestones

| # | Milestone | Due | Status |
| --- | --- | --- | --- |
| 1 | Foundations: tooling, Git workflow, first notebook reproducing an R analysis | 18 Oct | Complete |
| 2 | R and Python parity: the same public-data analysis in both languages, with tests confirming the outputs match | 8 Nov | [ ] |
| 3 | Lapse modelling: survival and gradient boosting models on a simulated membership book, with a time-based backtest | 6 Dec | [ ] |
| 4 | Forecasting pipeline: tested, scheduled, with automated checks and a live app | 20 Dec | [ ] |
| 5 | Portfolio and write-up: portfolio page and an article on moving a lapse workflow from R to Python | 31 Dec | [ ] |

## Toolkit

| Job | R | Python |
| --- | --- | --- |
| Environments and packages | renv | uv |
| Data wrangling | dplyr, tidyr | pandas |
| SQL | DBI | DuckDB |
| Plotting | ggplot2 | plotnine, matplotlib |
| Modelling | tidymodels, survival | scikit-learn, statsmodels, lifelines |
| Testing | testthat | pytest |

## Repository layout

```text
python-learning/
├── sessions/          notebooks and exercises, one per study session
├── src/python_learning/   reusable code as it matures
├── main.py            starter script
├── pyproject.toml     project metadata and dependencies
└── uv.lock            exact package versions
```

Larger milestone projects will live in their own repositories and be linked here.

## Running the code

This project uses [uv](https://docs.astral.sh/uv/). To run it yourself:

```bash
git clone git@github.com:benlenep/python-learning.git
cd python-learning
uv sync
uv run python main.py
```

## Progress log

Short notes on what I learned each week, including mistakes. Newest first.

- *Week 1 (5 to 11 Oct):* set up uv, VS Code, Git and SSH; first push to GitHub.

### Milestone 1 plan (Python version of my AFL Shiny app)

- **Question:** Does AFL scoring drop after the first six rounds of the home-and-away season, and how consistently has that held from 2016 to 2025?
- **Dataset:** Home-and-away match results for 2016 to 2025 from [AFL Tables](https://afltables.com), pulled with the [fitzRoy](https://github.com/jimmyday12/fitzRoy) R package and saved as `afl_match_data.csv` (one row per match). Finals are excluded; Opening Round matches are coded as Round 0.
- **Results to reproduce:**
  1. Early (Rounds 0 to 6) vs rest-of-season average points per team for every season, with the drop and how many seasons show early scoring higher.
  2. The full early vs rest summary for 2025: games, average team score, average combined score, average winning margin, % of games with a 100+ score, and highest combined score.
- **Chart:** Paired bars by season comparing early-season and rest-of-season average points per team.
- **Repository:** `afl-early-season-scoring-r-to-python`

### Milestone 2 plan (R and Python pipeline parity, due 8 Nov)

- **Question:** Can the data pipeline behind my AFL early-season scoring dashboard be rebuilt in Python so that every output matches the original R version exactly, with automated tests proving it?
- **Dataset:** Raw home-and-away and finals results for 2016 to 2025 from [AFL Tables](https://afltables.com), pulled once with the [fitzRoy](https://github.com/jimmyday12/fitzRoy) R package and saved as `data/raw_results.csv`, so both languages read an identical input. fitzRoy checked on 25 Oct: 2025 returned 207 regular-season and 9 finals matches, with a 4-game Opening Round.
- **Pipeline steps to reproduce:**
  1. Keep home-and-away matches only (drop finals)
  2. Detect Opening Round seasons (a Round 1 with fewer than 7 games) and recode them: Opening Round becomes Round 0, later rounds shift down by 1
  3. Build the match table: nicknames, scores, combined and average team score, margin, winner or draw, 100+ flags, season phase
  4. Summarise by season and round, and by season and phase (early Rounds 0 to 6 vs rest of season)
- **Outputs to match:**
  1. `match_data`: one row per match, 17 columns
  2. `round_summary`: one row per season and round
  3. `phase_summary`: one row per season and phase
- **Tests:** pytest parity tests comparing all three Python outputs with R's, plus unit tests on small hand-made inputs for finals filtering, Opening Round detection and recoding, and draws.
- **Charts:** round-by-round average points per team for one season (coloured by phase) and a multi-season comparison, ported from the Shiny app to plotnine.
- **Out of scope:** the Shiny interface, value boxes and the hand-compiled `afl_yearly_averages.csv`. Chart reference lines are calculated from match data instead.
- **Quirks to keep for parity:** the match table labels the later phase "Mid/Late Season" while the summaries say "Rest of Season", and 2020 (shortened quarters) is included. Both match the original R code.
- **Repository:** `afl-data-pipeline-r-to-python`

## Principles

- **Translate, do not restart.** Every exercise maps to something I already do in R, so I can check the answers.
- **Ship artefacts, not hours.** A milestone counts only when there is a link to show for it.
- **Be honest about level.** This is a learning repository, so early code will be rough on purpose.
