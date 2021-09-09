# coding: utf-8
import subprocess
TEST_MODULES = ['src/enum_extend']
# kwhelp.method
def get_modules():
    global TEST_MODULES
    result = ''
    if len(TEST_MODULES) > 0:
        result = ' --cov=' + ' --cov='.join(TEST_MODULES)
    return result
def main():
    cov_mod = get_modules()
    # see: https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can
    cmd_str = "python -m pytest{0} --cov-report=html".format(cov_mod)
    res = subprocess.run(cmd_str.split(' '))
    if res and res.returncode != 0:
        print(res)
    res = subprocess.run(['coverage', 'report'])
    if res and res.returncode != 0:
        print(res)
    # print(cmd_str)

if __name__ == '__main__':
    main()
