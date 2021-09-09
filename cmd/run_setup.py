# coding: utf-8
import subprocess

def main():
    cmd_str = 'python setup.py sdist bdist_wheel'
    res = subprocess.run(cmd_str.split(' '))
    # print(res.stdout)
    cmd_str = 'twine check dist/*'
    res = subprocess.run(cmd_str.split(' '))
    # print(res.stdout)

if __name__ == '__main__':
    main()
