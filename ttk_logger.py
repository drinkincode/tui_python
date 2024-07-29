import TermTk as ttk

root = ttk.TTk()

    # Create a window and attach it to the root (parent=root)
logWin = ttk.TTkWindow(parent=root,pos = (1,1), size=(80,20), title="LogViewer Window", border=True, layout=ttk.TTkVBoxLayout())

    # Attach the logViewer widget to the window
ttk.TTkLogViewer(parent=logWin)

    # Push some Debug messages
ttk.TTkLog.info(    "Test Info Message")
ttk.TTkLog.debug(   "Test Debug Message")
ttk.TTkLog.error(   "Test Error Message")
ttk.TTkLog.warn(    "Test Warning Message")
ttk.TTkLog.critical("Test Critical Message")
ttk.TTkLog.fatal(   "Test Fatal Message")

    # Start the Main loop
root.mainloop()