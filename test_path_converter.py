import re
import pyperclip
import argparse

# Create argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--module", action="store_true", help="Run tests from module with all params.")
ap.add_argument("-a", "--all_tests", action="store_true", help="Run all tests from test file.")
ap.add_argument("-i", "--integration_test", help="Run integration test(s). Last 3 digits of port needs to by supplied!", metavar="INT")
ap.add_argument("-n", "--threads_number", help="Number of CPUs to run the tests. 0 means auto.", metavar="INT")

# Retrieve arguments
args = vars(ap.parse_args())


###
# test_string = "API Tests / simple_ui.simple_ui.tests.api.users.test_api_security.test_delete_last_admin[param with spaces] (from pytest)"
# integration test:
# pytest -c pytest.ini --rootdir=. --testenv env_integration --ssh-addresses 10.122.58.49:13164 --controller-url=https://10.122.58.49:12164/ --controller-username=cml2 --controller-password=cml2cml2 --mock-licensing tests/integration/test_groups.py
###


def main():
    jenkins_path = pyperclip.paste()
    # jenkins_path = test_string
    test_path = jenkins_path.split(".")
    test_module = test_path.pop(-1)
    test_path = f"{'/'.join(test_path)}.py"
    if "API" in test_path:
        test_path = test_path.replace("API Tests / ", "")
    if "Int" in test_path:
        test_path = test_path.replace("Int Tests / ", "")
    if "Unit" in test_path:
        test_path = test_path.replace("Unit Tests / ", "")
    if "Smoke" in test_path:
        test_path = test_path.replace("Smoke Tests / ", "")
    test_list = list(re.findall(r"([a-z_0-9A-Z]+)(\[.+\])?( \(from .+\))?(\n)*", test_module)[0])
    test_param = ""
    for item in test_list:
        if not item:
            test_list.remove(item)
        if "from pytest" in item:
            test_list.remove(item)
        if "[" in item:
            test_list.remove(item)
            if not (args["module"] or args["all_tests"]):
                test_param = item.replace(" ", "\\ ")
    test_module = f"::{test_list[0]}" if not args["all_tests"] else ""

    if int(args["threads_number"]) == 0:
        pytest = "pytest -n auto "
    elif args["threads_number"]:
        pytest = f"pytest -n {int(args['threads_number'])} "
    else:
        pytest = "pytest "

    if args["integration_test"]:
        pytest = f"{pytest}-c pytest.ini --rootdir=. --testenv env_integration --ssh-addresses 10.122.58.49:13{args['integration_test']} --controller-url=https://10.122.58.49:12{args['integration_test']}/ --controller-username=cml2 --controller-password=cml2cml2 --mock-licensing "

    test_cmd = f"{pytest}{test_path}{test_module}{test_param}"
    print()
    print(" Command below was successfully copied to clipboard. ".center(120, "="))
    print(test_cmd)
    print()
    pyperclip.copy(test_cmd)


if __name__ == "__main__":
    main()
