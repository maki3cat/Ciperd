

with open('gpt4-80', 'r') as f:
    with open('prompt.txt', 'w') as f_out:
        with open('response.txt', 'w') as f_out2:
            for line in f:
                if line.startswith('['):
                    f_out.write(line)
                else:
                    f_out2.write(line)
