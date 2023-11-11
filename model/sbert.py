from transformers import AutoTokenizer, AutoModel
from pathlib import Path


tokenize_path = Path('nlp/tokenize')

if not (tokenize_path / 'vocab.txt').exists():
    AutoTokenizer.from_pretrained('ai-forever/sbert_large_nlu_ru').save_pretrained(str(tokenize_path))
tokenizer_sbert = AutoTokenizer.from_pretrained(str(tokenize_path)) 

model_path = Path('nlp\model')

if not (model_path / 'model.safetensors').exists():
    AutoModel.from_pretrained('ai-forever/sbert_large_nlu_ru').save_pretrained(str(model_path))
model_sbert = AutoModel.from_pretrained(str(model_path)) 
