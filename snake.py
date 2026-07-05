#!/usr/bin/env python3
import curses, random, time

def main(s):
    curses.curs_set(0)
    s.nodelay(1)
    s.timeout(100)
    h, w = s.getmaxyx()
    snake = [(h//2, w//4)]
    food = (random.randint(1,h-2), random.randint(1,w-2))
    d = (0,1)
    score = 0
    while True:
        key = s.getch()
        if key == ord('q'): break
        if key == curses.KEY_UP and d != (1,0): d = (-1,0)
        elif key == curses.KEY_DOWN and d != (-1,0): d = (1,0)
        elif key == curses.KEY_LEFT and d != (0,1): d = (0,-1)
        elif key == curses.KEY_RIGHT and d != (0,-1): d = (0,1)
        head = (snake[0][0]+d[0], snake[0][1]+d[1])
        if (head[0]<=0 or head[0]>=h-1 or head[1]<=0 or head[1]>=w-1 or head in snake):
            break
        snake.insert(0, head)
        if head == food:
            score += 1
            while True:
                food = (random.randint(1,h-2), random.randint(1,w-2))
                if food not in snake: break
        else:
            snake.pop()
        s.clear()
        s.border(0)
        s.addstr(0, 2, f" Snake {score} ")
        s.addch(food[0], food[1], curses.ACS_DIAMOND)
        for i, (y,x) in enumerate(snake):
            ch = '@' if i==0 else 'o'
            try: s.addch(y, x, ch)
            except: pass
        s.refresh()
        time.sleep(0.08)
    s.clear()
    s.addstr(h//2, w//2-5, f"GAME OVER - Score: {score}")
    s.refresh()
    time.sleep(2)

curses.wrapper(main)
