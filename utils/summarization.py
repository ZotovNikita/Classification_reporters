from transformers import PreTrainedTokenizer, PreTrainedTokenizerFast
from transformers import T5ForConditionalGeneration


def summarization(text: str, tokenizer_sum: PreTrainedTokenizer | PreTrainedTokenizerFast, model_sum: T5ForConditionalGeneration):
    input_ids = tokenizer_sum(
        [text],
        max_length=300,
        add_special_tokens=True,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )["input_ids"]

    output_ids = model_sum.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    return tokenizer_sum.decode(output_ids, skip_special_tokens=True)
