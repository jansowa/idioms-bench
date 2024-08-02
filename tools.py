from model_tools import load_pipe, load_model
from settings import EVALUATING_METAMODEL_PROMPT
from transformers import AutoTokenizer
from prompts import (get_prompt_template_v1, get_prompt_template_v2, get_prompt_template_v3, get_prompt_template_v4,
                     get_prompt_template_v5, get_prompt_template_v6)
import time
import torch
import ray
import json


BATCH_SIZE = 1


def generate_evaluating_metamodel_prompt(model_response, reference_explanation, reference_sentiment, reference_idioms):
    def check_empty(value):
        if value is None or value == "" or value != value:  # value != value sprawdza NaN
            return "BRAK"
        return value

    model_response = check_empty(model_response)
    reference_explanation = check_empty(reference_explanation)
    reference_sentiment = check_empty(reference_sentiment)

    if reference_idioms not in [None, "", "BRAK"] and reference_idioms == reference_idioms:
        reference_idioms = format_idioms(reference_idioms)
    else:
        reference_idioms = "BRAK"

    return EVALUATING_METAMODEL_PROMPT.format(model_response=model_response, reference_explanation=reference_explanation, reference_sentiment=reference_sentiment, reference_idioms=reference_idioms)


def generate_answers_batch(questions, tokenizer, pipe, llm_params, prompt_ver=1):
    prompts = get_generate_answers_prompts(questions, tokenizer, prompt_ver=prompt_ver)

    outputs = pipe(
        prompts,
        **llm_params
    )

    clean_outputs = [output[0]['generated_text'] for output in outputs]
    print(clean_outputs)
    return clean_outputs


def get_generate_answers_prompts(questions, tokenizer, prompt_ver=1):
    chats = [get_prompt_template(q, prompt_ver=prompt_ver) for q in questions]
    prompts = [tokenizer.apply_chat_template(chat, tokenize=False) for chat in chats]
    return prompts


def get_prompt_template(q, prompt_ver=1):
    template_versions = {
        1: get_prompt_template_v1(q),
        2: get_prompt_template_v2(q),
        3: get_prompt_template_v3(q),
        4: get_prompt_template_v4(q),
        5: get_prompt_template_v5(q),
        6: get_prompt_template_v6(q)
    }
    return template_versions[prompt_ver]


@ray.remote(max_calls=1)
def calculate_for_model(model_name, df, llm_params, batch_size=BATCH_SIZE, prompt_ver=1):
    print(f"Przetwarzanie modelu: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    with torch.no_grad():
        model = load_model(model_name)
        pipe = load_pipe(model, tokenizer)

        answer_column = f'answer_{model_name.split("/")[-1]}'

        start_time = time.time()

        answers = []
        for i in range(0, len(df), batch_size):
            batch = df['Opinia'].iloc[i:i + batch_size].tolist()
            batch_answers = generate_answers_batch(batch, tokenizer, pipe, llm_params, prompt_ver=prompt_ver)
            answers.extend(batch_answers)

            print(f"Przetworzono batch {i // batch_size + 1}/{(len(df) - 1) // batch_size + 1}")

        df.loc[:len(answers) - 1, answer_column] = answers

        end_time = time.time()
        print(f"Czas przetwarzania dla modelu {model_name}: {end_time - start_time:.2f} sekund")
        return df

def format_idioms(reference_idioms):
    idioms_dict = json.loads(reference_idioms)
    formatted_list = []
    for index, (idiom, definition) in enumerate(idioms_dict.items(), start=1):
        formatted_list.append(f'{index}. "{idiom}" - {definition}')
    return '\n'.join(formatted_list)