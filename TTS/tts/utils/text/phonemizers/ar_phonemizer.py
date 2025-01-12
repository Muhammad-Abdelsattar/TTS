from typing import Dict
from arabic_phonemizer import ArabicPhonemizer
from TTS.tts.utils.text.phonemizers.base import BasePhonemizer


class ArabicPhonemizer(BasePhonemizer):
    
    language = "ar"
    
    def __init__(self,**kwargs):  # pylint: disable=unused-argument
        super().__init__(self.language)
        self.phoenemizer = ArabicPhonemizer()

    @staticmethod
    def name():
        return "ar_phonemizer"

    def _phonemize(self, text: str,separator:str="") -> str:
        ph = phonemizer.phonemize(text)
        return ph

    def phonemize(self, text: str,separator:str="",language:str="ar") -> str:
        """
        Overrides the default method so that we don't do any pre or post processing.
        """
        return self._phonemize(text,separator)

    @staticmethod
    def supported_languages() -> Dict:
        return {"ar": "Arabic"}

    def version(self) -> str:
        return "0.0.1"

    def is_available(self) -> bool:
        return True

        
if __name__ == "__main__":
    text = "هذه تجربة لتحويل النص العربي إلى رموز صوتية."
    phonemizer = ArabicPhonemizer()
    print(phonemizer.supported_languages())
    print(phonemizer.version())
    print(phonemizer.language)
    print(phonemizer.name())
    print(phonemizer.is_available())
    print(phonemizer.phonemize(text))
