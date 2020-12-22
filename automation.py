import copy

RUN_UNTIL_DIE = True
MAXIT = 20

class Automation:
    def __init__(self, init_state, action):
        self.row_size = len(init_state)
        self.column_size = len(init_state[0])
        self.state = copy.deepcopy(init_state)
        self.prev_state = copy.deepcopy(init_state)
        self.action = action
        self.expand()

    def expand(self):
        empty_row = [0 for i in range(len(self.state[0]))]
        self.state.insert(0, copy.deepcopy(empty_row))
        self.state.append(empty_row)
        for row in self.state:
            row.insert(0, 0)
            row.append(0)

    def clear(self):
        for row in range(1, self.row_size):
            for col in range(1, self.column_size):
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

    def expand_if_needed(self):
        need_to_expand = False
        col = 1
        for row in range(1, self.row_size + 1):
            if self.state[row][col] == 1:
                need_to_expand = True
                break
        if need_to_expand is False:
            col = self.column_size
            for row in range(1, self.row_size + 1):
                if self.state[row][col] == 1:
                    need_to_expand = True
                    break
        if need_to_expand is False:
            row = 1
            for col in range(1, self.column_size + 1):
                if self.state[row][col] == 1:
                    need_to_expand = True
                    break
        if need_to_expand is False:
            row = self.row_size
            for col in range(1, self.column_size + 1):
                if self.state[row][col] == 1:
                    need_to_expand = True
                    break
        if need_to_expand is True:
            self.expand()
            self.row_size += 2
            self.column_size += 2

    def step(self):
        self.prev_state = copy.deepcopy(self.state)
        self.clear()
        for row in range(1, self.row_size + 1):
            for col in range(1, self.column_size + 1):
                cell_with_friends = [self.prev_state[row - 1][col - 1], self.prev_state[row - 1][col], self.prev_state[row - 1][col + 1],
                                     self.prev_state[row + 0][col - 1], self.prev_state[row + 0][col], self.prev_state[row + 0][col + 1],
                                     self.prev_state[row + 1][col - 1], self.prev_state[row + 1][col], self.prev_state[row + 1][col + 1]]
                if self.action(cell_with_friends) is True:
                    self.state[row][col] = 1
        self.expand_if_needed()
        return self.is_dead()

    def print(self):
        print("")
        for row in range(1, self.row_size + 1):
            for col in range(1, self.column_size + 1):
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


init_state = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 1, 1, 0, 0],
              [0, 1, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

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

