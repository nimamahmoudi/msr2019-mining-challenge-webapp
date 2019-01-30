kubectl delete job django-migrations
kubectl apply -f kubernetes/django/job-migration.yaml
kubectl delete deployment django
kubectl apply -f kubernetes/django/deployment.yaml