def get_field(val):
    head = val.rstrip('0123456789')
    tail = val[len(head):]
    return head, int(tail)


row_vals = ["a", "b", "c"]
rows_h = [0] * 9
rows_v = [0] * 9


def check_hz_v(game):
    for i in range(0, 3):
        for ind in range(0, 3):
            val_h = game[row_vals[i]][ind]
            val_v = game[row_vals[ind]][i]
            val_desc = game[row_vals[i]][i]
            val_asc = game[row_vals[2 - i]][i]
            print(f"DESC: {val_desc} ASC:{val_asc}")


class field:
    field = {}

    def __init__(self):
        self.field["a"] = [" ", " ", " "]
        self.field["b"] = [" ", " ", " "]
        self.field["c"] = [" ", " ", " "]

    def get(self):
        return self.field

    def add_tick(self, row, column, ai):

        if " " in self.field[row] and 0 <= column <= 2:
            if ai:
                self.field[row][column] = "O"
                return True
            self.field[row][column] = "X"
            return True
        else:
            print("Please provide a valid entry!")
            return False

    def display(self):
        for row in self.field:
            drawstring = "|"
            for val in self.field[row]:
                drawstring += val + "|"

            print(drawstring)


turn = 0
playing = True
prev_turn = 1
if __name__ == "__main__":
    new_field = field()

    while playing:
        if prev_turn != turn:
            if turn % 2 == 0:
                new_field.display()
                print("Your turn...\n")
            else:
                print("The AI takes it's turn...")
            prev_turn = turn

        if turn % 2 == 0:
            to_row, to_column = get_field(input())
            new_field.add_tick(to_row.lower(), to_column - 1, False)
            turn += 1
        else:
            check_hz_v(new_field.get())
            turn += 1
