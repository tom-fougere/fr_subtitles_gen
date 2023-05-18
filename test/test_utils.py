import unittest
from src.utils import *


class TestFunctions(unittest.TestCase):
    def test_is_file(self):
        self.assertTrue(is_file('test/english_subtitles.srt'))
        self.assertFalse(is_file("test/"))

    def test_is_dir(self):
        self.assertFalse(is_dir('test/english_subtitles.srt'))
        self.assertTrue(is_dir("test/"))

    def test_list_files_in_dir(self):
        files = list_files_in_dir("test/")
        self.assertEqual(len(files), 1)

    def test_get_files(self):
        self.assertEqual(len(get_files('test/english_subtitles.srt')), 1)
        self.assertEqual(len(get_files("test/")), 1)

    def test_get_dir_structure(self):
        dir_in, dir_out, files = get_dir_structure(path=None)
        self.assertEqual(dir_in, 'd01_data/english')
        self.assertEqual(dir_out, 'd01_data/french')
        # self.assertEqual(len(files))

        dir_in, dir_out, files = get_dir_structure(path='test')
        self.assertEqual(dir_in, 'test')
        self.assertEqual(dir_out, 'test')
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0], "english_subtitles.srt")

        dir_in, dir_out, files = get_dir_structure(path='test/english_subtitles.srt')
        self.assertEqual(dir_in, 'test')
        self.assertEqual(dir_out, 'test')
        self.assertEqual(len(files), 1)
        self.assertEqual(files[0], "english_subtitles.srt")


if __name__ == '__main__':
    unittest.main()
