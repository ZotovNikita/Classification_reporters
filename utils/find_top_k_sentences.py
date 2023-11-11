from typing import Dict, List
import torch
from utils.cos_similarity import cos_similarity
from utils.lower_case import lower_case
from utils.get_embedding import get_embedding


def find_top_k_sentences(query: str, id2text: Dict[int, str], id2vec: torch.Tensor, tokenizer, model, top_k: int = 3) -> List[str]:
    query_emb = get_embedding(lower_case(query), tokenizer, model)
    idxs = torch.topk(cos_similarity(query_emb, id2vec), top_k).indices[0]
    return [id2text[id.item()] for id in idxs]
