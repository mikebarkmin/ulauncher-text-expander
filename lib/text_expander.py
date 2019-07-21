""" Text Expander module """

import os
import errno
import glob2


class TextExpander():
    """ Class that manages the Text Expansions Snippets """

    def __init__(self, expansions_dir):
        """ Constructor method"""
        self.expansions_dir = expansions_dir
        self.create_default_expansions_dir()

    def find(self, query=None):
        """ Llooks for a cheat sheet, optionally filtered by the query argument """

        files = glob2.glob('%s/**/*.txt' % self.expansions_dir)
        result = []
        for file_path in files:
            filename = os.path.basename(file_path)
            filename_without_ext = os.path.splitext(filename)[0].replace(
                '_', ' ').replace('-', ' ').title()

            if not os.path.isfile(file_path):
                continue

            if query and query.lower() not in filename.lower():
                continue

            result.append({
                'path': file_path,
                'name': filename,
                'normalized_name': filename_without_ext
            })

        result = sorted(result, key=lambda k: k['normalized_name'])

        return result

    def create_default_expansions_dir(self):
        """ creates the cheats dir if it does not exist """
        try:
            os.makedirs(self.expansions_dir)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(
                    self.expansions_dir):
                pass
            else:
                raise

    def set_expansions_dir(self, expansions_dir):
        """ Sets the expansions dir, overriding the default one """
        self.expansions_dir = expansions_dir
