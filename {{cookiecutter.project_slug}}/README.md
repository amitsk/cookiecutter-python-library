# {{cookiecutter.project_slug}}

![Run Tests and Lint](https://github.com/{{cookiecutter.project_slug}}/workflows/Run%20Tests%20and%20Lint/badge.svg)

- uv for dependency management
- Pytest for tests
- ruff for formatting and linting
- ty for type checking
{% if cookiecutter.use_analytics == "y" -%}
- Jupyter, Pandas, Matplotlib, Seaborn, Plotly for data analytics
{% endif %}

## Building

- Install uv https://docs.astral.sh/uv/getting-started/installation/
- Clone from GitHub
- Build - Install, test, lint `make build`. This step pulls the python version defined in pyproject.toml
- Tests can be run with `make test`

{% if cookiecutter.use_analytics == "y" -%}
## Analytics Features

This project includes optional analytics dependencies for data analysis and visualization:

### Dependencies Included
- **Jupyter**: Interactive notebook environment
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Static plotting
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive visualizations
- **IPykernel**: Jupyter kernel support

### Getting Started with Analytics

1. Install analytics dependencies:
   ```bash
   make install-analytics
   ```

2. Start Jupyter Lab:
   ```bash
   make jupyter
   ```

3. Or start Jupyter Notebook:
   ```bash
   make notebook
   ```

4. Open the example analysis notebook:
   ```
   notebooks/analysis_example.ipynb
   ```

### Manual Installation
You can also install the analytics dependencies manually:
```bash
uv sync --extra analytics
```

### Using Analytics Dependencies
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from {{cookiecutter.pkg_name}}.app import scrabble_score

# Your analytics code here
```
{% endif %}
