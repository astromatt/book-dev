Ingress
=======


Rationale
---------
Umożliwia komunikację z podem z zewnątrz. Na poziomie definicji ingresu
definiujemy service, do którego dopuszcza


Konfiguracja
------------
Pliki Ingress trzymane są w ``ingress.yaml``, przykład:

    $ cat ingress.yaml
    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
      labels:
        app: jenkins
      annotations:
        kubernetes.io/ingress.class: nginx
      name: jenkins
      namespace: jenkins
    spec:
      rules:
        - host: jenkins.example.com
          http:
            paths:
              - backend:
                  serviceName: jenkins
                  servicePort: 8080
                path: /

Tworzenie
---------
Tworzenie Ingress na podstawie konfiguracji z pliku yaml:

    $ kubectl apply -f ingress.yaml


Listowanie
----------
Wypisz aktywne Ingress:

    $ kubectl get ingress
