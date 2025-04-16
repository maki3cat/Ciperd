def one_file(path, prompt_file, data_file):
    prompt_count, data_count = 0, 0
    with open(prompt_file, 'a') as pf:
        with open(data_file, 'a') as df:
            oneline_data = []
            with open(path, 'r') as f:
                lines = f.readlines()
                count = 0
                for line in lines:
                    count += 1
                    line = line.strip()
                    line = line.strip("\n")
                    if len(line) <= 1 and len(oneline_data) > 0:
                        flush(oneline_data, df)
                        oneline_data = []
                        data_count += 1
                        continue
                    if len(line) <= 1:
                        continue
                    if line.strip().startswith('['):
                        if len(oneline_data) > 0:
                            flush(oneline_data, df)
                            oneline_data = []
                            data_count += 1
                        pf.write(line+"\n")
                        prompt_count += 1
                    else:
                        oneline_data.append(line)
            if len(oneline_data) > 0:
                flush(oneline_data, df)
                oneline_data = []
                data_count += 1
    print(f"Prompt count: {prompt_count}, Data count: {data_count}")


def flush(resp_lines, df):
    print("Flushing lines", resp_lines, len(resp_lines))
    df.write(("".join(resp_lines)).strip()+"\n")


# prompt_file = "data_2b/gemini_1_prompt.txt"
# data_file = "data_2b/gemini_1_data.txt"
# one_file("data_2b/data2_gemini_api.txt", prompt_file, data_file)

for i in range(1, 8):
    prompt_file = f"data_2b/gemini_{i}_prompt.txt"
    data_file = f"data_2b/gemini_{i}_data.txt"
    one_file(f"data_2b/raw/data2_gemini_api_{i}.txt", prompt_file, data_file)
