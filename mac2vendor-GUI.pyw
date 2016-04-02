from Tkinter import *


class GUI(Frame):

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.parent.title("Mac to Vendor")
        self.centerWindow()
        self.setUi()

    def setUi(self):
        lbl = Label(self.parent,text="Enter MAC")
        lbl.pack()
        self.txt_mac = Entry(self.parent,width="20",justify="center")
        self.txt_mac.bind("<Return>",self.check)
        self.txt_mac.pack()
        Entry.focus_set(self.txt_mac)
        self.result = StringVar()
        self.lbl_result = Label(self.parent,text="")
        self.lbl_result.pack()

    def centerWindow(self):
        w = 150; h = 100

        self.parent.maxsize(500,300)
        self.parent.minsize(240,90)

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw-w)/2
        y = (sh-h)/2
        self.parent.geometry("%dx%d+%d+%d" % (w,h,x,y))

    def check(self,*args):

        macinput = self.txt_mac.get()
        macObj = mac(macinput)
        if macObj.valid_mac != True:
            result = "Error in Mac Address"
        else:
            result = macObj.result
        self.lbl_result.config(text=result)



class mac:
    def __init__(self,addr):
        self.addr = str(addr.replace(":","")[:6]).upper()
        self.valid_mac = True
        mac_keymap = "0123456789ABCDEF"

        for value in self.addr:
            if value not in mac_keymap:
                valid_mac = False
                break

        if self.valid_mac:
            self.result = "Mac Not Found"
            with open("mac-oui.db","r") as db:
                data = db.readlines()

            for row in data:
                if self.addr == row[:6]:
                    self.result = row[7:]
                    break

if __name__ == "__main__":
    root = Tk()
    win = GUI(root)
    root.mainloop()
