# Kubernetes Deployments

## Postgres

```
# Create the volume
kubectl apply -f kubernetes/postgres/volume.yaml

# Claim to get the volume
kubectl apply -f kubernetes/postgres/volume_claim.yaml

# Create Secrets
kubectl apply -f kubernetes/postgres/secrets.yaml

# Deploy
kubectl apply -f kubernetes/postgres/deployment.yaml

# Add Access through the service
kubectl apply -f kubernetes/postgres/service.yaml

```

## Django

```
# This job will migrate the database everytime we need it to
kubectl apply -f kubernetes/django/job-migration.yaml
kubectl delete job django-migrations

# Deploy the django application
kubectl apply -f kubernetes/django/deployment.yaml

# open up the ports
kubectl apply -f kubernetes/django/service.yaml

```


# Test

```
kubectl run -i --tty test --image=ubuntu bash
```

## Useful Stuff

```
# SSH port forwarding
ssh -N -L 8001:localhost:8001 ubuntu@IP

# Foward the kubernetes postgres on local computer
kubectl port-forward svc/postgres-service 5432:5432


# Admin Dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/src/deploy/recommended/kubernetes-dashboard.yaml
kubectl proxy


http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/

```


