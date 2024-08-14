import pandas as pd
from tools import generate_evaluating_metamodel_prompt
import argparse
from openai import OpenAI

def main():
    parser = argparse.ArgumentParser(description="Script that generates evaluations for the benchmark.")
    parser.add_argument('--input_file', type=str, help='path of input file')
    parser.add_argument('--output_file', type=str, help='path of output file')
    parser.add_argument("--api_key", type=str, help="key for metamodel api key")
    parser.add_argument("--metamodel_name", type=str, help="Name of the metamodel")
    parser.add_argument("--base_url", type=str, help="Base url of the metamodel API")
    parser.add_argument("--metamodel_prompt_ver", type=int, default=1, help="Version of metamodel prompt")

    args = parser.parse_args()
    df_generated = pd.read_csv(args.input_file)
    answer_column = next((col for col in df_generated.columns if col.startswith('answer_')), None)
    sheet_url = "https://docs.google.com/spreadsheets/d/13BWWkJipOFIabCVEzY-eelkYtliTTjnV3XMBfztW6Mc/export?format=csv"

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
            reference_idioms=row['Związki frazeologiczne']
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

    df = df.drop(columns=['Licznik', 'Unnamed: 6'])
    df.to_csv(args.output_file)


if __name__ == "__main__":
    main()