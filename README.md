# 🐤 Flappy Bird

*A Python remake of the classic Flappy Bird game using the tsapp library.*

---

## 🎯 Purpose / Problem Statement

- Replicate the classic Flappy Bird gameplay in Python  
- Provide a lightweight, educational game to demonstrate basic 2D physics, collision detection, and event handling  
- Address the need for a beginner-friendly example of game development in Python

## 👥 Target Audience

- Students: learning Python or game development  
- Hobbyist programmers: exploring 2D game mechanics  
- Gamers: interested in simple, casual browser-style games

## 🛠️ Solution + ⚠️ Limitations

**Solution:**  
- Implements core Flappy Bird mechanics:
    - High score:
    ```python

    if highest_score > 0:
          text.text = 'Highest Score: ' + str(highest_score) + '\nPress SPACE to start' #display highscore if high score is present
    else:
          text.text = 'Press SPACE to start' #display this text if high score is not present

    ```
    - Adding score:
    ```python
    if curr_sprites[1].x >= curr_pipes[i].x and curr_pipes[i] not in scored_pipes: #logic for scoring
        score += 1
        scored_pipes.append(curr_pipes[i]) #keep track of pipes that has been passed
    ```
    - Jump & gravity:
    ```python

    curr_sprites[1].y_speed += GRAVITY #make gravity

    ```
    - Background movement:
    ```python

    def move_bg(curr_sprites, SPEED): #funct to move spite then reset position
      '''
      Args:
          curr_sprites (obj): a sprite that's being used to be moved (background in this case)
          SPEED (int): a constant that store the speed of the sprite's movement (background in this case)
      '''
      curr_sprites.center_x -= SPEED
      if curr_sprites.x <= -curr_sprites.width / 2:
          curr_sprites.center_x += curr_sprites.width / 2

    ```
    - Scrolling pipes:
    ```python

    curr_pipes[i].x -= SPEED # move pipe
    if curr_pipes[i].x + curr_pipes[0].width <= 0: #logic to reuse out of bound pipes 
        pipe_y = random.randint(window.height // 2, window.height - PIPE_FLOOR_GAP)
        curr_pipes[i].x = window.width + 10
        curr_pipes[i].y = pipe_y #get random pipe vertical position
        scored_pipes.remove(curr_pipes[i]) #remove pipe from scored pipes since it needs to be considered a new pipe

    curr_pipes_top[i].x -= SPEED # move top pipe
    if curr_pipes_top[i].x + curr_pipes_top[0].width <= 0: #logic to reuse out of bound pipes
        curr_pipes_top[i].x = window.width + 10
        curr_pipes_top[i].y = pipe_y - curr_pipes_top[i].height - curr_sprites[1].height * 4 #use char's 4x height for gap between pipes 

    ```


- Uses the `tsapp` library for simplified rendering and input handling  

**Current Limitations:**  
- Only has a “press space” prompt and reset prompt  
- No on-screen GUI  
- Bird tilt logic not fully implemented  
- Gravity and jump power parameters need fine-tuning  
- No audio effects, pause/menu screens, or difficulty scaling

## 🔑 Key Features / Key Components

- 🌀 Game Loop: Frame-by-frame update of physics and rendering  
- 🕊️ Gravity & Jump Physics: Adjustable parameters for bird movement and pipe location  
- 💥 Collision Detection: Pipe and ground collisions end the game  
- 🌿 Procedural Pipe Generation: Randomized pipe gaps at fixed intervals that are reused everytime it passes the window  
- 🏆 Scoring System: Increment score each time the bird passes a pipe  

## ⚙️ Technical Challenges + 🌟 Future Plans

**Challenges Solved:**  
- Implementing smooth gravity vs. jump power balance  
- Optimizing gameplay to make it smoother by reusing pipes  
- Detecting precise collision boundaries between bird and pipes  

**Wishes / Future Additions:**  
- Fully-featured GUI overlay  
- Animated bird tilt based on vertical velocity  
- Sound effects and background music  
- Main menu and high-score persistence
- Difficulty scaling according to the score

## 🗓️ Project Timeline

- **Day 1:**  
  - Set up project structure, Implement bird physics, basic rendering loop, add scrolling background, and add pipe generation  
- **Day 2:**  
  - Integrate collision logic and optimize pipe generation  
- **Day 3:**  
  - Integrate scoring system, option to reset, and high score tracker  
- **Ongoing:**  
  - GUI enhancements, parameter tweaks, and animations

## 🧰 Tools and Resources Used

- **Programming Language:** Python 3.x  
- **Library:** [tsapp](https://github.com/cdent/tsapp), [random](https://www.geeksforgeeks.org/python-random-module/)  
- **References & Tutorials:**  
  - Official tsapp documentation  
  - Stack Overflow Q&A for collision detection tips and game optimization tips  
- **AI Assistance:** ChatGPT for optimization tips and debugging

---

## 🤝 Contributing

- Feel free to open issues or submit pull requests for any improvements—UI design, physics tweaks, or new features!
