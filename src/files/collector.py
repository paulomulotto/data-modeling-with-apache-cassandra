
import os
import glob


class FileCollector:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def collect_files(self):
        file_path_list = []
        for root, dirs, files in os.walk(self.root_dir):
            file_path_list.extend(glob.glob(os.path.join(root, '*')))
        return file_path_list
