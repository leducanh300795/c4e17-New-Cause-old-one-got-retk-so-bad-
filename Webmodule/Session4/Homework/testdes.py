from random import randint,choice
def measurements():
    mesurements = [randint(85,95), randint(55,65), randint(85,95)]

    return (mesurements)
mesure = measurements()
print(mesure)

def description():
    characters = ['dễ dãi', 'vui vẻ', 'hòa đồng', 'yêu đời',
                  'khéo léo', 'hài hước', 'ngáo đá', 'điên dại',
                  'tình cảm', 'sida', 'hâm', 'cẩn thận',
                  'nổi loạn', 'cầu toàn', 'bốc đồng']
    description = []
    for i in range(randint(3,6)):
        character = choice(characters)
        description.append(character)
    return (description)
des = description()
print(*des, sep=', ')
