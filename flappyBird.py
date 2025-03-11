#libary(ies)
import random
import tsapp

#var(s)
running = 0 #tracker to check if game is running
lose = 0 #win or lose tracker
score = 0 #score counter
score_added = 0 
SPEED = 8 #movement speed; if changed need to change PIPE_NUM
GRAVITY = 50 #gravity
JUMP_PWR = 500 #jumping power
PIPE_NUM = 2 #max number of pipes on screen; if changed need to change SPEED
PIPE_GAP = 900 / 3 #gap between pipes horizontally
PIPE_FLOOR_GAP = 105 #floor gap for pipe so pipe is not too low
FLOOR_GAP = 85 #gap between floor and window's bottom
show_bounds = False #turn bounds on or off

#collection(s)
sprite_files = ('flappyBirdBackground.jpg', 'flappyModel.png', 'marioPipe.png')
curr_sprites = [] #bg and char
curr_pipes = [] #bottom pipes
curr_pipes_top = [] #top pipes
scored_pipes = [] #pipes that has been passed

#function(s)
def move_bg(curr_sprites, SPEED): #funct to move spite then reset position
    curr_sprites.center_x -= SPEED
    if curr_sprites.x <= -curr_sprites.width / 2:
        curr_sprites.center_x += curr_sprites.width / 2

window = tsapp.GraphicsWindow(900, 487) #initiate window

#add sprites to window
for sprite in sprite_files:
    if sprite == sprite_files[2]: #avoid adding pipe to window
        pass
    else:
        sprite_obj = tsapp.Sprite(sprite, 0, 0, 1)
        window.add_object(sprite_obj)
        curr_sprites.append(sprite_obj)

#adjust sprites
curr_sprites[1].center = window.center #set char in the middle
curr_sprites[1].scale = 0.2 #set char scale
curr_sprites[1].show_bounds = show_bounds

#add pipes to window
for i in range(PIPE_NUM):
    pipe_y = random.randint(window.height // 2, window.height - PIPE_FLOOR_GAP) #get random pipe vertical position
    pipe = tsapp.Sprite(sprite_files[2], 0, pipe_y, 0.4) #create bottom pipe obj
    pipe.x = window.width + pipe.width * i + PIPE_GAP * i
    window.add_object(pipe) #add pipe to window
    curr_pipes.append(pipe) #track pipes
    pipe.show_bounds = show_bounds
    
    pipe = tsapp.Sprite(sprite_files[2], 0, 0, 0.4) #create top pipe obj
    pipe.x = window.width + pipe.width * i + PIPE_GAP * i
    pipe.y = pipe_y - pipe.height - curr_sprites[1].height * 4 #get random pipe vertical position then use char's 4x height for gap between pipes 
    pipe.flip_y = True
    pipe.show_bounds = show_bounds
    window.add_object(pipe) #add pipe to window
    curr_pipes_top.append(pipe) #track pipes

#add text to window
text = tsapp.TextLabel('PixelifySans-Regular.ttf', window.height / 10, 0, window.height * (1 / 5), window.width, 'Press SPACE to start', tsapp.WHITE)
text.align = 'center'
window.add_object(text) #add text to window

#main loop
while window.is_running:
    
    if not lose: #make sure bg stop moving
        move_bg(curr_sprites[0], SPEED) #move bg
        
    if tsapp.was_key_released(tsapp.K_SPACE): #logic for user to start game
        running = 1
        
    if lose:
        pass
        
    while running: #game loop
            
        curr_sprites[1].y_speed += GRAVITY #make gravity
        
        text.text = score
            
        if not lose: #make sure bg stop moving
            move_bg(curr_sprites[0], SPEED) #move bg
            
            if tsapp.was_key_released(tsapp.K_SPACE): #logic for jumping
                curr_sprites[1].y_speed = -JUMP_PWR
            
            for i in range(len(curr_pipes)):

                if curr_sprites[1].x >= curr_pipes[i].x and curr_pipes[i] not in scored_pipes: #logic for scoring
                    score += 1
                    scored_pipes.append(curr_pipes[i]) #keep track of pipes that has been passed

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

        for pipe, t_pipe in zip(curr_pipes, curr_pipes_top): #logic if player hit a pipe
            if curr_sprites[1].is_colliding_rect(pipe) or curr_sprites[1].is_colliding_rect(t_pipe):
                lose = 1
            
        if curr_sprites[1].y >= window.height - curr_sprites[1].height - FLOOR_GAP: #logic if character fell
            curr_sprites[1].y_speed = 0
            curr_sprites[1].y = window.height - curr_sprites[1].height - FLOOR_GAP
            running = 0
            lose = 1
        
        window.finish_frame() #make sure frame loop even in inner loop

    window.finish_frame()
    
'''
note:
- make game logic to reset if lose
- make UI for score, reset, first indicator to press space, etc
- make a function to determine bird's "tilt". if speed == 0 then tilt = 0. if speed == max then tilt = 90. if speed == gravity then tilt = -90
- tweak the gravity and jump pwr
'''