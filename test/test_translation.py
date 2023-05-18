import unittest

import pandas as pd

from src.translation import *


class SRTranslationTest(unittest.TestCase):
    def test_init(self):
        srt_translator = SRTranslator()
        self.assertEqual(srt_translator.target_language, "fr")
        self.assertEqual(srt_translator.max_length, 512)
        self.assertEqual(srt_translator.default_model, True)
        self.assertEqual(srt_translator.model_name, "Helsinki-NLP/opus-mt-en-fr")
        self.assertEqual(srt_translator.tokenizer, None)

    def test_set_model(self):
        srt_translator = SRTranslator()
        srt_translator.set_model(model="test_model", tokenizer="test_tokenizer")

        self.assertEqual(srt_translator.default_model, False)
        self.assertEqual(srt_translator.model_name, "Custom")
        self.assertEqual(srt_translator.model, "test_model")
        self.assertEqual(srt_translator.tokenizer, "test_tokenizer")

    def test_translate_sentence(self):
        srt_translator = SRTranslator()
        new_sentence = srt_translator.translate_sentence(sentence="Hello world")
        self.assertEqual(new_sentence, "Bonjour monde")

    def test_translate_df(self):
        df = pd.DataFrame.from_dict({
            'sentence': ['Hello world']
        })

        srt_translator = SRTranslator()
        srt_translator.translate_df(
            df=df,
            column_to_translate='sentence',
            column_translation=None,
        )
        self.assertTrue('sentence_translated' in df.keys())
        self.assertEqual(df['sentence_translated'][0], 'Bonjour monde')

        srt_translator.translate_df(
            df=df,
            column_to_translate='sentence',
            column_translation='translation',
        )
        self.assertTrue('translation' in df.keys())
        self.assertEqual(df['translation'][0], 'Bonjour monde')

    def test_translate_file(self):
        srt_translator = SRTranslator()
        df = srt_translator.translate_file("test/english_subtitles.srt")

        self.assertEqual(len(df), 2)
        self.assertEqual(df['sentence_translated'][0], "Bonjour monde")


if __name__ == '__main__':
    unittest.main()
