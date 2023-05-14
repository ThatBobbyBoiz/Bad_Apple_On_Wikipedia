{
  const startFrame = //num1;  //change this
  const endFrame = //num2;  //change this
  const asciiBox = document.getElementById("ascii_art_project");
  let currentFrame = 0;
  let asciiFrames = [];

  // Load all ASCII frames from the GitHub repository
  const loadAsciiFrames = async () => {
    try {
      for (let i = startFrame; i <= endFrame; i++) {
        const frameNumber = i.toString().padStart(3, '0');
        const frameURL = `https://raw.githubusercontent.com/username/repo/main/ascii_frames/frame${frameNumber}.txt`; //change this part "username/repo/main/ascii_frames"
        const response = await fetch(frameURL);
        const data = await response.text();
        asciiFrames.push(data);
        if (i === startFrame) {
          asciiBox.innerHTML = asciiFrames[0];
        }
        await new Promise(resolve => setTimeout(resolve, 400)); 
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Load and display the next ASCII frame
  const loadAsciiFrame = () => {
    currentFrame = (currentFrame + 1) % asciiFrames.length;
    asciiBox.innerHTML = asciiFrames[currentFrame];
  };

  // Add event listener to the ASCII box to start the animation
  asciiBox.addEventListener('click', () => {
    setInterval(loadAsciiFrame, 1000/30); // the visual may not run at the exact 30 fps
  });

  // Load all ASCII frames and start the animation
  loadAsciiFrames();
}
