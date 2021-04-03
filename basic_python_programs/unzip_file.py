import zipfile
import sys


def unzip_files(path_, out_):
    local_zip = path_
    if local_zip.endswith('zip'):
        zip_ref = zipfile.ZipFile(local_zip, 'r')
        print(f'Extracting zip {path_} to path  {out_}')
        zip_ref.extractall(out_)
        zip_ref.close()
    else:
        print('Give path')


if __name__ == '__main__':
    path = str(sys.argv[1]).strip()
    out_folder = str(sys.argv[2]).strip()
    unzip_files(path, out_folder)
