# Path Converter for pytest paths from Jenkins
Author: Marek Paulik\
email: [marek.paulik@pantheon.tech](mailto:marek.paulik@pantheon.tech)

**Script for quickly converting test description copied from Jenkins to valid path attached to *pytest* command inside clipboard.**
## Usage
Copy path from Jenkins to clipboard. You can copy only the path, or with brackets, even with '(from pytest)'. The script will take care of new lines, if you accidentally copied them.
run *test_path_converter.py*. Script will convert clipboard content to valid pytest command.
### Example:
**Clipboard content:** (notice new lines at the end)
```
core.simple_core.tests.test_central_admin_version.test_version_load1[config0] (from pytest)


```
```
>>> test_path_converter.py
```
**Clipboard content after running the script:**
```
pytest core/simple_core/tests/test_central_admin_version.py::test_version_load1
```
## Dependecies
* pyperclip

## Installation
Either run the script from Poetry environment or install pyperclip system wide.
Make an alias or add it to $PATH and you are good to go.