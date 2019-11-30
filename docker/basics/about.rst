************
About Docker
************


What is docker?
===============
.. figure:: img/docker-vs-lxc.png
    :scale: 50%
    :align: center

    Docker vs LXC


Architecture
============
.. glossary::

    Guest
        Container running on Docker Engine

    Host
        Server running Docker Engine, see also :term:`Docker 0`

    Docker 0
        Server running Docker Engine


Docker image vs container
=========================
.. glossary::

    Image
        Ready to run Operating System with pre-installed software

    Container
        Running instance of an image

Layers
======
.. glossary::

    Layer
        Diff between outputs of Dockerfile ``RUN`` command while building an image


.. figure:: img/docker-layer-images.png
    :scale: 50%
    :align: center

    Layers

.. figure:: img/docker-layers.png
    :scale: 50%
    :align: center

    Layers

.. figure:: img/docker-container-layers.jpg
    :scale: 50%
    :align: center

    Container Layers

.. figure:: img/docker-container-layers.png
    :scale: 50%
    :align: center

    Container Layers
