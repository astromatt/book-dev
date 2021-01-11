************
About Docker
************


What is docker?
===============
* :cite:`DockerDocumentation`

.. figure:: ../_img/docker-vs-lxc.png
.. figure:: ../_img/docker-arch.png

.. figure:: ../_img/docker-stack-01-baremetal.png
.. figure:: ../_img/docker-stack-02-virtualization-1.png
.. figure:: ../_img/docker-stack-02-virtualization-2.png
.. figure:: ../_img/docker-stack-02-virtualization-3.png
.. figure:: ../_img/docker-stack-02-virtualization-4.png
.. figure:: ../_img/docker-stack-03-docker.png
.. figure:: ../_img/docker-stack-05-kubernetes.png
.. figure:: ../_img/docker-stack-06-architecture.png


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


.. figure:: ../_img/docker-layer-images.png
    :scale: 50%
    :align: center

    Layers

.. figure:: ../_img/docker-layers.png
    :scale: 50%
    :align: center

    Layers

.. figure:: ../_img/docker-container-layers.jpg
    :scale: 50%
    :align: center

    Container Layers

.. figure:: ../_img/docker-container-layers.png
    :scale: 50%
    :align: center

    Container Layers
