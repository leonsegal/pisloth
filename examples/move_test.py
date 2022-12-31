from pisloth import Sloth

sloth = Sloth([1,2,3,4])
sloth.set_offset([0,0,0,0])

def main():
    sloth.do_action('fall left')


if __name__ == "__main__":
    while True:
        main()

