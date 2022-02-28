Namespace
=========


Rationale
---------
Grupuje pody i inne zasoby (resource)


Tworzenie
---------
Tworzenie nowego namespace

    $ kubectl create namespace myns

Stwórz pod w namespace `myns` na podstawie `pod.yaml`

    $ cat pod.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: alpine
    spec:
      containers:
      - image: alpine
        name: alpine

    $ kubectl apply -n myns -f pod.yaml


Listowanie
----------
Wypisanie wszystkich dostępnych namespace:

    $ kubectl get namespaces


Konfiguracja
------------
Jeżeli nie określisz namespace, to jest brana wartość domyślna opcji
`current-context` z pliku `~/.kube/config`.

    $ ls -la ~/.kube/
    total 16
    drwxr-xr-x   4 matt  staff   128 Apr  8 20:35 .
    drwxr-xr-x+ 81 matt  staff  2592 Apr  8 22:14 ..
    drwxr-x---   4 matt  staff   128 Apr  8 20:35 cache
    -rw-------   1 matt  staff  5560 Apr  8 20:14 config

    $ cat ~/.kube/config
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: LS0t...tCg==
        server: https://kubernetes.docker.internal:6443
      name: docker-desktop
    contexts:
    - context:
        cluster: docker-desktop
        user: docker-desktop
      name: docker-desktop
    current-context: docker-desktop
    kind: Config
    preferences: {}
    users:
    - name: docker-desktop
      user:
        client-certificate-data: LS0t...LS0K
        client-key-data: LS0t...tCg==

Ustawianie namespace jako domyślnego:

    $ kubectl config set-context --current --namespace=myns

