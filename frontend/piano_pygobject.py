# Run tkinter code in another thread

from tkinter import Tk, Frame, BOTH, Label, PhotoImage
import threading
import time
import random

my_val = 0


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

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def get_value(self):
        global my_val
        label = Label(self.root, text=my_val)
        my_val += 1
        label['text'] = my_val
        label.pack()
        self.root.after(10, self.get_value)

    def find_label(self, name, array):
        for x in range(len(array)):
            if name == array[x][1]:
                return array[x][2]


    def key_pressed(self, key):
        note = KEYS_TO_NOTES.get(key, None)
        if note:
            if len(note) == 2:
                img = 'pictures/white_key_pressed.gif'
            else:
                img = 'pictures/black_key_pressed.gif'
            key_img = PhotoImage(file=img)
            label = self.find_label(note, keys)


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

    def start(self):
        ans =str(random.randint(0,1))+str(random.randint(0,1))+str(random.randint(0,1))+str(random.randint(0,1))+str(random.randint(0,1))
        print(ans)
        for i in range(len(ans)):
            if(ans[i]=='1'):
                note = KEYS_TO_NOTES.get(i+1, None)
                if len(note) == 2:
                    img = 'pictures/white_key_pressed.gif'
                else:
                    img = 'pictures/black_key_pressed.gif'
                key_img = PhotoImage(file=img)
                self.key_pressed(i+1)

    def init_user_interface(self):

        for key in keys:
            if len(key[1]) == 2:
                # img = 'pictures/white_key.gif'
                key.append(self.create_key(key))
            
        for key in keys:
            if len(key[1]) > 2:
                # img = 'pictures/black_key.gif'
                key.append(self.create_key(key))

        self.root.title('The Piano')

        w = 150
        h = 200
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.bind()
        
        # self.pack(fill=BOTH, expand=1)

    def create_key(self, img, key):
        # key_image = PhotoImage(file=img)
        label = Label(self.root, image=key_image, bd=0)
        label.image = key_image
        label.place(x=key[0], y=0)
        label.name = key[1]
        return label

    def run(self):
        self.root = Tk()
        self.init_user_interface()
        # self.root.after(0, self.start)
        # self.root.after(10, self.get_value)
        self.root.mainloop()


app = App()
print('Now we can continue running code while mainloop runs!')

