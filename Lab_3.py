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
    flag = True
    for i in range(place):
        if (place_index[0] >= 4):
            place_index[2] = 1
            break
        if (place <= 4 - place_index[0] and flag):
            point += object[3]
            flag = False
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

def custom_key(weight):
    return weight[2]

if inf:
    add_to_bag(object[9])
if ast:
    add_to_bag(object[4])

for i in range(len(object)):
    weight.append([i, object[i][2], object[i][3] / object[i][2]])
weight.sort(key=custom_key, reverse=True)

for i in range(6):
    add_to_bag(object[weight[i][0]])
for i in range(6):
    point -= object[weight[i + 6][0]][3]

print(bag[0])
print(bag[1])
print('point: ' + str(point))
