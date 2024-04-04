Przygotowanie
=============


Informacje dla wykonującego
---------------------------
Rsync można robić na stojących i działających instancjach po obu stronach,
tj. jira.example.com i jira.cloud.example.com, ale... Nigdy nie wiadomo co może
się stać (indeksowanie, cache, crony itp) i coś może się wysypać.

Rsynców katalogów domowych Postgresa bez kładzenia kontenerów w cloud bym
nie próbował. Bazy danych generalnie trzymają dużo rzeczy w pamięci i do
pliku zapisują rzadziej. Jeżeli trafi się na taką sytuację to można
stracić spójność danych. Podmienianie im plików w locie może (ale nie
musi) skończyć się źle. Natomiast nie warto, bo położenie kontenera rsync
i uruchomienie to dwie minuty, a prawdopodobieństwo zniszczenia danych
znacznie mniejsze.

Najbezpieczniej jest:
- położyć instancje w cloud (docker stop jira jiradb),
- usunąć je (docker rm jira jiradb)
- a następnie zrobić rsync i podnieść poleceniami z dokumentacji

Wielokrotnie testowałem rsync z działającą Jirą oraz Bitbucket na
jira.example.com oraz położonymi instancjami w Cloud i nigdy nie było
problemu. Najbezpieczniej jest jednak zawsze położyć instancje po obu
stronach (internal oraz w cloud) zarówno bazy danych jak i aplikacji,
a dopiero później robić rsync. Wtedy prawdopodobieństwo błędów jest
najmniejsze.



Sieć
----
1. Otworzenie na firewallu połączenia SSH oraz Rsync pomiędzy jira.example.com a jira.cloud.example.com


Przygotowanie maszyny źródłowej
-------------------------------
1. Zalogowanie się do maszyny `ssh jira.example.com`

2. Przelogowanie na root:
   - `sudo su -`

3. Dopisanie do `/root/.profile`

    ```bash
    project_name='jira.example.com'

    red='\[\033[00;31m\]'
    green='\[\033[00;32m\]'
    blue='\[\033[00;36m\]'
    white='\[\033[00;39m\]'

    export PS1="\n${green}root@${project_name}> ${white}"
    ```

4. Dopisanie do `/root/.ssh/config`

    ```ssh-config
    Host jira.cloud.example.com
            HostName jira.cloud.example.com
            Port 22
            User root
    ```

5. Wygenerowanie `ssh-keygen` klucza prywatnego dla użytkownika root@jira.example.com
6. Poprawa w pliku `/root/.ssh/id_rsa.pub` komentarza do klucza:
   - z `root@jira`
   - na `root@jira.example.com`


Przygotowanie maszyny docelowej
-------------------------------
1. Zalogowanie się po ssh do `ssh admin_jira@10.28.4.6`
    - Hasło zna również: ....
    - Dostęp robił: ....

2. Przelogowanie na root:
   - `sudo su -`

3. Dopisanie do `/home/root/.ssh/authorized_keys` klucza publicznego użytkownika root@jira.example.com

    ```ssh-key
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDh3x0QFqFYD028w/ZjWfrUBVZXCHxK9ZhhY1rZfA5cemWxve8e5IqBFkQaCwqAv5vnBDrrsAAswxV99stMInx1H00V4ZT7kg4U0Lu8xAFiqZIyzFCRZQ07Q1sFLj13J5A/r4Od7JB9N4FqDNWVD+R3Z9I0EZokabPAACrNlYt4fKSHlenKniJFUnjkEl8ZbGNbrfqw27y0/Gj8GVlGpkHmAtqZUj4Xy+Aw8K8qrdAY9erA3u3CPhEDX++Cn7iNRLYke5LXMof2OrnP/9rveIlJGiDKCw2r+K7sVp1GWCbFA8eX6GMQXvljj82oMkVWMYQf0pxxLh8dFcPlVJaMVqlO/E9H1bp1SiccLHFb7N4HNdVvSgFlWIltM4lGQ0vYfPtjqMdDAfTx2aRN7BoU1s7sONqNDLB8IKyKXz3WoW6GnB0wvvtOpkX3H+t1jgUhL1346p0HBEI776fzTElRIzRP1kP/qCm9Td6VxQh6RCHLnNRkZ5JvrOh+yxEAvRFN2v0= root@jira.example.com
    ```

4. Instalacja Docker i konfiguracja sieci
    - `curl https://get.docker.com |sh`
    - `docker network create atlassian`

