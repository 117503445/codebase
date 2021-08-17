from htutil import file
from pathlib import Path
import shutil
from tqdm import tqdm


dir_source = Path('exploitdb')
dir_dest = Path('exploitdb-python')


def main():
    if not dir_dest.exists():
        dir_dest.mkdir()
    else:
        print('dest already exists')
        return

    for f in tqdm(list(dir_source.glob('**/*.py'))):
        relate = f.relative_to(dir_source)
        file_dest = dir_dest / relate
        file.create_dir_if_not_exist(file_dest.parent)
        shutil.copy(dir_source/relate, file_dest)

if __name__ == '__main__':
    main()
