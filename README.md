# Bad_Apple_On_Wikipedia

## Table of Contents

- [Overview](#overview)
- [Code Explanation](#code-explanation)
- [Tutorial on How to Recreate Bad Apple on Wikipedia](#tutorial-on-how-to-recreate-bad-apple-on-wikipedia)

## Overview

This Github repo contains the necessary code and tutorial on how to run Bad Apple visual as ASCII art on Wikipedia.

For the most part, this works a lot like my `Bad Apple On ChatGPT` project, which you can check out here: "https://github.com/ThatBobbyBoiz/Bad_Apple_ChatGPT".

## Code Explanation

The code for this project is divided into two parts:

### create_ascii_art.py

This Python code generates ASCII art of every frame of the Bad Apple video. It requires a full directory of extracted Bad Apple video frames (6571 frames to be exact).

### run_bad_apple_wikipedia.js

This JavaScript code fetches the ASCII art frames from your public GitHub repository and displays them on a specified text element on Wikipedia page. It requires a public GitHub repository with pre-generated Bad Apple frames and editing of the HTML code of the Wikipedia page (more information in the tutorial).

## Tutorial on How to Recreate Bad Apple on Wikipedia

Before starting, it's advised to have some basic coding knowledge. Also, keep in mind that this is how I achieved this, and there may be better and more optimized ways to do it.

1. Download the Bad Apple video and extract it into individual frames (around 6571 frames). You can use many online public code to do this, personally, I would recommend this one: https://pypi.org/project/videotoframes/. Save all the extracted frames in a directory (e.g., Bad Apple Frames).

2. Run the `create_ascii_art.py` code (remember to change the variable I specified in the code before running it) to convert all the Bad Apple frames into ASCII art and save them in a specified directory.

3. Upload all your ASCII art files to your personal GitHub repository and make them public.

4. Go to Bad Apple!! Wikipedia page (any Wikipedia page should work just fine).

5. Open Web Developer Tool, and go to the Inspector tab. Then select any text element (a text element should look like this `<p>Text Here</p>`), right-click the element, and choose "Edit as HTML". Then change the code of the selected text element to this:

```html
<p id="ascii_art_project" style="font-family:monospace; font-size: 9px;line-height: 9px;width: 680px"></p>
```

You can change the style of the text element depends on your need, but if you want to change, also make sure the ASCII frame will fit the text element area, otherwise it may cause some glitches when the visual is playing.

6. Now, go to the Console tab and paste the content of the `run_bad_apple_wikipedia.js` code (remember to change the variable I specified in the code) into the console. If pasting is disabled, you can try typing `allow pasting` into the console.

Now, the ASCII frame should be displayed on Wikipedia page. I recommend you wait until all the frames are fetched. When it's done fetching, click anywhere on the ASCII frame, and it should start playing (in a loop).
