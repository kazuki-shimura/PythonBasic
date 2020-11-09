# import tarfile
#
# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('tar')
#
#
#
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     # tr.extractall(path='test_tar')
#     with tr.extractfile('test_dtar/tar/sub_dir/sub_test.txt') as f:
#         print(f.read())


import zipfile

with zipfile.ZipFile('test.zip', 'w') as z:
    z.write('test_dir')
    z.write('test_dir/test.txt')

