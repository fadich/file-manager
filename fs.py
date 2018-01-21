import os


class Item(object):
    _path = '.'

    def __init__(self, path='.'):
        self._path = path

    def get_path(self):
        return self._path

    def get_name(self):
        return self._path.split('/')[-1]


class Dir(Item):
    def __init__(self, path='.'):
        self._items = list()
        super(Dir, self).__init__(path)

    def list_dir(self):
        try:
            items = os.listdir(self._path)
        except WindowsError:
            return []

        for path in items:
            full_path = self._path + '/' + path
            if os.path.isdir(full_path):
                self._items.append(Dir(full_path))
            else:
                self._items.append(File(full_path))

        return self._items

    @staticmethod
    def is_dir(path):
        return os.path.isdir(path)


class File(Item):
    def __init__(self, path='.'):
        super(File, self).__init__(path)
