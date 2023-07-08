import warnings
from pywinauto import findwindows, application
import time



class Install():
    def __init__(self):
        warnings.filterwarnings("ignore", category=UserWarning)

        # Get a list of all top-level windows
        windows = findwindows.find_windows()

        softs = []

        print('Current Running Applications:\n')

        # Print information about each window to the console
        i = 1
        for handle in windows:
            try:
                self.window = application.Application().connect(handle=handle)
                win = self.window.window(handle = handle)
                if len(win.texts()[0]) > 0:
                    softs.append([handle, win.texts()[0]])
                    print(str(i)+'- '+win.texts()[0])
                    i += 1
            except:
                # Ignore errors for windows that could not be connected to
                pass

        print('')

        appnum = int(input('Application Number: '))


        win = self.window.window(handle = softs[appnum-1][0])

        title = win.texts()[0]
        win.set_focus()

        # win.print_control_identifiers()
        self.click_btn(title=title, btn='NextButton')
        time.sleep(1)


        self.click_btn(title=title, btn='RepairButton')
        time.sleep(1)

        self.click_btn(title=title, btn='RepairButton')
        time.sleep(1)


        while True:
            windows = findwindows.find_windows()

            for handle in windows:
                if title == self.window.window(handle = handle).texts()[0]:
                    win = self.window.window(handle = handle)
                    break


            if not win['Progress'].exists():
                break
            
            # Wait a short time before checking again
            time.sleep(0.1)


        win['RepairButton'].click()


    def click_btn(self, title = '', btn = ''):
        windows = findwindows.find_windows()
        for handle in windows:
            if title == self.window.window(handle = handle).texts()[0]:
                win = self.window.window(handle = handle)
                break
            
        btn = win[btn]
        btn.click()

if __name__ == '__main__':
    test = Install()