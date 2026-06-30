from PIL import Image, ImageDraw, ImageFont
import io
import os
from colors import ColorUtils

class ImageGenerator:
    @staticmethod
    def create_palette_image(colors, width=800, height=200, title="Color Palette"):
        """Create an image showing a color palette"""
        try:
            # Create image
            img = Image.new('RGB', (width, height + 80), color='white')
            draw = ImageDraw.Draw(img)
            
            # Calculate color block width
            block_width = width // len(colors)
            
            # Draw color blocks
            for i, color in enumerate(colors):
                x1 = i * block_width
                x2 = (i + 1) * block_width
                draw.rectangle([x1, 40, x2, height + 40], fill=color)
                
                # Draw color code
                try:
                    draw.text((x1 + 5, height + 50), color, fill='black')
                except:
                    pass
            
            # Add title
            try:
                draw.text((10, 10), title, fill='black')
            except:
                pass
            
            # Save to bytes
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            return img_byte_arr
        except Exception as e:
            print(f"Error creating palette image: {e}")
            return None
    
    @staticmethod
    def create_color_preview(hex_color, size=300):
        """Create a preview image of a single color"""
        try:
            img = Image.new('RGB', (size, size), color=hex_color)
            draw = ImageDraw.Draw(img)
            
            # Add color info
            color_info = ColorUtils.get_color_info(hex_color)
            text = f"{color_info['name']}\n{hex_color}\nRGB{color_info['rgb']}"
            
            # Check if color is dark for text color
            rgb = ColorUtils.hex_to_rgb(hex_color)
            brightness = (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000
            text_color = 'white' if brightness < 128 else 'black'
            
            try:
                draw.text((10, 10), text, fill=text_color)
            except:
                pass
            
            # Save to bytes
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            
            return img_byte_arr
        except Exception as e:
            print(f"Error creating color preview: {e}")
            return None
