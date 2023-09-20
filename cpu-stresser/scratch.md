```
docker build -t us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/cpu-stresser .
docker push us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/cpu-stresser

# update node pool to use static CPU assignment
gcloud container node-pools update default-pool \
    --cluster=cluster-1 \
    --system-config-from-file=system-config.yaml --project=mc-e2m-01

gcloud beta container --project "mc-e2m-01" clusters create "cluster-2" --region "us-central1" --no-enable-basic-auth --cluster-version "1.27.3-gke.100" --release-channel "regular" --machine-type "c3-standard-4" --image-type "COS_CONTAINERD" --disk-type "pd-ssd" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "2" --logging=SYSTEM,WORKLOAD --monitoring=SYSTEM --enable-ip-alias --network "projects/mc-e2m-01/global/networks/default" --subnetwork "projects/mc-e2m-01/regions/us-central1/subnetworks/default" --no-enable-intra-node-visibility --default-max-pods-per-node "110" --security-posture=standard --workload-vulnerability-scanning=disabled --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --enable-managed-prometheus --enable-shielded-nodes --node-locations "us-central1-a","us-central1-b","us-central1-c" --system-config-from-file=system-config.yaml
```