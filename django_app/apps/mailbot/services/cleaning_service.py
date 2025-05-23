import re
import string
from bs4 import BeautifulSoup
from nltk import download
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


download('rslp')
download('punkt')
download('punkt_tab')
download('stopwords')
        
        
class CleaningService:
    
    def __init__(self, body: str):
        self.body = body
        
    def to_lower(self):
        self.body = self.body.lower()
        return self

    def remove_html(self):
        self.body = BeautifulSoup(self.body, "html.parser").get_text(separator=" ")
        return self
    
    def remove_emails(self):
        self.body = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL_REMOVIDO]', self.body)
        return self

    def remove_phones(self):
        self.body = re.sub(r'\b(?:\+?55\s?)?\(?\d{2}\)?\s?\d{4,5}-?\d{4}\b', '[TELEFONE_REMOVIDO]', self.body)
        return self
    
    def remove_cpf(self):
        self.body = re.sub(r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b', '[CPF_REMOVIDO]', self.body)
        return self

    def remove_cnpj(self):
        self.body = re.sub(r'\b\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}\b', '[CNPJ_REMOVIDO]', self.body)
        return self
    
    def remove_credit_card(self):
        self.body = re.sub(r'\b(?:\d[ -]*?){13,16}\b', '[CARTAO_REMOVIDO]', self.body)
        return self

    def remove_punctuation(self):
        self.body = self.body.translate(str.maketrans('', '', string.punctuation))
        return self
    
    def normalize_spaces(self):
        self.body = re.sub(r'[\n\r\t]+', ' ', self.body)
        self.body = re.sub(r'\s+', ' ', self.body).strip()
        return self
    
    def remove_stopwords(self):
        stop_words = set(stopwords.words('portuguese'))
        tokens = word_tokenize(self.body, language='portuguese')
        tokens_limpos = [palavra for palavra in tokens if palavra not in stop_words]
        self.body = ' '.join(tokens_limpos)
        return self

    def stemming(self):
        stemmer = RSLPStemmer()
        tokens = word_tokenize(self.body, language='portuguese')
        tokens_stem = [stemmer.stem(token) for token in tokens]
        self.body = ' '.join(tokens_stem)
        return self
    
    def get(self):
        return self.body
