Matplotlib-sixel backend
========================

A matplotlib backend which outputs sixel graphics onto the terminal


TODO:

* finish readme (links etc)
* cleanup code
* proper install file
* Check for xterm at start.
  Currently only shows a exception because of curses (in some cases).
  Also check terminal mode, whether sixel support is there
* Resize has still some problems.
  The figures are often too big for small windows

Dependencies
------------

* xterm with Sixel support configured
* imagemagick (for converting the graphics)
* matplotlib and numpy

Usage
-----


    from pylab import *
    matplotlib.use('module://matplotlib-sixel')
    plt.plot(sin(arange(100) / 10))
    show()

    # --> now shows the plot inside the xterm window
