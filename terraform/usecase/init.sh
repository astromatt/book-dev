#! /bin/sh

## Install MicroK8s
sudo snap install microk8s --classic

## Setup env and add user to the microk8s group
sudo usermod -aG microk8s $USER
sudo chown -fR $USER ~/.kube
echo 'alias mkctl="microk8s kubectl"' >> ~/.bashrc

## Reload the user groups
newgrp microk8s

## Check the status while Kubernetes starts
microk8s status --wait-ready

## Turn on the services you want
microk8s enable dashboard dns ingress

## Start using Kubernetes
microk8s kubectl get all --all-namespaces

## Install Tekton CI
URL='https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml'
kubectl apply --filename $URL

## Install Argo CD
URL='https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml'
kubectl create namespace argocd
kubectl apply -n argocd -f $URL