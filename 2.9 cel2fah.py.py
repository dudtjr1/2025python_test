print('섭씨\t 화씨')

for celsius in range(0, 51, 10):
    fahrenhit = (9/5) * celsius + 32
    print(f'{celsius}\t {fahrenhit}')