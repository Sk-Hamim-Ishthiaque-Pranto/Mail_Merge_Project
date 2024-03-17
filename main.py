with open('./Input/Names/invited_names.txt') as file:
    name_list = file.read().split('\n')
with open('./Input/Letters/starting_letter.txt', 'r') as sample_file:
    temp_text = sample_file.read()

for name in name_list:
    with open(f'./Output/ReadyToSend/letter_for_{name}', 'w') as output_file:
        output_file.write(temp_text.replace('[name]', name))
