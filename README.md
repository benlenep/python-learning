# python-learning

A public record of me learning Python for data science, coming from an R background in actuarial modelling, forecasting and retention analysis.

The plan runs from 5 October to 31 December 2026 and is built around five milestones. Each one produces something you can open and check, rather than a course certificate.

## Why this repository exists

I already work in R for forecasting, lapse modelling and pipeline automation. This project translates those skills into Python and adds the engineering habits that data science roles expect: version control, testing, automated checks and deployment.

Everything here uses public or simulated data.

## Milestones

| # | Milestone | Due | Status |
| --- | --- | --- | --- |
| 1 | Foundations: tooling, Git workflow, first notebook reproducing an R analysis | 18 Oct | [ ] |
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

## Principles

- **Translate, do not restart.** Every exercise maps to something I already do in R, so I can check the answers.
- **Ship artefacts, not hours.** A milestone counts only when there is a link to show for it.
- **Be honest about level.** This is a learning repository, so early code will be rough on purpose.