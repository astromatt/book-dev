***************
DevOps Workshop
***************

Author
======

:name: `Matt Harasymczuk <http://astrotech.io>`_
:email: `devops@astrotech.io <mailto:devops@astrotech.io>`_
:www: `http://www.astrotech.io <http://astrotech.io>`_
:facebook: `https://facebook.com/matt.harasymczuk <https://facebook.com/matt.harasymczuk>`_
:linkedin: `https://linkedin.com/in/mattharasymczuk <https://linkedin.com/in/mattharasymczuk>`_

Informacje o dokumencie i szkoleniu
===================================

.. tip:: Pamiętaj, że zawsze najbardziej aktualna wersja znajduje się na http://devops.astrotech.io

.. note:: Szkolenie obejmuje 32 godziny wykładów oraz warsztatów i pokrywa zagadnienia związane z ruchem i metodyką DevOps oraz praktyczną wiedzą na temat wykorzystania i zaadaptowania jej w nowoczesnych organizacjach IT. Uczestnik szkolenia opanuje używanie systemów i narzędzi DevOps m.in. Puppet, Docker, Vagrant oraz współpracę w duchu Agile.

.. warning::

    Minimalne wymagania sprzętowe:

    - 2 CPU Cores
    - 4 GB RAM
    - 10 GB free disk space

    Zalecane wymagania sprzętowe:

    - 4 CPU Cores
    - 8 GB RAM
    - 20 GB free disk space

    Oprogramowanie:

    - Najnowsza wersja Virtualbox
    - Najnowsza wersja Vagrant
    - Najnowsza wersja GIT
    - Najnowsza wersja Putty (jeżeli osoba korzysta z Windows)

    Po instalacji proszę o uruchomienie poleceń

    .. code-block:: sh

        vagrant init ubuntu/xenial64
        vagrant up --provider virtualbox

Wprowadzenie
============

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: Wprowadzenie

    wprowadzenie/program-szkolenia.rst
    wprowadzenie/wstep.rst
    wprowadzenie/agile-vs-devops.rst
    wprowadzenie/srodowisko-wirtualne.rst

Proces wytwarzania oprogramowania
=================================

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: Proces wytwarzania oprogramowania

    proces-wytwarzania-oprogramowania/wstep.rst
    proces-wytwarzania-oprogramowania/standardy-projektu.rst
    proces-wytwarzania-oprogramowania/wersjonowanie.rst
    proces-wytwarzania-oprogramowania/procesy-ci-cd.rst
    proces-wytwarzania-oprogramowania/standardy-pracy-zespolu.rst
    proces-wytwarzania-oprogramowania/jakosc-oprogramowania.rst
    proces-wytwarzania-oprogramowania/user-centered-design.rst
    proces-wytwarzania-oprogramowania/dobre-praktyki.rst
    proces-wytwarzania-oprogramowania/zarzadzanie-zmiana.rst
    proces-wytwarzania-oprogramowania/polityki-bezpieczenstwa.rst
    proces-wytwarzania-oprogramowania/manifest-agile.rst
    proces-wytwarzania-oprogramowania/scrum.rst
    proces-wytwarzania-oprogramowania/technologie.rst

Ekosystem narzędziowy
=====================

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: Ekosystem narzędziowy

    ekosystem-narzedziowy/index.rst
