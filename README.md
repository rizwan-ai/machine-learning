# Machine Learning

This repository contains various machine learning algorithms implemented using Python. It provides examples of how to use popular ML libraries such as NumPy, pandas, scikit-learn, and others. The project is organized for ease of understanding, experimentation, and extension.

## Project Structure

- `ml-env/`: Python virtual environment for the project
- `data/`: Folder for storing datasets
- `notebooks/`: Jupyter notebooks demonstrating machine learning algorithms
- `src/`: Source code for machine learning models and utilities
- `README.md`: Project documentation

## Setup Instructions

Follow these steps to set up the environment and get started:

### 1. Prerequisites

Ensure you have the following installed on your system:

- **Homebrew 4.3.14** or higher (managed using [brew](https://brew.sh/))
- **Pyenv 2.4.3** or higher (managed using [brew pyenv](https://formulae.brew.sh/formula/pyenv))
- **Python 3.11.9** or higher (managed using [pyenv python](https://github.com/pyenv/pyenv))
- **Git 2.45.2** or higher (managed using [brew git](https://formulae.brew.sh/formula/git))

You can verify your installed versions with:

```bash
brew --version

pyenv --version
pyenv versions
pyenv version
brew info pyenv

python --version
brew info python

git --version
brew info git
```

### 2. Setting up the Environment
1. **Clone the repository:**

```bash
git clone https://github.com/your-username/machine-learning.git
cd machine-learning
```

2. **Create and activate the virtual environment:**

```bash
python -m venv ml-env
source ml-env/bin/activate  # For macOS/Linux
```

3. **Install the required Python libraries:**

Once the virtual environment is activated, install the dependencies:

```bash
pip install -r requirements.txt
```

4. **Verify the environment:**

Ensure the required packages are installed:

```bash
pip list
```