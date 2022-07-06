# Software Engineering for Data Scientists in Python

Three software engineering concepts that help Data Scientists or Developer save time, collaborate, and write better code are 
- Modularity
- Documentation
- Automated Testing

In Python, we use PEP 8 conventions as Python style guide and we can use `pycodestyle`'s `StyleGuide` class to check multiple files for PEP 8 compliance.

Normally, we can import functions in submodule in package by
- For package' key functionality, it skip the file' name to directly and easily accessible functions through importing package's name
  - `from .utils import plot_counter, sum_counters` in `__init__.py`
  - `import my_package` in `my_script.py`
- For less central functionality
  - `import my_package.utils` in `my_script.py`

With `requirements.txt` file, it can help your package be more portable by allowing your users to easily recreate its intended environments.
- `pip install -r requirements.txt`

In order to make your package installable by `pip` you need to create a `setup.py` file.
