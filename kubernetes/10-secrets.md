Secrets
=======
* Wyglądają identycznie jak ConfigMapy
* Różnica jest taka, że zawartość jest zaszyfrowana (base64)

    $ kubectl create secret generic  # key-value
    $ kubectl create secret tls  # do trzymania kluczy, certyfikatów itp
    $ kubectl create secret docker-registry  # trzyma credentiale do rejestru dockerowego, trzyma je w pliku docker.json (chyba)


Tworzenie
---------

    $ kubectl create secret generic topsecret --from-literal password=mypassword --from-literal=myusername
    secret/topsecret created
    $ kubectl describe secrets topsecret

    $ kubectl get secrets topsecret -o yaml  # pozwala na podglądnięcie secretów

    $ echo 'YW5kaQ==' | base64 --decode
    myusername

Nie poleca się wrzucania wyników tego polecenia do repozytorium kodu, bo ktoś może podejrzeć wartości.
Korzystamy z KubeSeal, który szyfruje Secrety.
Pozwala na trzymanie configów w repozytorium kodu.
Kiedy trafia na Kubernetes, to jest już odszyfrowywany.

Zalecany jest Vault, który jest bardziej bezpieczny, ale trudniejszy.


Kasowanie
---------

    $ kubectl delete secrets --all
