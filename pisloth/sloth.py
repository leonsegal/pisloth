from robot_hat import Robot
from robot_hat import mapping

class Sloth(Robot):
    move_list = {
    "forward":[
      [0, 40, 0, 15],
      [-30, 40, -30, 15],
      [-30, 0, -30, 0],

      [0, -15, 0, -40],
      [30, -15, 30, -40],
      [30, 0, 30, 0],
      ],

    "turn right":[
      [0, -20, 0, -40],
      [-20, -20, 0, -40],
      [-20, 0, 0, 0],

      [0, 40, 0, 20],
      [20, 40, 0, 20],
      [20, 0, 0, 0],
      ],

    "turn left":[
      [0, 40, 0, 20],
      [0, 40, 20, 20],
      [0, 0, 20, 0],

      [0, -20, 0, -40],
      [0, -20, -20, -40],
      [0, 0, -20, 0],
      ],
    "backward":[
      [0, 40, 0, 15],
      [30, 40, 30, 15],
      [30, 0, 30, 0],

      [0, -15, 0, -40],
      [-30, -15, -30, -40],
      [-30, 0, -30, 0],
      ],

    "stand":[
      [0,0,0,0],
      ],

    "moon walk left": [
      [0, 0, 0, -30],
      [0, 30, 0, -60],
      [0, 60, 0, -30],
      [0, 30, 0, 0],
      [0, 0, 0, 0]
    ],
    "moon walk right": [
      [0, 30, 0, 0],
      [0, 60, 0, -30],
      [0, 30, 0, -60],
      [0, 0, 0, -30],
      [0, 0, 0, 0]
    ],


    "hook": [
      [0, 50, 0, -50],
    ],

    "big swing": [
      [0, -90, 0, 90],
    ],

    "swing": [
      [0, -40, 0, 40],
    ],

    "walk boldly": [
      [-15, -15, 15, -40],
      [10, -30, 40, -40],
      [10, 0, 40, 0],

      [-15, 40, 15, 15],
      [-40, 40, -10, 30],
      [-40, 0, -10, 0],
    ],

    "walk backward boldly": [
      [-15, -15, 15, -40],
      [-40, -30, -10, -40],
      [-40, 0, -10, 0],

      [-15, 40, 15, 15],
      [10, 40, 40, 30],
      [10, 0, 40, 0],
    ],

    "walk shyly": [
      [10, -15, -10, -40],
      [25, -30, -5, -40],
      [25, 0, -5, 0],

      [10, 40, -10, 15],
      [5, 40, -25, 30],
      [5, 0, -25, 0],
    ],

    "walk backward shyly": [
      [10, -15, -10, -40],
      [5, -30, -25, -40],
      [5, 0, -25, 0],

      [10, 40, -10, 15],
      [25, 40, -5, 30],
      [25, 0, -5, 0],
    ],


    "stomp right": [
      [0, 15, 0, 0],
      [0, 30, 0, -15],
      [0, 15, 0, -30],
      [0, 0, 0, -15],
      [0, 0, 0, 0],
    ], 
    "stomp left": [  
      [0, 0, 0, -15],
      [0, 15, 0, -30],
      [0, 30, 0, -15],
      [0, 15, 0, 0],
      [0, 0, 0, 0]
    ],

    "close": [
      [30, 0, -30, 0],
      # [0, 0, 0, 0]
    ],
    "open": [
      [-30, 0, 30, 0],
      # [0, 0, 0, 0]
    ],

    "tiptoe left":[
      [-20, 35, -20, 15],
      [-20, 15, -20, 15],
    ],

    "tiptoe right":[
      [20, -15, 20, -35],
      [20, -15, 20, -15],
    ],

    "fall left": [
      [-40, 70, -40, 30],
      [-40, 30, -40, 30],
    ],
    "fall right": [
      [40, -30, 40, -70],
      [40, -30, 40, -30],
    ],

    }

    def do_action(self,motion_name, step=1, speed=None, bpm=None):
        if bpm == None:
            speed = 50 if speed == None else speed
            # speed = mapping(speed, 0, 100, 0, 80)
        for _ in range(step):
            for motion in self.move_list[motion_name]:
                if bpm != None:
                    self.servo_move(motion, bpm=bpm)
                else:
                    self.servo_move(motion, speed=speed)

    def add_action(self,action_name,action_list):
        if action_name not in self.move_list.keys():
            self.move_list[action_name] = action_list

if __name__=="__main__":
    a = Sloth([1,2,3,4])
    while 1:
        for i in a.move_list:
            a.do_action(i,step=2,speed=100)