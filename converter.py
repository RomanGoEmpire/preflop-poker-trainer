# loop over all files in cards folder
import os

for filename in os.listdir('C:\\Users\\gerlo\\Programming\\PycharmProjects\\preflop_poker\\images\\cards'):
    split = filename.split('.')[0].split('_')
    if split[0] == '10':
        split[0] = 'T'
    rank_letter = split[0][0].upper()
    suit_letter = split[2][:1]
    new = f'{rank_letter}_{suit_letter}.svg'
    print(new)
    os.rename(f'C:\\Users\\gerlo\\Programming\\PycharmProjects\\preflop_poker\\images\\cards\\{filename}', f'C:\\Users\\gerlo\\Programming\\PycharmProjects\\preflop_poker\\images\\cards\\{new}')
