from transformers import pipeline
from tqdm import tqdm
from src.rw_srt_file import read_srt, COLUMNS_NAME


class SRTranslator:
    def __init__(self, target_language='fr', max_length=512):
        self.target_language = target_language
        self.max_length = max_length
        self.default_model = True
        self.model_name = f"Helsinki-NLP/opus-mt-en-{self.target_language}"
        self.model = pipeline("translation", model=self.model_name)
        self.tokenizer = None

    def set_model(self, model, tokenizer, model_name=None):
        self.model_name = "Custom" if model_name is None else model_name
        self.model = model
        self.tokenizer = tokenizer
        self.default_model = False

    def translate_sentence(self, sentence):

        # Simple pre-processing
        sentence = f'{sentence.strip()}'

        if self.default_model:
            # Translate the sentence
            translated_sentence = self.model(sentence, max_length=self.max_length)[0]['translation_text']

        else:
            # Add start and end of sentence tokens and tokenize the input
            inputs = self.tokenizer(sentence, return_tensors='pt')

            # Translate the input and decode the output
            outputs = self.model.generate(**inputs)
            translated_sentence = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return translated_sentence

    def translate_df(self, df, column_to_translate, column_translation=None):

        # Name of the new column
        column_name = column_to_translate + '_translated' if column_translation is None else column_translation

        # Apply the translation to each sentence in the DataFrame
        tqdm.pandas()
        df[column_name] = df[column_to_translate].progress_apply(
            lambda x: self.translate_sentence(x))

    def translate_file(self, srt_file_path):

        # Read file
        srt_df = read_srt(srt_file_path)

        # Translate
        self.translate_df(
            df=srt_df,
            column_to_translate=COLUMNS_NAME['sentence'],
            column_translation=None,
        )

        return srt_df
