from htutil import file
import json
from pathlib import Path


def main():
    py_dict = {}
    p = Path('./exploitdb-python')
    for py_file in p.glob('**/*.py'):
        key = str(py_file.relative_to('.'))
        value = file.read_all_text(py_file)
        py_dict[key] = value
    file.write_pkl('exploitdb-python.pkl', py_dict)
    file.write_all_text('exploitdb-python.json', json.dumps(py_dict, indent=4))


if __name__ == '__main__':
    main()
