import queue
import time
import curses

path = [
    ["#", "#", "#", "#", "#", " ", " ", "O", "#", "#", "#", "#", "#", " ", "#", "#", "#"],
    ["#", "#", " ", " ", " ", " ", "#", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", "#", "#", " ", "#", " ", "#", " ", " ", "#", " ", " ", " ", "#", "#"],
    ["#", " ", "#", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", "#", " ", " ", "#", "#", " ", " ", " ", "#", " ", "#", " ", " ", " "],
    ["#", " ", "#", " ", "#", " ", " ", "#", "#", " ", " ", " ", " ", "#", "#", "#", " "],
    ["#", " ", " ", " ", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", " "],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    [" ", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", "#", " ", " "],
    [" ", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", " "],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", "#", "#", " ", " ", " ", " "],
    [" ", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", " ", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "#"],
    [" ", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", "X", " ", "#", "#"],
]

initial = (0, 7)
final = 'X'


def draw_path(screen, path, route=[]):
    white = curses.color_pair(1)
    green = curses.color_pair(2)

    for i, row in enumerate(path):          # row is the elements in path
        for j, value in enumerate(row):     # j is the column in each row
            if (i, j) in route:
                screen.addstr(i, j*2, "  ", green)
            else:
                screen.addstr(i, j*2, value, white)


def find_route(screen, path):
    crossed = set()  # paths that have already been taken

    q = queue.Queue()
    q.put((initial, [initial]))     #

    while not q.empty():
        position, route = q.get()
        row, col = position

        screen.clear()
        draw_path(screen, path, route)
        screen.refresh()

        if path[row][col] == final:
            return route

        steps = find_next_step(path, row, col)
        for step in steps:
            ro, co = step
            if path[ro][co] == '#':
                continue
            if step in crossed:
                continue
            new_route = route + [step]
            q.put((step, new_route))
            crossed.add(step)


def find_next_step(path, row, col):
    next_steps = []
    if row > 0:
        next_steps.append((row-1, col))
    if row + 1 < len(path):
        next_steps.append((row+1, col))
    if col > 0:
        next_steps.append((row, col-1))
    if col + 1 < len(path[0]):
        next_steps.append((row, col+1))

    time.sleep(0.3)
    return next_steps


def main(screen):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_MAGENTA)

    find_route(screen, path)
    screen.getch()


curses.wrapper(main)
