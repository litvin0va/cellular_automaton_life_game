import copy

RUN_UNTIL_DIE = True
MAXIT = 10

class Automation:
    def __init__(self, init_state, action):
        self.state = copy.deepcopy(init_state)
        self.prev_state = copy.deepcopy(init_state)
        self.action = action
        self.row_size = len(init_state)
        self.column_size = len(init_state[0])

    def clear(self):
        for row in range(self.row_size):
            for col in range(self.column_size):
                self.state[row][col] = 0

    def is_same(self):
        return self.state == self.prev_state

    def is_empty(self):
        for row in range(self.row_size):
            for col in range(self.column_size):
                if self.state[row][col] == 1:
                    return False
        return True

    def is_dead(self):
        return self.is_empty() or self.is_same()

    def step(self):
        self.prev_state = copy.deepcopy(self.state)
        self.clear()
        for row in range(1, self.row_size - 1):
            for col in range(1, self.column_size - 1):
                cell_with_friends = [self.prev_state[row - 1][col - 1], self.prev_state[row - 1][col], self.prev_state[row - 1][col + 1],
                                     self.prev_state[row + 0][col - 1], self.prev_state[row + 0][col], self.prev_state[row + 0][col + 1],
                                     self.prev_state[row + 1][col - 1], self.prev_state[row + 1][col], self.prev_state[row + 1][col + 1]]
                if self.action(cell_with_friends) is True:
                    self.state[row][col] = 1
        return self.is_dead()

    def print(self):
        print("\n")
        for row in range(self.row_size):
            for col in range(self.column_size):
                print(self.state[row][col], end='')
            print("")

def life_action(cell):
    friends_sum = cell[0] + cell[1] + cell[2] +\
                  cell[3] +           cell[5] +\
                  cell[6] + cell[7] + cell[8]
    if cell[4] == 1:
        if friends_sum == 2 or friends_sum == 3:
            return True
        else:
            return False
    else:
        if friends_sum == 3:
            return True
        else:
            return False


init_state = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

auto = Automation(init_state, life_action)
auto.print()
if RUN_UNTIL_DIE == True:
    for i in range(MAXIT):
        if auto.step() is True:
            auto.print()
            print("Game Over!")
            break
        auto.print()
else:
    while True:
        action = input()
        if action == "s":
            if auto.step() is True:
                auto.print()
                print("Game Over!")
                break
            auto.print()
        else:
            break

