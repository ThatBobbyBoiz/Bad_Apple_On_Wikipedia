import os
from PIL import Image

# Define ASCII characters to use
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Set input and output directory paths
input_dir = "frames/" #change this
output_dir = "ascii_frames/" #change this

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Get a list of all frame files in the input directory and sort them in alphanumeric order
frame_files = os.listdir(input_dir)
frame_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

# Loop through each frame file and convert to ASCII art
for i, frame_file in enumerate(frame_files):
    # Open frame file as an image
    frame_path = os.path.join(input_dir, frame_file)
    frame_image = Image.open(frame_path)

    # Resize image to fit in the terminal window
    width, height = frame_image.size
    aspect_ratio = height / width
    new_width = 140                                      # Don't know why I wrote my code so dumb like below, but well it works
    new_height = int(aspect_ratio * new_width * 0.244)   # You may change the new_height and new_width depends on your need
    if new_height != 60:                                 # Note: if you change the new_height and new_width value, you may need to change
        new_height = 60                                  # the text element's style on Wikipedia page to make the visual looks fit
        if new_width != 140:                             # These default value will work just fine 
            new_width = 140
    resized_image = frame_image.resize((new_width, new_height))

    # Convert image to grayscale and get pixel data
    grayscale_image = resized_image.convert("L")
    pixels = grayscale_image.getdata()

    # Generate ASCII art from pixel data
    ascii_frame = ""
    for j, pixel in enumerate(pixels):
        if j % new_width == 0 and j != 0:
            ascii_frame += "\n"
        ascii_frame += ascii_chars[pixel // 25]
    
    # Save ASCII art as a text file
    output_path = os.path.join(output_dir, f"frame{i:03}.txt")
    with open(output_path, "w") as file:
        file.write(ascii_frame)
