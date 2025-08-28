# Python Library Cookiecutter Template

A modern, opinionated Cookiecutter template for Python libraries that follows current best practices and includes everything you need to get started with a professional Python project.

## 🚀 Features

This template provides a complete Python library setup with:

### 📦 Modern Dependency Management
- **[uv](https://docs.astral.sh/uv/)** - Ultra-fast Python package installer and resolver
- **pyproject.toml** configuration following PEP 621 standards
- Automatic virtual environment management

### 🧪 Testing & Quality Assurance
- **[pytest](https://pytest.org/)** - Modern testing framework with comprehensive plugins:
  - `pytest-cov` - Code coverage reporting
  - `pytest-html` - HTML test reports
  - `pytest-mock` - Mock fixtures
  - `pytest-faker` - Fake data generation
  - `pytest-datadir` - Test data directory management
  - `pytest-print` - Enhanced print debugging
- **[ruff](https://github.com/astral-sh/ruff)** - Extremely fast Python linter and formatter
- **[ty](https://github.com/brownben/ty)** - Type checking with mypy

### 📊 Optional Analytics Features
- **[Jupyter](https://jupyter.org/)** - Interactive notebook environment for data exploration
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis library
- **[Matplotlib](https://matplotlib.org/)** - Comprehensive plotting library
- **[Seaborn](https://seaborn.pydata.org/)** - Statistical data visualization
- **[Plotly](https://plotly.com/python/)** - Interactive plotting library
- **IPykernel** - Jupyter kernel support for Python

### 🏗️ Build System
- **Hatchling** build backend for modern Python packaging
- **Makefile** with common development tasks
- Automated clean-up commands for build artifacts

### 📁 Project Structure
The template generates a well-organized project structure:

```
your-project/
├── src/
│   └── your_package/
│       ├── __init__.py
│       ├── app.py          # Example application code
│       └── main.py         # Entry point
├── tests/
│   └── your_package/
│       ├── conftest.py     # Test configuration
│       ├── test_app.py     # Application tests
│       └── test_main.py    # Main module tests
├── notebooks/              # Analytics notebooks (if enabled)
│   └── analysis_example.ipynb
├── pyproject.toml          # Project configuration
├── Makefile               # Development commands
├── conftest.py            # Root test configuration
└── README.md              # Project documentation
```

## 🎯 Template Variables

When you run the cookiecutter, you'll be prompted for the following variables:

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `full_name` | Your full name | "Developer" | "John Doe" |
| `email` | Your email address | "test@test.com" | "john@example.com" |
| `project_name` | Human-readable project name | "Python Boilerplate" | "My Awesome Library" |
| `project_slug` | URL/package-friendly name | Auto-generated | "my-awesome-library" |
| `pkg_name` | Python package name | Auto-generated | "my_awesome_library" |
| `version` | Initial version | "0.1.0" | "0.1.0" |
| `python_version` | Minimum Python version | "3.13" | "3.13" |
| `year` | Copyright year | "2025" | "2025" |
| `use_analytics` | Include analytics dependencies | "y" or "n" | "y" |

## 🛠️ Getting Started

### Prerequisites

1. **Python 3.13+** - [Download Python](https://www.python.org/downloads/)
2. **uv** - Install from [official docs](https://docs.astral.sh/uv/getting-started/installation/)
3. **Cookiecutter** - Install with:
   ```bash
   pip install cookiecutter
   # or
   uv tool install cookiecutter
   ```

### Creating a New Project

1. Generate your project:
   ```bash
   cookiecutter https://github.com/amitsk/cookiecutter-python-library
   ```

2. Navigate to your new project:
   ```bash
   cd your-project-name
   ```

3. Set up the development environment:
   ```bash
   make install
   ```

4. Run the example code:
   ```bash
   uv run python src/your_package/main.py
   ```

## 🔧 Development Workflow

The template includes a comprehensive Makefile with common development tasks:

```bash
# Install dependencies and set up development environment
make install

# Run the complete build pipeline (install, lint, type check, test)
make build

# Run tests with coverage
make test

# Run linting
make lint

# Run type checking
make type_check

# Clean up build artifacts
make clean

# Format code
make format

# Analytics commands (if analytics is enabled)
make install-analytics  # Install analytics dependencies
make jupyter            # Start Jupyter Lab
make notebook          # Start Jupyter Notebook

# View all available commands
make help
```

## 📊 Using Analytics Features

If you chose to include analytics dependencies (`use_analytics: y`), your project will include powerful data analysis and visualization capabilities:

### 🚀 Quick Start with Analytics

1. **Install analytics dependencies:**
   ```bash
   make install-analytics
   ```

2. **Start Jupyter Lab:**
   ```bash
   make jupyter
   ```

3. **Open the example notebook:**
   Navigate to `notebooks/analysis_example.ipynb` to see a demonstration of:
   - Using your package functions with pandas DataFrames
   - Creating static visualizations with matplotlib and seaborn
   - Building interactive plots with plotly
   - Performing basic data analysis

### 📝 Example Analytics Usage

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from your_package.app import scrabble_score

# Create sample data
words = ['python', 'data', 'analysis', 'jupyter']
scores = [scrabble_score(word) for word in words]
df = pd.DataFrame({'word': words, 'score': scores})

# Static visualization
sns.barplot(data=df, x='score', y='word')
plt.title('Scrabble Scores')
plt.show()

# Interactive visualization
fig = px.bar(df, x='word', y='score', title='Interactive Scrabble Scores')
fig.show()
```

### 🎯 Analytics Dependencies Included

- **Jupyter**: Complete notebook environment with JupyterLab interface
- **Pandas**: DataFrame operations, data cleaning, and analysis
- **Matplotlib**: Publication-quality static plots and figures
- **Seaborn**: Beautiful statistical visualizations with minimal code
- **Plotly**: Interactive plots that work in notebooks and web apps
- **IPykernel**: Python kernel for Jupyter with proper environment integration

## 📋 Example Application

The template includes a sample Scrabble score calculator to demonstrate:
- Modern Python package structure
- Type hints and annotations
- Usage of third-party dependencies (`more-itertools`, `loguru`)
- Comprehensive test coverage
- Documentation best practices

## 🎨 Code Quality Features

- **Ruff configuration** with comprehensive rule sets including:
  - Pyflakes (F) - Logic errors
  - pycodestyle (E, W) - Style enforcement
  - pep8-naming (N) - Naming conventions
  - pyupgrade (UP) - Modern Python syntax
  - flake8-annotations (ANN) - Type hints
  - flake8-bandit (S) - Security checks
  - And many more...

- **Pytest configuration** with sensible defaults
- **Type checking** with ty/mypy integration
- **Coverage reporting** with configurable thresholds

## 🤝 Contributing

This template is designed to be a starting point for Python libraries. Feel free to:
- Customize the generated project to fit your needs
- Add additional dependencies or tools
- Modify the project structure
- Update the example code

## 📄 License

Projects generated from this template are created with MIT license by default. You can modify this in the generated `pyproject.toml` file.

