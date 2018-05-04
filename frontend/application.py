from Tkinter import *
 
root = Tk()
 
freq = 1000
 
def playnote(event):
    canvas.focus_set()
    print "clicked at", event.x, event.y
    #Low D#
    if event.x < 50 and event.x > 0 and event.y < 298:
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(12, 160, text="Eb4", fill="#FFF")
    #F#
    if event.x < 216 and event.x > 156 and event.y < 298:
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(173, 160, text="Gb4", fill="#FFF")
    #G#
    if event.x < 306 and event.x > 245 and event.y < 298:
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(266, 160, text="Ab4", fill="#FFF")
    #A#
    if event.x < 405 and event.x > 345 and event.y < 298:
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        file="piano.mf.Bb4.wav"
        PlaySound(file, SND_FILENAME|SND_ASYNC)
        canvas.create_text(363, 160, text="Bb4", fill="#FFF")
    #C#
    if event.x < 590 and event.x > 532 and event.y < 298:
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(549, 160, text="Db4", fill="#FFF")
    #D#
    if event.x < 678 and event.x > 621 and event.y < 298:
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(641, 160, text="Eb5", fill="#FFF")
    #E
    if (event.x < 100 and event.x > 0 and event.y > 298 and event.y < 455) or \
        (event.x < 100 and event.x > 50 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(42, 360, text="E4", fill="#000")
    #F
    if (event.x < 187 and event.x > 100 and event.y > 298 and event.y < 455) or \
        (event.x < 155 and event.x > 100 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(125, 360, text="F4", fill="#000")
    #G
    if (event.x < 275 and event.x > 187 and event.y > 298 and event.y < 455) or \
        (event.x < 245 and event.x > 217 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(214, 360, text="G4", fill="#000")
    #A
    if (event.x < 372 and event.x > 275 and event.y > 298 and event.y < 455) or \
       (event.x < 345 and event.x > 307 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(306, 360, text="A4", fill="#000")
    #B
    if (event.x < 473 and event.x > 373 and event.y > 298 and event.y < 455) or \
        (event.x < 473 and event.x > 404 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(407, 360, text="B4", fill="#000")
    #C
    if (event.x < 560 and event.x > 474 and event.y > 298 and event.y < 455) or \
       (event.x < 532 and event.x > 474 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(503, 360, text="C4", fill="#000")
    #D
    if (event.x < 648 and event.x > 561 and event.y > 298 and event.y < 455) or \
       (event.x < 621 and event.x > 590 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(594, 360, text="D4", fill="#000")
    #E
    if (event.x < 729 and event.x > 650 and event.y > 298 and event.y < 455) or \
       (event.x < 729 and event.x > 678 and event.y < 455):
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(679, 360, text="E5", fill="#000")
        
 
def key(event):
    if repr(event.char)=="'q'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(12, 160, text="Eb4", fill="#FFF")
        
    if repr(event.char)=="'a'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(42, 360, text="E4", fill="#000")
        
    if repr(event.char)=="'s'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(125, 360, text="F4", fill="#000")
        
    if repr(event.char)=="'e'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(173, 160, text="Gb4", fill="#FFF")
        
    if repr(event.char)=="'d'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(214, 360, text="G4", fill="#000")
        
    if repr(event.char)=="'r'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(266, 160, text="Ab4", fill="#FFF")
        
    if repr(event.char)=="'f'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(306, 360, text="A4", fill="#000")
        
    if repr(event.char)=="'t'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(363, 160, text="Bb4", fill="#FFF")
        
    if repr(event.char)=="'g'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(407, 360, text="B4", fill="#000")
        
    if repr(event.char)=="'h'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(503, 360, text="C4", fill="#000")
        
    if repr(event.char)=="'u'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(549, 160, text="Db4", fill="#FFF")
        
    if repr(event.char)=="'j'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(594, 360, text="D4", fill="#000")
        
    if repr(event.char)=="'i'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(641, 160, text="Eb5", fill="#FFF")
        
    if repr(event.char)=="'k'":
        canvas.delete('all')
        canvas.create_image(0,0, image = pic1, anchor = NW)
        canvas.create_text(679, 360, text="E5", fill="#000")
 
    if repr(event.char)== "'m'":
        global freq
        freq = freq + 200
        print "frequency", freq
 
    if repr(event.char)== "'n'":
        global freq
        freq = freq - 200
        print "frequency", freq
 
    
pic1 = PhotoImage(file = 'keyboard03.gif')
 
frame = Frame(root, width=0, height=0)
frame.bind("<Key>", key)
frame.focus_set()
frame.pack()
        
    
canvas = Canvas(root, width = 740, height = 475, bg = 'yellow')    
canvas.pack(expand = YES, fill = BOTH)
canvas.create_image(0,0, image = pic1, anchor = NW)
canvas.bind("<Button-1>", playnote)
canvas.bind("<Key>", key)
canvas.bind("<Button-3>", Beep)
 
 
root.mainloop()