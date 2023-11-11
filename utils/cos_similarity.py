from sentence_transformers import util
import torch


def cos_similarity(first_embeddings: torch.Tensor, second_embeddings: torch.Tensor) -> torch.Tensor:
    return util.cos_sim(first_embeddings, second_embeddings)
