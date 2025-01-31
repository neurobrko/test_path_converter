# Path Converter for pytest paths from Jenkins
Author: Marek Paulik\
email: [marek.paulik@pantheon.tech](mailto:marek.paulik@pantheon.tech)

**Script for quickly converting test description copied from Jenkins to valid path attached to *pytest* command inside clipboard.**\
**DISCLAIMER: Some Unit tests have different path and will not work with this script.!**
## Usage
Copy path from Jenkins to clipboard. You can copy only the path, or with brackets, even with '(from pytest)' or with 'API tests / ' prefix. The script will take care of new lines, if you accidentally copied them.
run *test_path_converter.py*. Script will convert clipboard content to valid pytest command.\
If you copy whole line, but want to run complete test module without parameters, or even all tests in selected test file, you can specify that with command line arguments, which you can combine.\
**-m** Run the module without parametrization.\
**-a** Run all tests from a test file. (Overrides -m)\
**-i** When running integration test, use with last three digits of port as argument.\
**-n** Set number of CPUs to execute tests. 0 means auto.
### Example:
**API TEST**

**Clipboard content:** (notice new lines at the end)
```
API Tests / simple_ui.simple_ui.tests.api.users.test_api_CRUD.test_update_user[client_config0-admin-myself updating myself-admin] (from pytest)


```
**Clipboard content after running the script with -m argument:**
```
>>> test_path_converter.py -m
```
```
pytest simple_ui/simple_ui/tests/api/users/test_api_CRUD.py::test_update_user
```
**Clipboard content after running the script with -a argument:**
```
>>> test_path_converter.py -a
```
```
pytest simple_ui/simple_ui/tests/api/users/test_api_CRUD.py
```
**Clipboard content after running the script without arguments:**
```
>>> test_path_converter.py
```
```
pytest simple_ui/simple_ui/tests/api/users/test_api_CRUD.py::test_update_user[client_config0-admin-myself\ updating\ myself-admin]
```
**INTEGRATION TEST**

**Clipboard content:** (notice new lines at the end)
```
Int Tests / tests.integration.test_services.test_lld_sync_not_ready[some parameter here] (from pytest)
```
```
>>> test_path_converter.py -i 104
```
**Clipboard content after running the script:**
```
pytest -c pytest.ini --rootdir=. --testenv env_integration --ssh-addresses 10.122.58.49:13104 --controller-url=https://10.122.58.49:12104/ --controller-username=cml2 --controller-password=cml2cml2 --mock-licensing tests/integration/test_services.py::test_lld_sync_not_ready[some\ parameter\ here]
```
## Dependecies
* pyperclip

## Installation
Either run the script from Poetry environment or install pyperclip system wide.
Make an alias or add it to $PATH and you are good to go.