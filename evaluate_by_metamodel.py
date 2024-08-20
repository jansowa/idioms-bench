import pandas as pd
from tools import generate_evaluating_metamodel_prompt
import argparse
import os
import glob
from openai import OpenAI


def process_file(input_file, output_file, args):
    df_generated = pd.read_csv(input_file)
    answer_column = next((col for col in df_generated.columns if col.startswith('answer_')), None)
    sheet_url = args.google_sheet_url

    df_gs = pd.read_csv(sheet_url)

    df = df_generated[[answer_column]]
    df = pd.concat([df, df_gs], axis=1)

    prompt_col_name = f"metamodel_prompt_{answer_column}"

    # Tworzymy nową kolumnę, stosując funkcję generate_evaluating_metamodel_prompt
    df[prompt_col_name] = df.apply(
        lambda row: generate_evaluating_metamodel_prompt(
            model_response=row[answer_column],
            reference_explanation=row['Wyjaśnienie'],
            reference_sentiment=row['Sentyment'],
            reference_idioms=row['Związki frazeologiczne'],
            prompt_ver=args.metamodel_prompt_ver
        ),
        axis=1
    )

    API_KEY = args.api_key
    MODEL_NAME = args.metamodel_name
    BASE_URL = args.base_url

    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
    )

    def get_metamodel_evaluation(prompt):
        try:
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=prompt,
                temperature=0.0,
                max_tokens=100
            )
            response = completion.choices[0].message.content.strip()
        except:
            response = "ERROR"
        print(response)
        return response

    df['evaluation_' + answer_column] = df[prompt_col_name].apply(get_metamodel_evaluation)

    df = df.drop(columns=['Licznik', 'Unnamed: 6'], errors='ignore')
    df.to_csv(output_file, index=False)


def main():
    parser = argparse.ArgumentParser(description="Script that generates evaluations for the benchmark.")
    parser.add_argument('--input_file', type=str, help='Path of input file')
    parser.add_argument('--input_directory', type=str, help='Path of input directory containing CSV files')
    parser.add_argument('--output_directory', type=str, help='Directory where output files will be saved',
                        default='output')
    parser.add_argument("--api_key", type=str, help="Key for metamodel API")
    parser.add_argument("--metamodel_name", type=str, help="Name of the metamodel")
    parser.add_argument("--base_url", type=str, help="Base URL of the metamodel API")
    parser.add_argument("--metamodel_prompt_ver", type=int, default=3, help="Version of metamodel prompt")
    parser.add_argument("--google_sheet_url", type=str, help="URL with Google Sheet containing original data")

    args = parser.parse_args()

    if not os.path.exists(args.output_directory):
        os.makedirs(args.output_directory)

    if args.input_file:
        output_file = os.path.join(args.output_directory, os.path.basename(args.input_file))
        process_file(args.input_file, output_file, args)
    elif args.input_directory:
        csv_files = glob.glob(os.path.join(args.input_directory, "*.csv"))
        for csv_file in csv_files:
            output_file = os.path.join(args.output_directory, os.path.basename(csv_file))
            process_file(csv_file, output_file, args)
    else:
        print("Please provide either --input_file or --input_directory.")


if __name__ == "__main__":
    main()
