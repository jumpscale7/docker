Build tools for jumpscale docker images
=======================================

use these build scripts to make your life easy

base image with mc & prepared for jumpscale
-------------------------------------------

we use 
https://github.com/phusion/baseimage-docker
as basis

just execute following on an installed ubuntu 14.04 or 14.10 64 bit machine
the result will be a built docker

```
#if ubuntu is in recent state & apt get update was done recently
curl https://raw.githubusercontent.com/Jumpscale/docker/master/install/build_mc.sh | bash

```

base image with jumpscale starting from mc image above
-------------------------------------------

```
curl https://raw.githubusercontent.com/Jumpscale/docker/master/install/build_js.sh | bash

```

and now?
========

e.g. push your created docker
```
docker login
docker push despiegk/mc
```


