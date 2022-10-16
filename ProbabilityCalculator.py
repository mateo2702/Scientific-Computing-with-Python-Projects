import random
import copy

class Hat:
    def __init__(self, **Balls):
        self.contents=[]
        for i in Balls:
            for j in range(Balls[i]):
                self.contents.append(i)
    
    def draw(self, numb):
        self.removed = []
        if numb > len(self.contents):
            return self.contents
        else:
            for i in range(numb):
                self.removed.append(self.contents.pop(random.randrange(len(self.contents))))
        return self.removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0

    for i in range(num_experiments):
        cont = 0
        hatCopy = copy.deepcopy(hat)
        draw = hatCopy.draw(num_balls_drawn)

        removed = dict()
        for ball in draw:
            removed[ball] = removed.get(ball, 0) + 1

        for key, value in expected_balls.items():
            if (value <= removed.get(key,0)):
                cont += 1

        if (cont == len(expected_balls)):
            probability += 1

    probability = probability/num_experiments

    return probability


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat, {"red":2,"green":1}, 5, 2000)
