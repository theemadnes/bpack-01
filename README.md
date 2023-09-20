# bpack-01
playing around with bin-packing in containers

### notes

```
# prep emulator 
docker run --privileged --rm tonistiigi/binfmt --install arm64


docker build --platform=linux/arm64 -t us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/cpu-stresser-arm .
docker push us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/cpu-stresser-arm
```

```
# image for x86
us-central1-docker.pkg.dev/cicd-system-demo-01/cicd-demo-01/cpu-stresser@sha256:823120a5ca095669a67b06d6daf0fb2fa94d218cded8f79174048c25ac797e55
# image for ARM


```