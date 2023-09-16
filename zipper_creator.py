import zipfile
import pathlib


def make_archive(filepaths, dest_dir):

    """
    This fucnction convert file(s) to zip format
    :param filepaths: directory for the origin file(s)
    :param dest_dir: destination folder
    :return:
    """

    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


if __name__ == '__main__':
    make_archive(filepaths=['a.txt', 'b.txt'], dest_dir='new')
