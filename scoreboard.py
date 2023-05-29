from turtle import Screen,Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        with open("data.txt", "r") as file:
            last_line = file.readlines()[-1]
            self.high_score=int(last_line)
        self.color("white")
        self.penup()
        self.goto(0, 270)

        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=('Arial', 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="a") as file:
                file.write(f"\n{self.high_score}")

        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    """def game_over(self):
        self.goto(0, 0)
        self.write("Game Over ", False, align="center", font=('Arial', 24, 'normal'))"""





