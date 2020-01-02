.. Glow documentation master file, created by
   sphinx-quickstart on Mon Nov  4 05:15:19 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Glow's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Application Design
==================

.. mermaid::

    graph LR;
        G{Glow}
        G --> DM[DisplayManager]
        DM --> GS[GlowStrip]
        GS --> GE[GlowEffect]


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
