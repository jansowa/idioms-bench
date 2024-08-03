import torch
from transformers import pipeline, AutoModelForCausalLM


def load_pipe(model, tokenizer):
    return pipeline(model=model, tokenizer=tokenizer, task='text-generation', return_full_text=False)


def load_model(model_name):
    return AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
        revision="main"
    )
