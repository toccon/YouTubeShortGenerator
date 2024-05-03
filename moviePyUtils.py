from moviepy.editor import TextClip

def createTextClip(text, font="Arial", fontsize=100, color="white", border_color=None, border_width=0, start=0, duration=0,
                   method="label", size=None, align="center",
                   on_color=False, on_color_width=0, on_color_height=0, on_color_opacity=1.0, on_color_color=(0,0,0)):
    """General function to add text to a video. Currently need to call .set_position() after to set the position of the text. 

    Args:
        text (_type_): _description_
        fontsize (int, optional): _description_. Defaults to 100.
        color (str, optional): _description_. Defaults to "white".
        border_color (_type_, optional): _description_. Defaults to None.
        border_width (int, optional): _description_. Defaults to 0.
        start (int, optional): _description_. Defaults to 0.
        duration (int, optional): _description_. Defaults to 5.
        on_color (bool, optional): _description_. Defaults to False.
        on_color_width (int, optional): _description_. Defaults to 0.
        on_color_height (int, optional): _description_. Defaults to 0.
        on_color_opacity (float, optional): _description_. Defaults to 1.0.
        on_color_color (tuple, optional): _description_. Defaults to (0,0,0).

    Returns:
        TextClip: text clip to be used in a CompositeVideoClip
    """
    
    text_clip = TextClip(text, font=font, fontsize=fontsize, color=color, stroke_color=border_color, stroke_width=border_width, method=method, size=size, align=align)

    if(duration != 0):
        text_clip = text_clip.set_duration(duration)
    
    if(on_color):
        text_clip = text_clip.on_color(size=(on_color_width,on_color_height), color=on_color_color, pos="center", col_opacity=on_color_opacity)
    
    text_clip = text_clip.set_start(start)
    text_clip = text_clip.set_duration(duration)
    return text_clip