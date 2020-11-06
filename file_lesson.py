"""withステートメントについて
withステートメントを使用するとf.close()をしないで済むをする（抜けた時にクローズしてくれる）
ので基本的にはwithステートメントを使用する
f.close()はopenしたまんまだとメモリを食ってしまうので閉じるという意味で行う
"""
with open('test.txt', 'w') as f:
    f.write('Test {}'.format('fjsdajflksajfdlkjflkajfkljsalfkj'))




# readは現在地から何個読むか
# seekは何番目の位置に行くか
s = """\
AAAAA
BBBBB
CCCCC
DDDDD
EEEEE
"""

with open('test2.txt', 'r') as f:
    print(f.tell())
    print(f.read(18))
    f.seek(18)
    print(f.read(5))




# テンプレートの作成方法
import string

with open('design/email_template.txt') as f:
    t = string.Template(f.read())

contents = t.substitute(name='Mike', content='最近はどうですか？')
print(contents)




#csvファイルの作成
import csv
with open('csv/test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'a', 'Count': 1})
    writer.writerow({'Name': 'b', 'Count': 2})



#ファイルの操作について
import os

# print(os.path.exists('test.txt'))
# print(os.path.isfile('test.txt'))
# print(os.path.isdir('test.txt'))
# print(os.path.isdir('csv'))

# os.rename('test.txt', 'renamed.txt')
# os.symlink('renamed.txt', 'symlink.txt')

# os.mkdir('test_dir')
# os.rmdir('test_dir')


import pathlib
# pathlib.Path('empty.txt').touch()
# os.remove('empty.txt')
# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()


import glob
print(glob.glob('test_dir/test_dir2/*'))


import shutil
shutil.copy('test_dir/test_dir2/empty.txt',
            'test_dir/test_dir2/empty2.txt')
print(glob.glob('test_dir/test_dir2/*'))


