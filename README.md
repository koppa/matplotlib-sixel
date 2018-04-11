Matplotlib-sixel backend
========================

A matplotlib backend which outputs sixel graphics onto the terminal.
The code is inspired by the ipython-notebook matplotlib backend.


TODO:

* An Exception breaks the terminal
* Support other terminals than xterm
* Resize has still some problems.
  The figures are often too big for small windows

Dependencies
------------

* xterm with Sixel support configured
* imagemagick (for converting the graphics)
* matplotlib and numpy

Installation
-------------
    python setup.py install

Usage
-----


    import matplotlib
    matplotlib.use('module://matplotlib-sixel')
    from pylab import *
    plt.plot(sin(arange(100) / 10))
    show()

    # --> now shows the plot inside the xterm window
