try:
    from Tkinter import Tk, Frame, BOTH, Label, PhotoImage
except ImportError:
    from tkinter import Tk, Frame, BOTH, Label, PhotoImage
import simpleaudio as sa
import time as t
import random

KEYS_TO_NOTES = {
    1: 'C1',
    2: 'D1',
    3: 'E1',
    4: 'C#1',
    5: 'D#1',
}


keys = [
            [0, 'C1'],
            [35, 'C#1'],
            [50, 'D1'],
            [85, 'D#1'],
            [100, 'E1'],
        ]

def find_label(name, array):
    for x in range(len(array)):
        if name == array[x][1]:
            return array[x][2]


def key_pressed(key):
    note = KEYS_TO_NOTES.get(key, None)
    if note:
        if len(note) == 2:
            img = 'pictures/white_key_pressed.gif'
        else:
            img = 'pictures/black_key_pressed.gif'
        key_img = PhotoImage(file=img)
        label=find_label(note, keys)


        def key_released():
            note = KEYS_TO_NOTES.get(key, None)
            if note:
                if len(note) == 2:
                    img = 'pictures/white_key.gif'
                else:
                    img = 'pictures/black_key.gif'
                key_img = PhotoImage(file=img)
                label.configure(image=key_img)
                label.image = key_img
        

        label.configure(image=key_img)
        label.image = key_img
        label.after(250,key_released)

        

        wave_obj = sa.WaveObject.from_wave_file('sounds/' + note + '.wav')
        wave_obj.play()
        print(note)

def start(some):
    ans =str(random.randint(0,1))+str(random.randint(0,1))+str(random.randint(0,1))+str(random.randint(0,1))+str(random.randint(0,1))
    print(ans)
    for i in range(len(ans)):
        if(ans[i]=='1'):
            key_pressed(i+1)

class Piano(Frame):

    def __init__(self, parent):

        Frame.__init__(self, parent, background='SkyBlue3')

        self.parent = parent

        self.init_user_interface()

    def init_user_interface(self):

        for key in keys:
            if len(key[1]) == 2:
                img = 'pictures/white_key.gif'
                key.append(self.create_key(img, key))
            
        for key in keys:
            if len(key[1]) > 2:
                img = 'pictures/black_key.gif'
                key.append(self.create_key(img, key))

        self.parent.title('The Piano')

        w = 150
        h = 200
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.parent.bind('1', start)
        
        self.pack(fill=BOTH, expand=1)

    def create_key(self, img, key):
        key_image = PhotoImage(file=img)
        label = Label(self, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=0)
        label.name = key[1]
        return label


def main():
    root = Tk()
    app = Piano(root)
    app.mainloop()

if __name__ == '__main__':
    main()