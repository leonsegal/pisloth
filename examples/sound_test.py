from robot_hat import Music
import time

music = Music()

def main():
    music.background_music('./musics/india-Arulo.mp3')
    music.music_set_volume(20)

    music.music_stop()
    time.sleep(10)

if __name__ == "__main__":
    while True:
        main()
