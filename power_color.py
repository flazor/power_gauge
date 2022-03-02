
BLUE = '0000ff'
GREEN = '00ff00'
YELLOW = 'ffff00'
ORANGE = 'ff7f00'
RED = 'ff0000'

BLUE_LIMIT = 90
B_G_FADE_LIMIT = 100
GREEN_LIMIT = 150
G_Y_FADE_LIMIT = 200
YELLOW_LIMIT = 300
Y_O_FADE_LIMIT = 500
ORANGE_LIMIT = 700
O_R_FADE_LIMIT = 1000

def color(k_watts):
    if k_watts < BLUE_LIMIT:
        return f'#{BLUE}'
    elif k_watts < B_G_FADE_LIMIT:
        return color_fader(k_watts, BLUE_LIMIT, B_G_FADE_LIMIT, BLUE, GREEN)
    elif k_watts < GREEN_LIMIT:
        return f'#{GREEN}' 
    elif k_watts < G_Y_FADE_LIMIT:
        return color_fader(k_watts, GREEN_LIMIT, G_Y_FADE_LIMIT, GREEN, YELLOW)
    elif k_watts < YELLOW_LIMIT:
        return f'#{YELLOW}' 
    elif k_watts < ORANGE_LIMIT:
        return f'#{ORANGE}' 
    else:
        return f'#{RED}' 

def color_fader(n, scale_min, scale_max, start_color, end_color):
    # Strip leading '#' from colors if it exists
    if start_color[0] == '#':
        start_color = start_color[1:7]
    if end_color[0] == '#':
        end_color = end_color[1:7]
    r_min = int(start_color[0:2], 16)
    r_max = int(end_color[0:2], 16)
    g_min = int(start_color[2:4], 16)
    g_max = int(end_color[2:4], 16)
    b_min = int(start_color[4:6], 16)
    b_max = int(end_color[4:6], 16)
    return rgb_fader(n, scale_min, scale_max, r_min, r_max, g_min, g_max, b_min, b_max)

def rgb_fader(n, scale_min, scale_max, r_min=0, r_max=255, g_min=0, g_max=255, b_min=0, b_max=255):
    scale_factor = (n - scale_min) / (scale_max - scale_min)
    red = int(fade(scale_factor, r_min, r_max))
    green = int(fade(scale_factor, g_min, g_max))
    blue = int(fade(scale_factor, b_min, b_max))
    return f'#{red:02x}{green:02x}{blue:02x}'

def fade(scale_factor, color_start=0, color_end=255):
    return (color_end - color_start) * scale_factor + color_start 

