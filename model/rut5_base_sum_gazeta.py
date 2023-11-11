from transformers import AutoTokenizer, AutoModel
from pathlib import Path
from transformers import T5ForConditionalGeneration


tokenize_path = Path('nlp/tokenize_sum')

if not (tokenize_path / 'vocab.txt').exists():
    AutoTokenizer.from_pretrained('IlyaGusev/rut5_base_sum_gazeta').save_pretrained(str(tokenize_path))
tokenizer_sum = AutoTokenizer.from_pretrained(str(tokenize_path)) 

model_path = Path('nlp\model_sum')

if not (model_path / 'model_sum.safetensors').exists():
    T5ForConditionalGeneration.from_pretrained('IlyaGusev/rut5_base_sum_gazeta').save_pretrained(str(model_path))
model_sum = T5ForConditionalGeneration.from_pretrained(str(model_path))
