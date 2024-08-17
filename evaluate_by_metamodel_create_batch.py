import pandas as pd
from tools import generate_evaluating_metamodel_prompt
import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Script that generates evaluations for the benchmark.")
    parser.add_argument('--input_file', type=str, help='path of input file')
    parser.add_argument("--metamodel_prompt_ver", type=int, default=3, help="Version of metamodel prompt")
    parser.add_argument("--metamodel_name", type=str, default="gpt-4o", help="Version of the metamodel")
    parser.add_argument("--google_sheet_url", type=str, help="URL with google sheet containing original data")

    args = parser.parse_args()
    df_generated = pd.read_csv(args.input_file)
    answer_column = next((col for col in df_generated.columns if col.startswith('answer_')), None)
    sheet_url = args.google_sheet_url

    # Wczytywanie danych do ramki pandas
    df_gs = pd.read_csv(sheet_url)

    df = df_generated[[answer_column]]
    df = pd.concat([df, df_gs], axis=1)

    prompt_col_name = f"metamodel_prompt_{answer_column}"

    # Tworzymy nową kolumnę, stosując funkcję generate_evaluation_prompt
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

    model_name = os.path.splitext(os.path.basename(args.input_file))[0]
    filename = f"data/batch_files/{model_name}.jsonl"
    # Otwieramy plik do zapisu
    with open(filename, 'w', encoding='utf-8') as f:
        # Iterujemy przez każdy wiersz w kolumnie
        for index, cell_content in df[prompt_col_name].items():
            # Tworzymy słownik z danymi
            data = {
                "custom_id": f"{model_name}_{index}",  # Używamy indeksu wiersza jako DF_ID
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": args.metamodel_name,
                    "messages": cell_content,
                    "max_tokens": 50,
                    "temperature": 0.0
                }
            }

            # Zapisujemy wiersz JSONL do pliku
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')

    print("The JSONL were created.")


if __name__ == "__main__":
    main()