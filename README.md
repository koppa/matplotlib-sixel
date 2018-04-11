Matplotlib-sixel backend
========================

A matplotlib backend which outputs sixel graphics onto the terminal.
The code is inspired by the ipython-notebook matplotlib backend.


TODO:

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


    from pylab import *
    matplotlib.use('module://matplotlib-sixel')
    plt.plot(sin(arange(100) / 10))
    show()

    # --> now shows the plot inside the xterm window
