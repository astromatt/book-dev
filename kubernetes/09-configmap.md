ConfigMap
=========

Tworzenie ConfigMapy:

    $ kubectl create configmap myconfigmap --from-literal KEY=VALUE
    $ kubectl create configmap myconfigmap --from-literal port=1337
    $ kubectl create configmap myconfigmap --from-literal port=1337 --from-literal host=localhost
    configmap/myconfigmap created

Wypisz wszystkie configmapy:

    $ kubectl get configmaps
    $ kubectl get cm

Wyświetlanie wartości:

    $ kubectl describe configmap myconfigmap
    $ kubectl describe cm myconfigmap


From YAML File
--------------
ConfigMapy można również stworzyć w pliku YAML i później zrobić `kubectl apply`

    $ kubectl create configmap myappcfg2 --from-file=application.yaml
    $ kubectl get cm
    $ kubectl describe cm myappcfg2
    $ kubectl edit cm myappcfg2
    $ kubectl get configmaps myappcfg2 -o yaml
    $ kube-neat get configmaps myappcfg2 -o yaml  # oczyszcza dane wypluwane przez kubectl


From ENV File
-------------
