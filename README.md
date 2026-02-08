# Wildfires in the States — MyST Book

This project publishes a book-style analysis site from a Jupyter notebook using **MyST**.  
It analyzes U.S. wildfire patterns (1992–2015) from the FPA FOD dataset.

## Project structure

```text
wildfires_in_the_states/
├─ project.ipynb          # Main analysis notebook
├─ download_kaggle.py     # Script to download dataset
├─ requirements.txt       # Python dependencies
├─ myst.yml               # MyST project config
├─ book/                  # Generated book site
├─ _build/                # Generated site/build artifacts
└─ README.md
```

## Prerequisites

- Python 3.10+ (recommended: same version used in development)
- pip
- Git
- Kaggle API credentials (if using download_kaggle.py / kagglehub)

## Setup

### 1) Clone

```bash
git clone <repository-url>
cd wildires_in_the_states
```

### 2) Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

## 4) Run locally (live dev server)

```bash
myst start
```

Then open the local URL shown in terminal (commonly http://localhost:3000).

## 5) Build static HTML

```bash
myst build --html
```

Output is written to `_build/`.

## Git workflow notes

Ignored directories/files (see `.gitignore`):

- `_build/`
- `output/`
- `yearly_pie_charts/`
- other generated artifacts

This keeps commits clean and focused on source files.

## Troubleshooting

- **ModuleNotFoundError**: activate your venv and reinstall requirements.
- **Notebook execution fails**: run notebook cells top-to-bottom in Jupyter first.
- **Dataset path issues**: verify the SQLite path in project.ipynb.
- **Kernel path errors**: reselect kernel in Jupyter and save notebook metadata.

### Clean rebuild

```bash
rm -rf _build
myst build --html
```

## Core dependencies

- `mystmd`
- `pandas`
- `matplotlib`
- `scipy`
- `scikit-learn`
- `kagglehub`
- `jupyterlab`
- `ipywidgets`

## License

Dataset is U.S. government/public-domain source data (per dataset documentation).
Code in this repository is released under the MIT License.