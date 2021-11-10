### Szkolenie

## Pods

_pod_ - a group of sea mammals such as *whales*

list namespaces

```shell
kubectel get namespaces
```

list pods in default namespace

```shell
kubectl get pod
```

list pods in 'jenkins' namespace

```shell
kubectl -n jenkins get pod

# NAME , READY                    , STATUS, RESTARTS                          , AGE
# nazwa, ilosc kontenerów w podzie,..     , ilosc restartów kontenera w podzie, ...
```

get more information about pod ( NODE, IP, ...)

```shell
kubectl -n jenkins get pod -o wide
```

much more pod information

```shell
kubect -n jenkins describe pod 
```

![describe_pod_img.png](media/describe_pod_img.png)

even more pod information in yaml format

```shell
kubectl -n jenkins describe pod -o yaml
```

![describe_pod_yaml.png](media/describe_pod_yaml.png)

## How to make new deployment

First create new namespace

```shell
kubectl create namespace nsnazwa
```

Them use that namespace as a default context

```shell
kubectel config set-context --current --namespace=nsnazwa 
```

run a pod using image `example/mailcatcher-openshift` (it's similar to docker)

```shell
kubectl run mailcatcher --image=example/mailcatcher-openshift 
```

take a look at logs ot that pod

```shell
kubectl logs mailcatcher
## --since=10s - logs from last 10 seconds
## -f  - follow logs 
```

to get mor info on logs (or any other command) use

```shell
kubectl help logs
```

redirection of port 1080 of mailcatcher to localhost ( in our case bastion host )

```shell
kubectl port-forward mailcatcher 1080
# pokaz stronkę z poziomu konsoli bastion hosta
cutl localhost:1080
```

list all resources in current namespace

```shell
kubectl get all
```

## Komunikacja między podami

(_deprecated_) manually expose a pods port that can be used by other pods (don't use it as you should expose deployments
rather than pods, more on that later)

```shell
kubectl expose pod mailcatcher --port 1080
```

connect to jenkins pod with bash

```shell
kubectl -n jenkins exec -it jenkins-567f566dd-hlzwv /bin/bash
## in the console
# connect to service exposed in steps above ( accessing from different namespace)
curl http://mailcatcher.nsnazwa.svc.cluster.local:1080
# this would work if we're connected from same namespace
curl http://mailcatcher:1080
```

list labels for the pod

```shell
kubectl label pod mailcatcher --list
```

remove a service (ports will not be accessible from other pods)

```shell
kubectl delete service mailcatcher
```
expose the port again

```shell
kubectl expose pod mailcatcher --port 1080
```

show attributes of the mailcatcher service

```shell
kubectl get service mailcatcher -o yaml
```

_gotcha:_ you need to be aware that 'spec.selector' yaml path contains labels for a pod which will be called on the request
on the port 1080, if labels are messed up this might lead to surprising results

removing pod, does not remove the service
```shell
kubectl delete pod mailcatcher
```

removing all resources labeled with run=mailcatcher - would remove service and the pod

```shell
kubectl delete all -l run=mailcatcher
```

## Redeployment 

![img.png](media/img.png)

![img_1.png](media/img_1.png)

## Exposing services to outside world

The setup in COMPANY was created in a way that requires crating a subdomain as a first step
The nginx that is deployed is looking for a subdomain and traffic on that subdomain (in our case mail)
is redirected to a specific ingress (more details below)

![img_3.png](media/img_3.png)

```shell
# list services that are responsible for making the load balancing
kubectl -n ingress-nginx get service

```

### Crating ingress

as a rule of thumb - use existing ingress as a templace 

take ingress of drone-traffic app as one

```shell
kubectl -n drone-traffic get ingress
```

dup that ingres in yaml format to a file that we'll edit

```shell
kubectl -n drone-traffic get ingress drone-traffic-frontend -o yaml > mail-ingress.yaml
```

below is the dump, we need to get rid of junk and change some ids

```yaml

kind: Ingress
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"networking.k8s.io/v1beta1","kind":"Ingress","metadata":{"annotations":{"kubernetes.io/ingress.class":"nginx","nginx.ingress.kubernetes.io/configuration-snippet":"more_set_headers \"Access-Control-Allow-Origin:*\";\n","nginx.ingress.kubernetes.i
  o/cors-allow-methods":"PUT, GET, POST, OPTIONS","nginx.ingress.kubernetes.io/enable-cors":"true"},"labels":{"app":"drone-traffic-frontend"},"name":"drone-traffic-frontend","namespace":"drone-traffic"},"spec":{"rules":[{"host":"drone-traffic.dev.example.com","http":{"p
  aths":[{"backend":{"serviceName":"drone-traffic-frontend","servicePort":8080},"path":"/"},{"backend":{"serviceName":"drone-traffic-backend","servicePort":8080},"path":"/api"},{"backend":{"serviceName":"drone-traffic-backend","servicePort":8080},"path":"/ws"}]}}],"t
  ls":[{"secretName":"dev-example-tls"}]}}
kubernetes.io/ingress.class: nginx
nginx.ingress.kubernetes.io/configuration-snippet: |
  more_set_headers "Access-Control-Allow-Origin:*";
nginx.ingress.kubernetes.io/cors-allow-methods: PUT, GET, POST, OPTIONS
nginx.ingress.kubernetes.io/enable-cors: "true"
creationTimestamp: "2021-01-10T23:23:14Z"
generation: 3
labels:
  app: drone-traffic-frontend
name: drone-traffic-frontend
namespace: drone-traffic
resourceVersion: "43681710"
selfLink: /apis/extensions/v1beta1/namespaces/drone-traffic/ingresses/drone-traffic-frontend
uid: ba396b00-6c24-4877-8348-2a24739549f7
spec:
  rules:
    - host: drone-traffic.dev.example.com
      http:
        paths:
          - backend:
              serviceName: drone-traffic-frontend
              servicePort: 8080
            path: /
          - backend:
              serviceName: drone-traffic-backend
              servicePort: 8080
            path: /api
          - backend:
              serviceName: drone-traffic-backend
              servicePort: 8080
            path: /ws
  tls:
    - secretName: dev-example-tls
status:
  loadBalancer:
    ingress:
      - ip: 52.143.9.40


```

chang to (mail-ingress.yaml):

```yaml
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
  labels:
    app: mail
  name: mail
  namespace: nsnazwa
spec:
  rules:
    - host: mail.dev.example.com
      http:
        paths:
          - backend:
              serviceName: mailcatcher
              servicePort: 1080
            path: /
```

apply the ingress, now all should work
```shell
kubectl apply -f mail-ingress.yaml
```

and it works as we see on a screen below
![img_2.png](media/img_2.png)

## Deploymenty

creating a deployment for an image from console

```shell
kubectl create deployment mailcatcher --image=example/mailcatcher-openshift 
```

RS - replicatin set - defines number of pods, deployment strategy ( recreate, rolling)
_*NOTE*_ when you define a deployment you need to defina all other resources like service, ports etc in context of
that deployment, not a pod that belongs to one. deployment is dynamically managing pods, so we need to map to other
services on deployment level.

show properties of our deployment 

```shell
kubectl describe deployment mailcatcher
```

describe deployment in yaml format ( contains garbage that will not be useful if you want to take it as a template)

```shell
 kubectl get deployment mailcatcher -o yaml
```

start rolling update of a deployment

![img.png](media/img.png)
_gotcha:_ health checks - you need to implement them in a way that k8s really knows if a service is up and running as
no health checks might result in a switch to new instance of service that is actually still in deployment phase

rollout out deployment
```shell
kubectl rollout restart deployment mailcatcher
```

take a look at rollout history
```shell
kubectl -n drone-traffic rollout history deployment drone-traffic-backend

kubectl -n drone-traffic rollout history deployment
```

expose deployment ports (if more than one pod in deployment a round-robin approach is used to balance load)

```shell
kubectl expose deployment mailcatcher --port 1080
```

## Managing secrets

sample creation of a sealed secret

```shell
kubectl create secret generic test --from-literal user=myusername --from-literal password=asfasdf -n test123456 --dry-run -o yaml > cred.yaml
kubeseal --controller-name=sealed-secrets  --controller-namespace=gitops -o yanl < cred.yank > sealed-cred.yaml
```

sample command retrieving sealed secret 

```shell
kubectl -n keycload get secrets keycloak -o yaml
```
