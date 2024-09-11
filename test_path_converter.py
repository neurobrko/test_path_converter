import re
import pyperclip


def main():
    jenkins_path = pyperclip.paste().split(".")
    test_name = jenkins_path.pop(-1)
    test_name = re.sub(r"(\[.+\])?( \(from pytest\))?(\n)*", "", test_name)
    test_cmd = f"pytest {'/'.join(jenkins_path)}.py::{test_name}"
    print()
    print(" Command below was successfully copied to clipboard. ".center(120, "="))
    print(test_cmd)
    print()
    pyperclip.copy(test_cmd)


if __name__ == "__main__":
    main()
