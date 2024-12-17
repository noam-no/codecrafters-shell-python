class ANSI_CHAR:
    # Styles
    BOLD = '1'       # Bold or increased intensity
    FAINT = '2'      # Decreased intensity
    ITALIC = '3'     # Italic
    UNDERLINE = '4'  # Underline
    BLINK = '5'      # Slow blink
    FAST_BLINK = '6' # Rapid blink
    REVERSE = '7'    # Reverse video
    CONCEAL = '8'    # Conceal
    STRIKE = '9'     # Crossed-out
    
    # Reset styles
    BOLD_OFF = '22'    # Normal intensity
    ITALIC_OFF = '23'  # Not italic
    UNDER_OFF = '24'   # Underline off
    BLINK_OFF = '25'   # Blink off
    REVERSE_OFF = '27' # Inverse off
    
    # Standard colors (foreground)
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    DEFAULT = '39'
    
    # Bright colors (foreground)
    BRIGHT_BLACK = '90'
    BRIGHT_RED = '91'
    BRIGHT_GREEN = '92'
    BRIGHT_YELLOW = '93'
    BRIGHT_BLUE = '94'
    BRIGHT_MAGENTA = '95'
    BRIGHT_CYAN = '96'
    BRIGHT_WHITE = '97'
    
    # Background colors
    BG_BLACK = '40'
    BG_RED = '41'
    BG_GREEN = '42'
    BG_YELLOW = '43'
    BG_BLUE = '44'
    BG_MAGENTA = '45'
    BG_CYAN = '46'
    BG_WHITE = '47'
    BG_DEFAULT = '49'

def graphics_text_parser(text, *args):
    prefix = "\033["
    suffix = "m"
    codes = []
    
    for arg in args:
        if hasattr(ANSI_CHAR, arg):
            codes.append(getattr(ANSI_CHAR, arg))
    if not codes:
        return text
    format_code = ";".join(codes)
    reset_code = "\033[0m"
    return f"{prefix}{format_code}{suffix}{text}{reset_code}"