import warnings
import pandas as pd
import argparse
import ray
from tools import *

warnings.filterwarnings("ignore")


def main():
    all, model_names, num_gpus, output_file, samples_number, batch_size, prompt_ver = load_parameters()

    df = load_dataset()

    models = [
        "speakleash/Bielik-7B-Instruct-v0.1",
        "mistralai/Mistral-7B-Instruct-v0.3",
        "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "openchat/openchat-3.5-0106-gemma",
    ]
    if all:
        pass
    else:
        models = model_names
    if samples_number is None:
        samples_number = df.shape[0]

    llm_params = {
        "max_new_tokens": 1024,
        "do_sample": False
    }
    if output_file is None:
        output_file = "answers_prompt.csv"

    for model_name in models:
        #df = ray.get(calculate_for_model.options(num_gpus=num_gpus).remote(model_name, df[:samples_number], llm_params,
        #                                                                   prompt_ver=prompt_ver,
        #                                                                   batch_size=batch_size))
        df = calculate_for_model(model_name, df[:samples_number], llm_params, prompt_ver=prompt_ver, batch_size=batch_size)
        df.to_csv(output_file)


def load_parameters():
    parser = argparse.ArgumentParser(description="Script that generates answers for the benchmark.")
    parser.add_argument('--model_names', nargs='+', help='List with the names of the models to calculate the answers')
    parser.add_argument('--all', action='store_true', help='Calculate answers for all models from the scripts')
    parser.add_argument('--samples_number', type=int, default=None, help='Number of samples to generate answers')
    parser.add_argument('--output_file', type=str, default="generated_answers.csv",
                        help='Name of output file to save generated answers')
    parser.add_argument('--num_gpus', type=int, default=1, help="Number of GPUs")
    parser.add_argument('--batch_size', type=int, default=1, help="Batch size")
    parser.add_argument('--prompt_ver', type=int, default=1, help="Versions of generation prompt")
    args = parser.parse_args()
    return (args.all), (args.model_names), (args.num_gpus), (args.output_file), (args.samples_number), (
        args.batch_size), (args.prompt_ver)


def load_dataset():
    sheet_url = "TODO: paste link"
    df = pd.read_csv(sheet_url)
    return df


if __name__ == "__main__":
    main()
