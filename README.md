# python\_notes

> **A real code sandbox – not a slide deck.** Every folder in this repo contains executable notebooks or scripts you can run right now to see how I write Python, explore data, and build mini‑utilities.

---

## 📁 Repo at a glance

```
python_notes/
├── 1-Python-Basics/        # Language deep‑dives & small utilities
│   ├── app.py              # demo main
│   ├── *.ipynb             # decorators, OOP, file‑ops, etc.
│   ├── logs/               # logging demo (app.py + logger.py)
│   └── package/            # custom pkg & sub‑package example
├── 2-data-analysis/        # Pandas/NumPy notebooks + sample data
│   ├── *.ipynb             # EDA, SQL, visualisation
│   └── *.csv / *.xlsx      # public datasets used in notebooks
├── app.py                  # lightning‑quick sanity check (prints 2)
├── requirements.txt        # minimal runtime deps
└── .gitignore              # keeps venv & data out of Git
```

### What you can inspect quickly

| Topic                 | File / Notebook                                     |
| --------------------- | --------------------------------------------------- |
| Decorators & timing   | `1-Python-Basics/decorators.ipynb`                  |
| Operator overloading  | `1-Python-Basics/operatoroverloading.ipynb`         |
| Concurrency intro     | `1-Python-Basics/multithreading.py` + `multipro.py` |
| Structured logging    | `1-Python-Basics/logs/logger.py`                    |
| Pandas join/merge     | `2-data-analysis/pandas.ipynb`                      |
| SQL from Pandas       | `2-data-analysis/sql.ipynb`                         |
| Matplotlib vs Seaborn | `2-data-analysis/dataviz.ipynb`                     |

---

## 🚀 Setup & run

```bash
# clone
 git clone https://github.com/samvillasmith/python_notes.git && cd python_notes

# create isolated env (choose one)
 python -m venv .venv && source .venv/bin/activate      # venv (Mac/Linux)
 .venv\Scripts\activate                                 # venv (Windows)
 # OR
 conda env create -f environment.yml && conda activate python_notes

# install minimal deps
 pip install -r requirements.txt

# run a notebook
 jupyter lab 1-Python-Basics/decorators.ipynb

# run logging demo
 python 1-Python-Basics/logs/app.py
```

Everything should execute on **Python 3.11+** with < 100 MB RAM.

---

## 🎯 Why this repo exists

1. **Daily kata:** I sharpen language muscles by rewriting core patterns (decorators, context managers, dunders).
2. **Reference snippets:** Quick copy‑paste recipes for ETL, logging, and concurrency.
3. **Technical writing samples:** Each notebook includes markdown narrative so reviewers see how I explain concepts.

> For production‑grade projects (CI/CD, Docker, cloud deploy) check my pinned repos.

---

## 📝 License

MIT – clone, learn, reuse.

*Last updated: July 2025*
