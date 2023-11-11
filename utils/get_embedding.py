from typing import List
import torch
from utils.mean_pooling import mean_pooling
from transformers import PreTrainedTokenizer, PreTrainedTokenizerFast


def get_embedding(text: str | List[str], tokenizer: PreTrainedTokenizer | PreTrainedTokenizerFast, model) -> torch.Tensor:
    encoded_input = tokenizer(text, padding=True, truncation=True, max_length=16, return_tensors='pt')

    with torch.no_grad():
        model_output = model(**encoded_input)

    return mean_pooling(model_output, encoded_input['attention_mask'])
