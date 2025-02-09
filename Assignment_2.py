def setup():
    size(300,241) 
    img = load_image("https://upload.wikimedia.org/wikipedia/en/2/27/Bliss_%28Windows_XP%29.png") # calling on web for background image
    background(img) # setting Bliss image as background
    

# making the house variable
    global house   
    house = create_shape(GROUP)
    
    base = create_shape(RECT,30,150,50,50,5)
    base.set_fill('#33ffd1')
    roof = create_shape(TRIANGLE,55,120,25,150,85,150)
    roof.set_fill('#f44d0a')
        
    house.add_child(base)
    house.add_child(roof)
        
                                                   

# making the dog variable
    global dog
    dog = create_shape (GROUP)
 
    fill('#f4bb0a')
    body = create_shape(ELLIPSE,230,130,40,15)
    head = create_shape(ELLIPSE,210,120,20,20)
    l_ear = create_shape(ELLIPSE,200,110,15,10)
    r_ear = create_shape(ELLIPSE,220,110,15,10)
    f_leg = create_shape(RECT,215,135,5,15,7)
    b_leg = create_shape(RECT,240,135,5,15,7)
    tail = create_shape(RECT,248,125,10,3,12)
    
    dog.add_child(body)
    dog.add_child(head)
    dog.add_child(l_ear)
    dog.add_child(r_ear)
    dog.add_child(f_leg)
    dog.add_child(b_leg)
    dog.add_child(tail)





def draw():

# assigning a random shape to be drawn - house or dog
    words = [house,dog]
    word = random_choice(words)
    shape(word)
    
no_loop()
    
run_sketch()
