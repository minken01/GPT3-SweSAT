import openai
import pandas as pd

openai.api_key = "YOUR_API_KEY"
file_path = "CSV_FILE_PATH"

df = pd.read_csv(file_path)

 for i, row in df.iterrows():
        prompt = df.loc[i, "prompt"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt= prompt,
            temperature=0.0,
            max_tokens=3,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            api_key=openai.api_key,
        )
        response = response.get("choices")[0].get("text")
        if response[1] == df.loc[i,"correct_answer"][0]:
            print(i+1, "Answer: ", response, ",  Correct!")
        else:
            print(i+1, "Answer: ", response, ",  Wrong...")
