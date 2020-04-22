import os
import tempfile
import json
import argparse


def add_val(storage_path, key, val):
    ex = os.path.exists(storage_path)
    if not ex:
        with open(storage_path, 'w') as f:
            dic = {key: [val]}
            json.dump(dic, f, indent = 4)
    else:
        with open(storage_path, 'r') as f:
            dic = json.load(f)
        if key in dic:
            dic[key].append(val)
        else:
            dic[key] = [val]
        with open(storage_path, 'w') as f:
            json.dump(dic, f, indent = 4)


def print_val(storage_path, key):
    ex = os.path.exists(storage_path)
    if not ex:
        print()
    else:
        with open(storage_path, 'r') as f:
            dic = json.load(f)
            if dic.get(key):
                print(*dic.get(key), sep=', ')
            else:
                print()


def main():
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="ключ")
    parser.add_argument("--val", help="значение")
    args = parser.parse_args()
    if args.val:
        add_val(storage_path, args.key, args.val)
    else:
        print_val(storage_path, args.key)


if __name__ == '__main__':
    main()
