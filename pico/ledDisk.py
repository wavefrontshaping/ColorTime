from neopixel import Neopixel
from utime import ticks_ms, sleep_ms

N_LEDS = 61

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
WHITE = (255,255,255)

RGB_COLORS = [[0, 128, 0], [1, 128, 0], [2, 129, 0], [3, 129, 0], [5, 130, 0], [6, 131, 0], [7, 131, 0], [9, 132, 0], [10, 133, 0], [12, 133, 0], [13, 134, 0], [14, 135, 0], [16, 135, 0], [17, 136, 0], [19, 136, 0], [20, 137, 0], [22, 138, 0], [23, 138, 0], [25, 139, 0], [26, 140, 0], [28, 140, 0], [29, 141, 0], [31, 142, 0], [32, 142, 0], [34, 143, 0], [36, 143, 0], [37, 144, 0], [39, 145, 0], [41, 145, 0], [42, 146, 0], [44, 147, 0], [46, 147, 0], [47, 148, 0], [49, 149, 0], [51, 149, 0], [52, 150, 0], [54, 150, 0], [56, 151, 0], [58, 152, 0], [59, 152, 0], [61, 153, 0], [63, 154, 0], [65, 154, 0], [67, 155, 0], [69, 156, 0], [70, 156, 0], [72, 157, 0], [74, 157, 0], [76, 158, 0], [78, 159, 0], [80, 159, 0], [82, 160, 0], [84, 161, 0], [86, 161, 0], [88, 162, 0], [90, 163, 0], [92, 163, 0], [94, 164, 0], [96, 165, 0], [98, 165, 0], [100, 166, 0], [102, 166, 0], [104, 167, 0], [106, 168, 0], [108, 168, 0], [110, 169, 0], [112, 170, 0], [114, 170, 0], [117, 171, 0], [119, 172, 0], [121, 172, 0], [123, 173, 0], [125, 173, 0], [128, 174, 0], [130, 175, 0], [132, 175, 0], [134, 176, 0], [137, 177, 0], [139, 177, 0], [141, 178, 0], [143, 179, 0], [146, 179, 0], [148, 180, 0], [150, 180, 0], [153, 181, 0], [155, 182, 0], [158, 182, 0], [160, 183, 0], [162, 184, 0], [165, 184, 0], [167, 185, 0], [170, 186, 0], [172, 186, 0], [175, 187, 0], [177, 187, 0], [180, 188, 0], [182, 189, 0], [185, 189, 0], [187, 190, 0], [190, 191, 0], [191, 190, 0], [192, 189, 0], [193, 188, 0], [193, 186, 0], [194, 185, 0], [195, 184, 0], [195, 182, 0], [196, 181, 0], [196, 180, 0], [197, 178, 0], [198, 177, 0], [198, 175, 0], [199, 174, 0], [200, 172, 0], [200, 171, 0], [201, 170, 0], [202, 168, 0], [202, 167, 0], [203, 165, 0], [203, 163, 0], [204, 162, 0], [205, 160, 0], [205, 159, 0], [206, 157, 0], [207, 156, 0], [207, 154, 0], [208, 152, 0], [209, 151, 0], [209, 149, 0], [210, 147, 0], [210, 146, 0], [211, 144, 0], [212, 142, 0], [212, 141, 0], [213, 139, 0], [214, 137, 0], [214, 136, 0], [215, 134, 0], [216, 132, 0], [216, 130, 0], [217, 128, 0], [217, 127, 0], [218, 125, 0], [219, 123, 0], [219, 121, 0], [220, 119, 0], [221, 117, 0], [221, 115, 0], [222, 114, 0], [223, 112, 0], [223, 110, 0], [224, 108, 0], [225, 106, 0], [225, 104, 0], [226, 102, 0], [226, 100, 0], [227, 98, 0], [228, 96, 0], [228, 94, 0], [229, 92, 0], [230, 90, 0], [230, 88, 0], [231, 86, 0], [232, 83, 0], [232, 81, 0], [233, 79, 0], [233, 77, 0], [234, 75, 0], [235, 73, 0], [235, 71, 0], [236, 68, 0], [237, 66, 0], [237, 64, 0], [238, 62, 0], [239, 60, 0], [239, 57, 0], [240, 55, 0], [240, 53, 0], [241, 50, 0], [242, 48, 0], [242, 46, 0], [243, 44, 0], [244, 41, 0], [244, 39, 0], [245, 36, 0], [246, 34, 0], [246, 32, 0], [247, 29, 0], [247, 27, 0], [248, 24, 0], [249, 22, 0], [249, 20, 0], [250, 17, 0], [251, 15, 0], [251, 12, 0], [252, 10, 0], [253, 7, 0], [253, 5, 0], [254, 2, 0], [255, 0, 0]]

N_STEPS = len(RGB_COLORS)

PARTS = [[0,1,2,3,24,25,26,40,41,52],
         [4,5,6,7,27,28,42,43,53,54],
         [8,9,10,29,30,31,44,45,55],
         [11,12,13,14,32,33,46,47,56],
         [15,16,17,34,35,36,48,57],
         [18,19,20,36,37,49,50,58],
         [21,22,23,38,39,51,59,60]]

N_PARTS = len(PARTS)

def _apply_brightness(color, brightness):
    return [min(int(x*brightness),x) for x in color]

class LedDisk():

    def __init__(self, pin):
        self.leds = Neopixel(N_LEDS, 0, pin, "GRB")

    def Rotate(self, timeout = 60_000, stop_callback = None):
        t0 = ticks_ms()
        ind_blue = [0,1,2]
        while True:
            for i_r in range(N_PARTS):
                ind_parts = [(x+i_r)%N_PARTS for x in ind_blue]           
                all_blue = []
                for i_blue in ind_parts:
                    all_blue += PARTS[i_blue]
                for i in range(N_LEDS):
                    if i in all_blue:
                        self.leds.set_pixel(i, BLUE)
                    else:
                        self.leds.set_pixel(i, RED)
                self.leds.show()
                sleep_ms(25)
            if stop_callback and stop_callback():
                return
            if(ticks_ms()-t0 > timeout):
                return

    def Wave(
        self,
        timeout = 60_000,
        stop_callback = None,
        pause = 50
    ):
        def check_stop():
            if stop_callback and stop_callback():
                return True
            if(ticks_ms()-t0 > timeout):
                return True
            return False
        t0 = ticks_ms()
        while True:
            for i in range(N_LEDS):
                self.leds.set_pixel(i, BLUE)
                self.leds.show()
                sleep_ms(pause)
                if check_stop():
                    return
            for i in range(N_LEDS):
                self.leds.set_pixel(i, RED)
                self.leds.show()
                sleep_ms(pause)
                if check_stop():
                    return

    def Blink(
        self,
        color = RED,
        timeout = 60_000,
        stop_callback = None,
        pause = 150,
        brightness = 1.,
    ):
        self.Flash(
            color1 = color,
            color2 = BLACK,
            timeout = timeout,
            stop_callback = stop_callback,
            pause = pause,
            brightness = brightness
        )

    def Flash(
        self,
        color1 = RED,
        color2 = BLUE,
        timeout = 60_000,
        stop_callback = None,
        pause = 150,
        brightness = 1.,
    ):
        t0 = ticks_ms()
        while True:
            self.leds.fill(_apply_brightness(color1, brightness))
            self.leds.show()
            sleep_ms(pause)
            self.leds.fill(_apply_brightness(color2, brightness))
            self.leds.show()
            sleep_ms(pause)
            if stop_callback and stop_callback():
                return
            if(ticks_ms()-t0 > timeout):
                return

    def Step(self, step_value, brightness_min = 1., brightness_max = 1.):

        if brightness_min == brightness_max:
            brightness = brightness_max
        else:
            brightness = min(step_value*(brightness_max-brightness_min)+brightness_min,1.)
        i_step = min(int(step_value*N_STEPS), N_STEPS-1)
        new_color = _apply_brightness(RGB_COLORS[i_step], brightness)
        self.leds.fill(new_color)
        self.leds.show()

    def Red(self):
        self.leds.fill(RED)
        self.leds.show()

    def Green(self):
        self.leds.fill(GREEN)
        self.leds.show()

    def Blue(self):
        self.leds.fill(BLUE)
        self.leds.show()

    def Off(self):
        self.leds.fill(BLACK)
        self.leds.show()


