*****
C/C++
*****

Assignments
===========

Building c/c++ projects inside ``docker``
-----------------------------------------
#. Zainstaluj *Jenkins* za pomocą *Docker*
#. Zaciągnij repozytorium https://github.com/AstroTech/ecosystem-example-c
#. Budowanie ma odbywać się w kontenerze ``docker`` uruchamianym jako sibling
#. Dodaj job za pomocą Blue Ocean

    - apt update && apt install -y gcc libpcap-dev make
    - ./configure
    - make
    - make check
    - make install
