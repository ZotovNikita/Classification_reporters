from typing import Dict
import torch
from utils.cos_similarity import cos_similarity
from utils.lower_case import lower_case
from utils.get_embedding import get_embedding


def find_sentences(query: str, id2text: Dict[int, str], id2vec: torch.Tensor, tokenizer, model) -> str:
    query_emb = get_embedding(lower_case(query), tokenizer, model)
    return id2text[torch.argmax(cos_similarity(query_emb, id2vec)).item()]
