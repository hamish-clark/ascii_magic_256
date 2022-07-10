import sys
import colorama
from PIL import Image

import webbrowser
import urllib.error
import urllib.request
from enum import Enum

from numpy import array


__VERSION__ = 1.6


_COLOR_DATA_8 = [
	[(  0,   0,   0), colorama.Fore.LIGHTBLACK_EX, '#222'],
	[(  0,   0, 255), colorama.Fore.BLUE, '#00F'],
	[(  0, 255,   0), colorama.Fore.GREEN, '#0F0'],
	[(255,   0,   0), colorama.Fore.RED, '#F00'],
	[(255, 255, 255), colorama.Fore.WHITE, '#FFF'],
	[(255,   0, 255), colorama.Fore.MAGENTA, '#F0F'],
	[(  0, 255, 255), colorama.Fore.CYAN, '#0FF'],
	[(255, 255,   0), colorama.Fore.YELLOW, '#FF0']
]



_COLOR_DATA_256 = [
[(0, 0, 0), 0, '#000000'],
[(128, 0, 0), 1, '#800000'],
[(0, 128, 0), 2, '#008000'],
[(128, 128, 0), 3, '#808000'],
[(0, 0, 128), 4, '#000080'],
[(128, 0, 128), 5, '#800080'],
[(0, 128, 128), 6, '#008080'],
[(192, 192, 192), 7, '#c0c0c0'],
[(128, 128, 128), 8, '#808080'],
[(255, 0, 0), 9, '#ff0000'],
[(0, 255, 0), 10, '#00ff00'],
[(255, 255, 0), 11, '#ffff00'],
[(0, 0, 255), 12, '#0000ff'],
[(255, 0, 255), 13, '#ff00ff'],
[(0, 255, 255), 14, '#00ffff'],
[(255, 255, 255), 15, '#ffffff'],
[(0, 0, 0), 16, '#000000'],
[(0, 0, 95), 17, '#00005f'],
[(0, 0, 135), 18, '#000087'],
[(0, 0, 175), 19, '#0000af'],
[(0, 0, 215), 20, '#0000d7'],
[(0, 0, 255), 21, '#0000ff'],
[(0, 95, 0), 22, '#005f00'],
[(0, 95, 95), 23, '#005f5f'],
[(0, 95, 135), 24, '#005f87'],
[(0, 95, 175), 25, '#005faf'],
[(0, 95, 215), 26, '#005fd7'],
[(0, 95, 255), 27, '#005fff'],
[(0, 135, 0), 28, '#008700'],
[(0, 135, 95), 29, '#00875f'],
[(0, 135, 135), 30, '#008787'],
[(0, 135, 175), 31, '#0087af'],
[(0, 135, 215), 32, '#0087d7'],
[(0, 135, 255), 33, '#0087ff'],
[(0, 175, 0), 34, '#00af00'],
[(0, 175, 95), 35, '#00af5f'],
[(0, 175, 135), 36, '#00af87'],
[(0, 175, 175), 37, '#00afaf'],
[(0, 175, 215), 38, '#00afd7'],
[(0, 175, 255), 39, '#00afff'],
[(0, 215, 0), 40, '#00d700'],
[(0, 215, 95), 41, '#00d75f'],
[(0, 215, 135), 42, '#00d787'],
[(0, 215, 175), 43, '#00d7af'],
[(0, 215, 215), 44, '#00d7d7'],
[(0, 215, 255), 45, '#00d7ff'],
[(0, 255, 0), 46, '#00ff00'],
[(0, 255, 95), 47, '#00ff5f'],
[(0, 255, 135), 48, '#00ff87'],
[(0, 255, 175), 49, '#00ffaf'],
[(0, 255, 215), 50, '#00ffd7'],
[(0, 255, 255), 51, '#00ffff'],
[(95, 0, 0), 52, '#5f0000'],
[(95, 0, 95), 53, '#5f005f'],
[(95, 0, 135), 54, '#5f0087'],
[(95, 0, 175), 55, '#5f00af'],
[(95, 0, 215), 56, '#5f00d7'],
[(95, 0, 255), 57, '#5f00ff'],
[(95, 95, 0), 58, '#5f5f00'],
[(95, 95, 95), 59, '#5f5f5f'],
[(95, 95, 135), 60, '#5f5f87'],
[(95, 95, 175), 61, '#5f5faf'],
[(95, 95, 215), 62, '#5f5fd7'],
[(95, 95, 255), 63, '#5f5fff'],
[(95, 135, 0), 64, '#5f8700'],
[(95, 135, 95), 65, '#5f875f'],
[(95, 135, 135), 66, '#5f8787'],
[(95, 135, 175), 67, '#5f87af'],
[(95, 135, 215), 68, '#5f87d7'],
[(95, 135, 255), 69, '#5f87ff'],
[(95, 175, 0), 70, '#5faf00'],
[(95, 175, 95), 71, '#5faf5f'],
[(95, 175, 135), 72, '#5faf87'],
[(95, 175, 175), 73, '#5fafaf'],
[(95, 175, 215), 74, '#5fafd7'],
[(95, 175, 255), 75, '#5fafff'],
[(95, 215, 0), 76, '#5fd700'],
[(95, 215, 95), 77, '#5fd75f'],
[(95, 215, 135), 78, '#5fd787'],
[(95, 215, 175), 79, '#5fd7af'],
[(95, 215, 215), 80, '#5fd7d7'],
[(95, 215, 255), 81, '#5fd7ff'],
[(95, 255, 0), 82, '#5fff00'],
[(95, 255, 95), 83, '#5fff5f'],
[(95, 255, 135), 84, '#5fff87'],
[(95, 255, 175), 85, '#5fffaf'],
[(95, 255, 215), 86, '#5fffd7'],
[(95, 255, 255), 87, '#5fffff'],
[(135, 0, 0), 88, '#870000'],
[(135, 0, 95), 89, '#87005f'],
[(135, 0, 135), 90, '#870087'],
[(135, 0, 175), 91, '#8700af'],
[(135, 0, 215), 92, '#8700d7'],
[(135, 0, 255), 93, '#8700ff'],
[(135, 95, 0), 94, '#875f00'],
[(135, 95, 95), 95, '#875f5f'],
[(135, 95, 135), 96, '#875f87'],
[(135, 95, 175), 97, '#875faf'],
[(135, 95, 215), 98, '#875fd7'],
[(135, 95, 255), 99, '#875fff'],
[(135, 135, 0), 100, '#878700'],
[(135, 135, 95), 101, '#87875f'],
[(135, 135, 135), 102, '#878787'],
[(135, 135, 175), 103, '#8787af'],
[(135, 135, 215), 104, '#8787d7'],
[(135, 135, 255), 105, '#8787ff'],
[(135, 175, 0), 106, '#87af00'],
[(135, 175, 95), 107, '#87af5f'],
[(135, 175, 135), 108, '#87af87'],
[(135, 175, 175), 109, '#87afaf'],
[(135, 175, 215), 110, '#87afd7'],
[(135, 175, 255), 111, '#87afff'],
[(135, 215, 0), 112, '#87d700'],
[(135, 215, 95), 113, '#87d75f'],
[(135, 215, 135), 114, '#87d787'],
[(135, 215, 175), 115, '#87d7af'],
[(135, 215, 215), 116, '#87d7d7'],
[(135, 215, 255), 117, '#87d7ff'],
[(135, 255, 0), 118, '#87ff00'],
[(135, 255, 95), 119, '#87ff5f'],
[(135, 255, 135), 120, '#87ff87'],
[(135, 255, 175), 121, '#87ffaf'],
[(135, 255, 215), 122, '#87ffd7'],
[(135, 255, 255), 123, '#87ffff'],
[(175, 0, 0), 124, '#af0000'],
[(175, 0, 95), 125, '#af005f'],
[(175, 0, 135), 126, '#af0087'],
[(175, 0, 175), 127, '#af00af'],
[(175, 0, 215), 128, '#af00d7'],
[(175, 0, 255), 129, '#af00ff'],
[(175, 95, 0), 130, '#af5f00'],
[(175, 95, 95), 131, '#af5f5f'],
[(175, 95, 135), 132, '#af5f87'],
[(175, 95, 175), 133, '#af5faf'],
[(175, 95, 215), 134, '#af5fd7'],
[(175, 95, 255), 135, '#af5fff'],
[(175, 135, 0), 136, '#af8700'],
[(175, 135, 95), 137, '#af875f'],
[(175, 135, 135), 138, '#af8787'],
[(175, 135, 175), 139, '#af87af'],
[(175, 135, 215), 140, '#af87d7'],
[(175, 135, 255), 141, '#af87ff'],
[(175, 175, 0), 142, '#afaf00'],
[(175, 175, 95), 143, '#afaf5f'],
[(175, 175, 135), 144, '#afaf87'],
[(175, 175, 175), 145, '#afafaf'],
[(175, 175, 215), 146, '#afafd7'],
[(175, 175, 255), 147, '#afafff'],
[(175, 215, 0), 148, '#afd700'],
[(175, 215, 95), 149, '#afd75f'],
[(175, 215, 135), 150, '#afd787'],
[(175, 215, 175), 151, '#afd7af'],
[(175, 215, 215), 152, '#afd7d7'],
[(175, 215, 255), 153, '#afd7ff'],
[(175, 255, 0), 154, '#afff00'],
[(175, 255, 95), 155, '#afff5f'],
[(175, 255, 135), 156, '#afff87'],
[(175, 255, 175), 157, '#afffaf'],
[(175, 255, 215), 158, '#afffd7'],
[(175, 255, 255), 159, '#afffff'],
[(215, 0, 0), 160, '#d70000'],
[(215, 0, 95), 161, '#d7005f'],
[(215, 0, 135), 162, '#d70087'],
[(215, 0, 175), 163, '#d700af'],
[(215, 0, 215), 164, '#d700d7'],
[(215, 0, 255), 165, '#d700ff'],
[(215, 95, 0), 166, '#d75f00'],
[(215, 95, 95), 167, '#d75f5f'],
[(215, 95, 135), 168, '#d75f87'],
[(215, 95, 175), 169, '#d75faf'],
[(215, 95, 215), 170, '#d75fd7'],
[(215, 95, 255), 171, '#d75fff'],
[(215, 135, 0), 172, '#d78700'],
[(215, 135, 95), 173, '#d7875f'],
[(215, 135, 135), 174, '#d78787'],
[(215, 135, 175), 175, '#d787af'],
[(215, 135, 215), 176, '#d787d7'],
[(215, 135, 255), 177, '#d787ff'],
[(215, 175, 0), 178, '#d7af00'],
[(215, 175, 95), 179, '#d7af5f'],
[(215, 175, 135), 180, '#d7af87'],
[(215, 175, 175), 181, '#d7afaf'],
[(215, 175, 215), 182, '#d7afd7'],
[(215, 175, 255), 183, '#d7afff'],
[(215, 215, 0), 184, '#d7d700'],
[(215, 215, 95), 185, '#d7d75f'],
[(215, 215, 135), 186, '#d7d787'],
[(215, 215, 175), 187, '#d7d7af'],
[(215, 215, 215), 188, '#d7d7d7'],
[(215, 215, 255), 189, '#d7d7ff'],
[(215, 255, 0), 190, '#d7ff00'],
[(215, 255, 95), 191, '#d7ff5f'],
[(215, 255, 135), 192, '#d7ff87'],
[(215, 255, 175), 193, '#d7ffaf'],
[(215, 255, 215), 194, '#d7ffd7'],
[(215, 255, 255), 195, '#d7ffff'],
[(255, 0, 0), 196, '#ff0000'],
[(255, 0, 95), 197, '#ff005f'],
[(255, 0, 135), 198, '#ff0087'],
[(255, 0, 175), 199, '#ff00af'],
[(255, 0, 215), 200, '#ff00d7'],
[(255, 0, 255), 201, '#ff00ff'],
[(255, 95, 0), 202, '#ff5f00'],
[(255, 95, 95), 203, '#ff5f5f'],
[(255, 95, 135), 204, '#ff5f87'],
[(255, 95, 175), 205, '#ff5faf'],
[(255, 95, 215), 206, '#ff5fd7'],
[(255, 95, 255), 207, '#ff5fff'],
[(255, 135, 0), 208, '#ff8700'],
[(255, 135, 95), 209, '#ff875f'],
[(255, 135, 135), 210, '#ff8787'],
[(255, 135, 175), 211, '#ff87af'],
[(255, 135, 215), 212, '#ff87d7'],
[(255, 135, 255), 213, '#ff87ff'],
[(255, 175, 0), 214, '#ffaf00'],
[(255, 175, 95), 215, '#ffaf5f'],
[(255, 175, 135), 216, '#ffaf87'],
[(255, 175, 175), 217, '#ffafaf'],
[(255, 175, 215), 218, '#ffafd7'],
[(255, 175, 255), 219, '#ffafff'],
[(255, 215, 0), 220, '#ffd700'],
[(255, 215, 95), 221, '#ffd75f'],
[(255, 215, 135), 222, '#ffd787'],
[(255, 215, 175), 223, '#ffd7af'],
[(255, 215, 215), 224, '#ffd7d7'],
[(255, 215, 255), 225, '#ffd7ff'],
[(255, 255, 0), 226, '#ffff00'],
[(255, 255, 95), 227, '#ffff5f'],
[(255, 255, 135), 228, '#ffff87'],
[(255, 255, 175), 229, '#ffffaf'],
[(255, 255, 215), 230, '#ffffd7'],
[(255, 255, 255), 231, '#ffffff'],
[(8, 8, 8), 232, '#080808'],
[(18, 18, 18), 233, '#121212'],
[(28, 28, 28), 234, '#1c1c1c'],
[(38, 38, 38), 235, '#262626'],
[(48, 48, 48), 236, '#303030'],
[(58, 58, 58), 237, '#3a3a3a'],
[(68, 68, 68), 238, '#444444'],
[(78, 78, 78), 239, '#4e4e4e'],
[(88, 88, 88), 240, '#585858'],
[(98, 98, 98), 241, '#626262'],
[(108, 108, 108), 242, '#6c6c6c'],
[(118, 118, 118), 243, '#767676'],
[(128, 128, 128), 244, '#808080'],
[(138, 138, 138), 245, '#8a8a8a'],
[(148, 148, 148), 246, '#949494'],
[(158, 158, 158), 247, '#9e9e9e'],
[(168, 168, 168), 248, '#a8a8a8'],
[(178, 178, 178), 249, '#b2b2b2'],
[(188, 188, 188), 250, '#bcbcbc'],
[(198, 198, 198), 251, '#c6c6c6'],
[(208, 208, 208), 252, '#d0d0d0'],
[(218, 218, 218), 253, '#dadada'],
[(228, 228, 228), 254, '#e4e4e4'],
[(238, 238, 238), 255, '#eeeeee']
]


def get_256_code(code: int):
	return u"\u001b[38;5;" + str(code) + "m"

def add_cdata(CD: []):
	CD[1] = get_256_code(CD[1])
	return CD


_COLOR_DATA = map(lambda d: add_cdata(d), _COLOR_DATA_256)

PALETTE = [ [[(v/255.0)**2.2 for v in x[0]], x[1], x[2]] for x in _COLOR_DATA ]
CHARS_BY_DENSITY = ' .`-_\':,;^=+/"|)\\<>)iv%xclrs{*}I?!][1taeo7zjLunT#JCwfy325Fp6mqSghVd4EgXPGZbYkOA&8U$@KHDBWNMR0Q'

class Modes(Enum):
	C256 = "C256"
	ASCII = 'ASCII'
	TERMINAL = 'TERMINAL'
	HTML = 'HTML'
	HTML_TERMINAL = 'HTML_TERMINAL'

Back = colorama.Back

_colorama_is_init = False


class AsciiArt:
	def __init__(self, image: Image.Image):
		self._image = image

	def to_terminal(self, **kwargs):
		art = from_image(self._image, **kwargs)
		to_terminal(art)

	def to_html_file(self, path: str, mode: Modes = Modes.HTML, **kwargs):
		if mode != Modes.HTML and mode != Modes.HTML_TERMINAL:
			raise ValueError('Mode must be HTML or HTML_TERMINAL')

		art = from_image(self._image, mode=mode, **kwargs)
		to_html_file(path, art, **kwargs)

	def to_file(self, path: str, **kwargs):
		art = from_image(self._image, **kwargs)
		to_file(path, art)


def quick_test() -> None:
	to_terminal(from_url('https://source.unsplash.com/800x600?landscapes')) # type: ignore


# From URL
def _from_url(url: str) -> Image.Image:
	try:
		req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		with urllib.request.urlopen(req) as response:
			return Image.open(response)
	except urllib.error.HTTPError as e:
		raise e from None

def from_url(url: str, **kwargs) -> str:
	img = _from_url(url)
	return from_image(img, **kwargs)

def obj_from_url(url: str) -> AsciiArt:
	return AsciiArt(_from_url(url))


# From image file
def _from_image_file(img_path: str) -> Image.Image:
	return Image.open(img_path)


def from_image_file(img_path: str, **kwargs) -> str:
	img = _from_image_file(img_path)
	return from_image(img, **kwargs)


def obj_from_image_file(img_path: str) -> AsciiArt:
	return AsciiArt(_from_image_file(img_path))


# From clipboard
def _from_clipboard() -> Image.Image:
	try:
		from PIL import ImageGrab
		img = ImageGrab.grabclipboard()
	except (NotImplementedError, ImportError):
		img = from_clipboard_linux()

	if not img:
		raise OSError('The clipboard does not contain an image')

	return img


def from_clipboard_linux() -> Image.Image:
	try:
		import gi # type: ignore
		gi.require_version("Gtk", "3.0") # type: ignore
		from gi.repository import Gtk, Gdk # type: ignore
	except ModuleNotFoundError:
		print('Accessing the clipboard under Linux requires the PyGObject module')
		print('Ubuntu/Debian: sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0')
		print('Fedora: sudo dnf install python3-gobject gtk3')
		print('Arch: sudo pacman -S python-gobject gtk3')
		print('openSUSE: sudo zypper install python3-gobject python3-gobject-Gdk typelib-1_0-Gtk-3_0 libgtk-3-0')
		exit()

	clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

	try:
		buffer = clipboard.wait_for_image()
		data = buffer.get_pixels()
		w = buffer.props.width
		h = buffer.props.height
		stride = buffer.props.rowstride
	except:
		raise OSError('The clipboard does not contain an image')

	mode = 'RGB'
	img = Image.frombytes(mode, (w, h), data, 'raw', mode, stride)
	return img


def from_clipboard(**kwargs) -> str:
	img = _from_clipboard()
	return from_image(img, **kwargs)

def obj_from_clipboard() -> AsciiArt:
	return AsciiArt(_from_clipboard())


# From image
def from_image(img, columns=120, width_ratio=2.2, char=None, mode: Modes=Modes.TERMINAL, back: colorama.ansi.AnsiBack = None, debug=False, **kwargs) -> str:
	if mode not in Modes:
		raise ValueError('Unknown output mode ' + str(mode))

	img_w, img_h = img.size
	scalar = img_w*width_ratio / columns
	img_w = int(img_w*width_ratio / scalar)
	img_h = int(img_h / scalar)
	rgb_img = img.resize((img_w, img_h))
	color_palette = img.getpalette()

	grayscale_img = rgb_img.convert("L")

	chars = [char] if char else CHARS_BY_DENSITY

	if debug:
		rgb_img.save('rgb.jpg')
		grayscale_img.save('grayscale.jpg')

	lines = []
	for h in range(img_h):
		line = []

		for w in range(img_w):
			# get brightness value
			brightness = grayscale_img.getpixel((w, h)) / 255
			pixel = rgb_img.getpixel((w, h))
			# getpixel() may return an int, instead of tuple of ints, if the
			# source img is a PNG with a transparency layer
			if isinstance(pixel, int):
				pixel = (pixel, pixel, 255) if color_palette is None else tuple(color_palette[pixel*3:pixel*3 + 3])

			srgb = [ (v/255.0)**2.2 for v in pixel ]
			char = chars[int(brightness * (len(chars) - 1))]
			line.append(
				_build_char(char, srgb, brightness, mode)
			)

		if mode == Modes.TERMINAL and back:
			lines.append(back + line + colorama.Back.RESET)
		else:
			lines.append(line)

	if mode == Modes.TERMINAL:
		return '\n'.join(lines) + colorama.Fore.RESET

	elif mode == Modes.ASCII or mode == Modes.C256:

		for line in lines:
			for c in line:
				sys.stdout.write(c)
			print()
		# return '\n'.join(lines)
	elif mode == Modes.HTML or mode == Modes.HTML_TERMINAL:
		return '<br />'.join(lines)


def obj_from_image(img: Image.Image) -> AsciiArt:
	return AsciiArt(img)


def to_file(path: str, art: str) -> None:
	with open(path, 'w') as f:
		f.write(art)


def init_terminal() -> None:
	global _colorama_is_init
	if not _colorama_is_init:
		colorama.init()
		_colorama_is_init = True


def to_terminal(ascii_art: str) -> None:
	init_terminal()
	print(ascii_art)


def to_html_file(
	path: str,
	art: str,
	styles: str = 'display: inline-block; border-width: 4px 6px; border-color: black; border-style: solid; background-color:black; font-size: 8px;',
	additional_styles: str= '',
	auto_open: bool = False,
	**kwargs,
) -> None:
	html = f"""<!DOCTYPE html>
<head>
	<title>ASCII art</title>
	<meta name="generator" content="ASCII Magic {__VERSION__} - https://github.com/LeandroBarone/python-ascii_magic/" />
</head>
<body>
	<pre style="{styles} {additional_styles}">{art}</pre>
</body>
</html>"""
	with open(path, 'w') as f:
		f.write(html)
	if auto_open:
		webbrowser.open(path)


def _convert_color(rgb: list, brightness: float) -> dict:
	min_distance = 2
	index = 0

	for i in range(len(PALETTE)):
		tmp = [ v*brightness for v in PALETTE[i][0] ]
		distance = _L2_min(tmp, rgb)

		if distance < min_distance:
			index = i
			min_distance = distance

	return {
		'term': PALETTE[index][1],
		'hex-term': PALETTE[index][2],
		'hex': '#{:02x}{:02x}{:02x}'.format(*(int(c*200+55) for c in rgb)),
	}


def _L2_min(v1: list, v2: list) -> float:
    return (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2


def _build_char(char: str, srgb: list, brightness: float, mode: Modes = Modes.TERMINAL) -> str:
	color = _convert_color(srgb, brightness)

	if mode == Modes.C256:
		return color["term"] + char

	elif mode == Modes.TERMINAL:
		return color['term'] + char
	
	elif mode == Modes.ASCII:
		return char

	elif mode == Modes.HTML_TERMINAL:
		c = color['hex-term']
		return f'<span style="color: {c}">{char}</span>'

	elif mode == Modes.HTML:
		c = color['hex']
		return f'<span style="color: {c}">{char}</span>'
