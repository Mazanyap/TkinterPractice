"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Alex Mazany.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """

    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()


    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    conditional_hello = ttk.Button(frame1, text='Ok?')
    conditional_hello['command'] = (lambda:
                                     hello_or_goodbye(my_entry_box))
    conditional_hello.grid()

    cool_entry_box = ttk.Entry(frame1)
    cool_entry_box.grid()

    stringer = ttk.Button(frame1, text='stringulate')
    stringer['command'] = (lambda:
                                    string_repeater(my_entry_box, cool_entry_box))
    stringer.grid()

    print_stuff_button = ttk.Button(frame1, text='Say Hello')
    print_stuff_button['command'] = (lambda:
                                     Say_Hello())
    print_stuff_button.grid()

    print_stuff_button = ttk.Button(frame1, text='Do NOT')
    print_stuff_button['command'] = (lambda:
                                     secret())
    print_stuff_button.grid()

    root.mainloop()


def Say_Hello():
    print('Hello')


def hello_or_goodbye(my_entry_box):
    contents_of_entry_box = my_entry_box.get()
    if contents_of_entry_box == 'ok':
        print('Hello')
    else:
        print('Goodbye')


def string_repeater(my_entry_box, cool_entry_box):
    string = my_entry_box.get()
    n = int(cool_entry_box.get())
    for k in range(n):
        print(string)


def secret():
    while True:
        print('$')


    # ------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # ------------------------------------------------------------------
    # Done: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
