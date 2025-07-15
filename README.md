# python\_notes

> **A real code sandbox – not a slide deck.** Every folder contains *executable* notebooks or scripts so you can watch me write Python, explore data, and build mini‑utilities.

---

## 📁 Repo at a glance

```text
python_notes/
├── 1-Python-Basics/          # Language deep‑dives & small utilities
│   ├── app.py                # tiny demo main
│   ├── *.ipynb               # decorators, OOP, file‑ops, etc.
│   ├── advanced_multithreading.py    # futures + queues
│   ├── multithreading*.py            # intro + scraping demo
│   ├── factor*_processing.py         # multiprocessing example
│   ├── logs/                 # structured logging demo (app.py + logger.py)
│   └── package/              # custom pkg & sub‑package example
├── 2-data-analysis/          # Pandas/NumPy notebooks + sample data
│   ├── *.ipynb               # EDA, SQL, visualisation
│   ├── *.csv / *.xlsx / *.db # public datasets used in notebooks
│   └── mcc_data.pkl          # pickled DataFrame for memory‑profiling
├── app.py                    # lightning‑quick sanity check (prints 2)
├── requirements.txt          # minimal runtime deps
└── .gitignore                # keeps venv & data out of Git
```

### What you can inspect quickly

| Topic                     | File / Notebook                                     |
| ------------------------- | --------------------------------------------------- |
| Decorators & timing       | `1-Python-Basics/decorators.ipynb`                  |
| Operator overloading      | `1-Python-Basics/operatoroverloading.ipynb`         |
| Concurrency ‑ intro       | `1-Python-Basics/multithreading.py` + `multipro.py` |
| Concurrency ‑ deep dive   | `1-Python-Basics/advanced_multithreading.py`        |
| Web‑scraping with threads | `1-Python-Basics/multithreading_scraping.py`        |
| Structured logging        | `1-Python-Basics/logs/logger.py` + `logging.ipynb`  |
| Memory management tips    | `1-Python-Basics/memory_management.ipynb`           |
| Pandas join / merge       | `2-data-analysis/pandas.ipynb`                      |
| Vectorised data wrangling | `2-data-analysis/datamanipulation.ipynb`            |
| SQL from Pandas           | `2-data-analysis/sql.ipynb`                         |
| Matplotlib **vs** Seaborn | `2-data-analysis/dataviz.ipynb`                     |
| NumPy essentials          | `2-data-analysis/numpy.ipynb`                       |

---

## 🚀 Setup & run

```bash
# clone
git clone https://github.com/samvillasmith/python_notes.git && cd python_notes

# create isolated env (choose one)
python -m venv .venv && source .venv/bin/activate      # venv (Mac/Linux)
.venv\Scripts\activate                               # venv (Windows)
# OR (if you prefer conda)
conda create -n python_notes python=3.11 && conda activate python_notes

# install dependencies
pip install -r requirements.txt

# run a notebook
jupyter lab 1-Python-Basics/decorators.ipynb

# run logging demo
python 1-Python-Basics/logs/app.py
```

All notebooks execute on **Python 3.11+** and comfortably fit in **< 100 MB RAM** (even the heavy NumPy demos stay slim).

---

## 🎯 Why this repo exists

1. **Daily kata:** I sharpen language muscles by rewriting core patterns (decorators, context managers, dunders).
2. **Reference snippets:** Quick copy‑paste recipes for ETL, logging, concurrency, and data wrangling.
3. **Technical writing samples:** Each notebook includes markdown narrative so reviewers see how I explain concepts.

> For production‑grade projects (CI/CD, Docker, cloud deploy) check my pinned repos.

---

## 📝 License

MIT – clone, learn, reuse.

<sub>Last updated: July 15, 2025</sub>
