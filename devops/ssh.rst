SSH
===

Instalacja klienta
------------------
#. Zainstaluj klient SSH

    * Windows np. w instalatorze `GIT` - https://git-scm.org/download
    * Linux np. za pomocą `apt-get`
    * macOS np. za pomocą `brew` lub `XCode`)

#. Uruchom terminal (np. `Git Bash`)
#. Sprawdź wersję `SSH` i wpisz w komórkę w arkuszu kalkulacyjnym

    .. code-block:: console

        $ ssh -V
        OpenSSH_8.1p1

Klucz Prywatny
--------------
#. Pobierz klucz `.pem` podany przez prowadzącego i zapisz go na pulpicie jako `szkolenie.pem`
#. Poniższe polecenie wykonaj tylko dla `Linux` albo `macOS` (dla `Windows` nie trzeba):

    .. code-block:: console

        $ chmod 400 ~/Desktop/szkolenie.pem

Konfiguracja SSH
----------------
#. Edytuj plik ``~/.ssh/config``

    .. code-block:: console

        $ vim ~/.ssh/config

#. Przejście do trybu edycji klawisz `a`
#. Wpisz treść:

    .. code-block:: text

        Host aws
            Hostname <TWOJE-IP>
            User ubuntu
            Port 22
            IdentityFile ~/Desktop/szkolenie.pem
            ServerAliveInterval 240

#. Zwróć uwagę na wcięcia
#. W miejsce <TWOJE-IP> wpisz adres, który nadał Ci prowadzący
#. Aby zapisać i wyjść wciśnij klawisz `Esc` a później `:wq`

Połączenie
----------
#. Połącz się do swojej maszyny w Cloud

    .. code-block:: console

        $ ssh aws
        Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-1029-aws x86_64)

         * Documentation:  https://help.ubuntu.com
         * Management:     https://landscape.canonical.com
         * Support:        https://ubuntu.com/advantage

          System information as of Tue Dec 22 17:31:49 UTC 2020

          System load:                      0.0
          Usage of /:                       68.9% of 7.69GB
          Memory usage:                     22%
          Swap usage:                       0%
          Processes:                        131
          Users logged in:                  0
          IPv4 address for br-2e3914befcfc: 172.18.0.1
          IPv4 address for docker0:         172.17.0.1
          IPv4 address for eth0:            172.31.15.93

         * Introducing self-healing high availability clusters in MicroK8s.
           Simple, hardened, Kubernetes for production, from RaspberryPi to DC.

             https://microk8s.io/high-availability

        49 updates can be installed immediately.
        8 of these updates are security updates.
        To see these additional updates run: apt list --upgradable


        3 updates could not be installed automatically. For more details,
        see /var/log/unattended-upgrades/unattended-upgrades.log

        *** System restart required ***
        Last login: Tue Dec 22 08:51:57 2020 from 46.204.21.113
        ubuntu@ip-172-31-15-93:~$

#. Sprawdź na jakiego użytkownika jesteś zalogowany/zalogowana

    .. code-block:: console

        $ whoami
        ubuntu
