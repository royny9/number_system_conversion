from tkinter import *
from PIL import Image as PilImage
from PIL import ImageTk as imGG


class Window:
    def __init__(self, width, height, title='convertation', resizble = (False, False), icon=None):
        #### main program
        self.color_bg = '#6d6c79'# const
        self.text_config = ('bahnschrift', 14)# const
        self.y = 32
        
        self.win = Tk()
        self.win.title(title)        
        self.win.geometry(f'{width}x{height}+200+200')
        self.win.resizable(resizble[0], resizble[1])
        self.win['bg'] = self.color_bg        
        #### icon check
        if icon:
            self.win.iconbitmap(icon)
        self.main_resault = ''
        img_button_rez = PilImage.open(r'E:\my brain\Новая папка\ButtonCalculate.png')
        img_button_rez = img_button_rez.resize((130,50), PilImage.ANTIALIAS)
        self.btn_rez_img =  imGG.PhotoImage(img_button_rez)
        
        img_button_clr = PilImage.open(r'E:\my brain\Новая папка\ButtonClear.png')
        img_button_clr = img_button_clr.resize((130,50), PilImage.ANTIALIAS)
        self.btn_clr_img =  imGG.PhotoImage(img_button_clr)
        
        # vigets    
        self.label_num = Label(self.win, text='Enter your num ',background=self.color_bg, font=self.text_config,justify=LEFT, anchor=W, pady=5, padx=5)
        self.button_col = Button(self.win, image=self.btn_rez_img,highlightthickness=0, bd=0,padx=5, pady=10, activebackground=self.color_bg ,command=self.conversion_to_number_system, background=self.color_bg)
        self.label_ss = Label(self.win, text='Enter before base ', bg=self.color_bg, font=self.text_config, anchor=W, pady=5, padx=5)
        self.entry_num = Entry(self.win,width=self.y, font=self.text_config)
        self.entry_ss = Entry(self.win, width=self.y, font=self.text_config)
        self.label_result = Text(self.win, width=40, bg='#3a3a49', font=self.text_config, padx=5, pady=5,borderwidth=1, height=1)
        self.button_clear = Button(self.win,text='clear', image=self.btn_clr_img,highlightthickness=0, bd=0,padx=5, pady=10, activebackground=self.color_bg, command=self.clear_all, background=self.color_bg)
        self.label_ss_1 = Label(self.win, text='Enter after base ', bg=self.color_bg, font=self.text_config,padx=5, pady=5, anchor=W)
        self.entry_ss_1 = Entry(self.win, width=self.y, font=self.text_config)
        self.label_useless = Label(self.win, text='ахаха а ты меня не видишь', bg=self.color_bg, fg=self.color_bg, font=self.text_config)
        self.label_useless_1 = Label(self.win, text='ахаха а ты меня не видишь', bg=self.color_bg, fg=self.color_bg, font=self.text_config)
    
    def drow_vidgets(self):# widget placement
        self.label_num.grid(column=0, row=0,rowspan=1)  
        self.entry_num.grid(column=1, row=0, columnspan=2, rowspan=1)
        self.label_ss.grid(column=0, row=1,rowspan=1)
        self.entry_ss.grid(column=1, row=1, columnspan=2, rowspan=1)
        self.button_col.grid(column=0, row=4) 
        self.label_result.grid(column=0,row=6, columnspan=3)
        self.button_clear.grid(column=2, row=4)
        self.label_ss_1.grid(column=0, row=2,rowspan=1)
        self.entry_ss_1.grid(column=1, row=2, columnspan=2,rowspan=1)
        self.label_useless.grid(column=0, row=5, columnspan=2)
        self.label_useless_1.grid(column=0, row=3, columnspan=2)
 
    def clear_all(self):  # clear enrey_ss, entry_num, label_result
        self.entry_num.delete(0, END)
        self.entry_ss.delete(0, END)
        self.label_result.delete(0.0, 'end')
        self.entry_ss_1.delete(0, END)
        self.main_resault = ''
  
    def conversion_to_number_system(self):
        self.label_result.delete(0.0, 'end')
        num = self.entry_num.get().replace(' ', '')
        after_ss = self.entry_ss_1.get().replace(' ', '')
        before_ss = self.entry_ss.get().replace(' ', '')
        
        if int(after_ss) != 10 and int(before_ss) != 10:
            self.resault_other_to_other = ''
            int_after_ss = int(after_ss)
            int_befor_ss = int(before_ss)
            num_other_ten = int(num, int_befor_ss)
            
            
            # internal variables for translation
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsuvwxyz"
            
            # verification of the correctness of the number system
            if int_after_ss == 0 or int_befor_ss == 0 or int_after_ss > 63:
                self.label_result.insert(0.0, 'не надо так делать ')
            
            # translation cycle up to 62 bases
            while num_other_ten > 0:
                vn_convertor = num_other_ten % int_after_ss
                self.resault_other_to_other = digits[vn_convertor] + self.resault_other_to_other
                num_other_ten //= int_after_ss
            self.main_resault = self.resault_other_to_other
            
        
        
        if int(before_ss) == 10: # transfer and from 10 to another
            
            # internal variables for translation
            internal_number = int(num)
            internal_base = int(after_ss)
            before_base = int(before_ss)
            resault_ten_to_other = ''
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrsuvwxyz"
            
            # verification of the correctness of the number system
            if internal_base == 0 or before_base == 0 or internal_base > 63:
                self.label_result.insert(0.0, 'не надо так делать ')
            
            # translation cycle up to 62 bases
            while internal_number > 0:
                vn_convertor = internal_number % internal_base
                resault_ten_to_other = digits[vn_convertor] + resault_ten_to_other
                internal_number //= internal_base
            self.main_resault = resault_ten_to_other    
            
        if int(before_ss) != 10 and int(after_ss) == 10: # translation and another at 10
            resault_other_to_10 = int(num, int(before_ss))
            self.main_resault = resault_other_to_10
        self.label_result.insert(0.0, self.main_resault) # result output       

    
    def run(self):   # run program
        self.drow_vidgets()
        self.win.mainloop()
        


    
if __name__ == '__nmain__':
    window = Window(500, 280)
    window.run()        