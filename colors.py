import colorsys
import random

class ColorUtils:
    # Predefined color palettes
    PALETTES = {
        'monochrome': ['#000000', '#333333', '#666666', '#999999', '#CCCCCC', '#FFFFFF'],
        'pastel': ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF', '#E8BAFF'],
        'vibrant': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'],
        'earth': ['#8B4513', '#A0522D', '#D2691E', '#CD853F', '#DEB887', '#F5DEB3'],
        'ocean': ['#006994', '#0077B6', '#00B4D8', '#90E0EF', '#CAF0F8', '#E0F7FA'],
        'sunset': ['#FF512F', '#DD2475', '#FF6B6B', '#FECA57', '#FF9FF3', '#54A0FF'],
        'forest': ['#228B22', '#32CD32', '#006400', '#8FBC8F', '#2E8B57', '#3CB371'],
        'neon': ['#FF00FF', '#00FFFF', '#FF0000', '#00FF00', '#FFFF00', '#FF4500'],
        'retro': ['#F4A460', '#FFD700', '#DC143C', '#00CED1', '#FF69B4', '#7B68EE'],
        'winter': ['#E8F4F8', '#B8D8E3', '#A8D5E2', '#7EC8E3', '#5BA3C9', '#3A7CA5'],
    }
    
    # Color names mapping
    COLOR_NAMES = {
        '#FF0000': 'Red',
        '#00FF00': 'Green',
        '#0000FF': 'Blue',
        '#FFFF00': 'Yellow',
        '#FF00FF': 'Magenta',
        '#00FFFF': 'Cyan',
        '#000000': 'Black',
        '#FFFFFF': 'White',
        '#808080': 'Gray',
        '#800000': 'Maroon',
        '#808000': 'Olive',
        '#008000': 'Dark Green',
        '#800080': 'Purple',
        '#008080': 'Teal',
        '#000080': 'Navy',
        '#FFA500': 'Orange',
        '#FFC0CB': 'Pink',
        '#A52A2A': 'Brown',
        '#FFD700': 'Gold',
        '#C0C0C0': 'Silver',
    }
    
    @staticmethod
    def hex_to_rgb(hex_color):
        """Convert hex color to RGB tuple"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(rgb):
        """Convert RGB tuple to hex color"""
        return '#{:02x}{:02x}{:02x}'.format(*rgb)
    
    @staticmethod
    def get_color_name(hex_color):
        """Get color name from hex code"""
        return ColorUtils.COLOR_NAMES.get(hex_color.upper(), 'Custom Color')
    
    @staticmethod
    def generate_palette(count=5, palette_type='random'):
        """Generate a color palette"""
        if palette_type in ColorUtils.PALETTES:
            palette = ColorUtils.PALETTES[palette_type]
            if len(palette) >= count:
                return random.sample(palette, count)
            return palette + random.sample(ColorUtils.PALETTES['vibrant'], count - len(palette))
        else:
            # Generate random palette
            palette = []
            for _ in range(count):
                hue = random.random()
                saturation = random.uniform(0.5, 1.0)
                lightness = random.uniform(0.3, 0.7)
                rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
                hex_color = ColorUtils.rgb_to_hex(tuple(int(c * 255) for c in rgb))
                palette.append(hex_color)
            return palette
    
    @staticmethod
    def complementary_color(hex_color):
        """Get complementary color"""
        rgb = ColorUtils.hex_to_rgb(hex_color)
        comp_rgb = tuple(255 - c for c in rgb)
        return ColorUtils.rgb_to_hex(comp_rgb)
    
    @staticmethod
    def analogous_colors(hex_color, count=3):
        """Get analogous colors"""
        rgb = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = colorsys.rgb_to_hls(*[c/255 for c in rgb])
        
        colors = []
        for i in range(count):
            hue = (h + i * 0.0833) % 1.0
            rgb_color = colorsys.hls_to_rgb(hue, l, s)
            hex_color = ColorUtils.rgb_to_hex(tuple(int(c * 255) for c in rgb_color))
            colors.append(hex_color)
        return colors
    
    @staticmethod
    def triadic_colors(hex_color):
        """Get triadic colors"""
        rgb = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = colorsys.rgb_to_hls(*[c/255 for c in rgb])
        
        colors = []
        for i in range(3):
            hue = (h + i * 0.3333) % 1.0
            rgb_color = colorsys.hls_to_rgb(hue, l, s)
            hex_color = ColorUtils.rgb_to_hex(tuple(int(c * 255) for c in rgb_color))
            colors.append(hex_color)
        return colors
    
    @staticmethod
    def tetradic_colors(hex_color):
        """Get tetradic colors"""
        rgb = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = colorsys.rgb_to_hls(*[c/255 for c in rgb])
        
        colors = []
        for i in range(4):
            hue = (h + i * 0.25) % 1.0
            rgb_color = colorsys.hls_to_rgb(hue, l, s)
            hex_color = ColorUtils.rgb_to_hex(tuple(int(c * 255) for c in rgb_color))
            colors.append(hex_color)
        return colors
    
    @staticmethod
    def get_color_info(hex_color):
        """Get detailed information about a color"""
        rgb = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = colorsys.rgb_to_hls(*[c/255 for c in rgb])
        
        return {
            'hex': hex_color,
            'rgb': rgb,
            'hsl': (int(h * 360), int(s * 100), int(l * 100)),
            'name': ColorUtils.get_color_name(hex_color),
            'complementary': ColorUtils.complementary_color(hex_color)
        }
