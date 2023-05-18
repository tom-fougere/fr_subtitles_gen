import unittest
import os
from src.rw_srt_file import *


class TestFunctions(unittest.TestCase):
    def test_read_srt(self):
        df = read_srt("test/english_subtitles.srt")

        self.assertEqual(len(df), 2)
        self.assertEqual(len(df.keys()), 4)

        for key, val in COLUMNS_NAME.items():
            self.assertTrue(val in df.keys())

    def test_write_srt_file(self):
        new_file_path = 'test/new_file.srt'
        df = read_srt("test/english_subtitles.srt")
        write_srt_file(
            df=df,
            column_name_sentence=COLUMNS_NAME['sentence'],
            output_file_path=new_file_path
        )

        df_translated = read_srt(new_file_path)
        self.assertTrue(df.equals(df_translated))

        os.remove(new_file_path)


if __name__ == '__main__':
    unittest.main()
