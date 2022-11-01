point = 10
bag = [[0 for i in range(4)] for j in range(2)]
inf, ast = True, False
place_index = [0, 0, 0]
weight = []
object = [['Винтовка', 'в', 3, 25], ['Пистолет', 'п', 2, 15], ['Боекомплект', 'б', 2, 15], ['Аптечка', 'а', 2, 20],
          ['Ингалятор', 'и', 1, 5], ['Нож', 'н', 1, 15], ['Топор', 'т', 3, 20], ['Оберег', 'о', 1, 25],
          ['Фляжка', 'ф', 1, 15], ['Антидот', 'д', 1, 10], ['Еда', 'к', 2, 20], ['Арбалет', 'р', 2, 20]]

def add_to_bag(object):
    global place_index
    global point
    place = object[2]
    marker = True
    for i in range(place):
        if (place_index[0] >= 4):
            place_index[2] = 1
            break
        if (place <= 4 - place_index[0] and marker):
            point += object[3]
            marker = False
        bag[0][place_index[0]] = object[1]
        place_index[0] += 1
        place -= 1

    if (place_index[2] == 1):
        if (place > 0):
            if (place <= 4 - place_index[1]):
                point += object[3]
                for i in range(place):
                    if (place_index[1] >= 4):
                        break
                    bag[1][place_index[1]] = object[1]
                    place_index[1] += 1


def key(weight):
    return weight[2]

if inf:
    add_to_bag(object[9])
if ast:
    add_to_bag(object[4])

for i in range(len(object)):
    weight.append([i, object[i][2], object[i][3] / object[i][2]])
weight.sort(key=key, reverse=True)

for i in range(6):
    add_to_bag(object[weight[i][0]])
for i in range(6):
    point -= object[weight[i + 6][0]][3]

variants = [[[0, 1, 2, 3, 4, 6], [5, 7, 8, 9, 10, 11]], [[0, 1, 2, 3, 7], [4, 5, 6, 8, 9, 10, 11]],
        [[0, 1, 2, 3, 4, 8], [5, 7, 6, 9, 10, 11]], [[0, 1, 2, 3, 4, 9], [5, 7, 6, 8, 10, 11]],
        [[0, 1, 2, 3, 10], [5, 7, 6, 9, 4, 8, 11]], [[0, 1, 2, 4, 9, 8], [5, 7, 6, 3, 10, 11]],
        [[0, 1, 2, 4, 9, 8], [5, 7, 6, 3, 10, 11]], [[0, 1, 2, 3, 10], [5, 7, 6, 4, 8, 9, 11]]]

for i in range(len(variants)):
    bag = [[0 for i in range(4)] for j in range(2)]
    point = 10
    place_index = [0, 0, 0]
    for j in range(len(variants[i][0])):
        add_to_bag(object[weight[variants[i][0][j]][0]])
    for j in range(len(variants[i][1])):
        point -= object[weight[variants[i][1][j]][0]][3]

    if (point > 0):
        print(bag[0])
        print(bag[1])
        print('point: ' + str(point))