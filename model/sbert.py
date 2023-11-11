from transformers import AutoTokenizer, AutoModel
from pathlib import Path


tokenizer = AutoTokenizer.from_pretrained("nlp/tokenizer")

model_path = Path('nlp\model')

if not (model_path / 'model.safetensors').exists():
    AutoModel.from_pretrained('ai-forever/sbert_large_nlu_ru').save_pretrained(str(model_path))
model_sbert = AutoModel.from_pretrained(str(model_path)) 
