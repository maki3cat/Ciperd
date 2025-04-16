with open('gpt4-80', 'r') as f:
    with open('gpt4_80_prompt.txt', 'w') as f_out:
        with open('gpt4_80_conv.txt', 'w') as f_out2:
            for line in f:
                if line.startswith('['):
                    f_out.write(line)
                else:
                    f_out2.write(line)

with open('gemini-20', 'r') as f:
    with open('gemini_20_prompt.txt', 'w') as f_out:
        with open('gemini_20_conv.txt', 'w') as f_out2:
            for line in f:
                if line.startswith('['):
                    f_out.write(line)
                else:
                    f_out2.write(line)
