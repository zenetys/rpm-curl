| <nobr>Package name</nobr> | <nobr>Supported targets</nobr> |
| :--- | :--- |
| curl0z | <nobr>el8, el9</nobr> |
<br/>

This package depends on shared libraries provided by:

* [zenetys/rpm-aws-lc](https://github.com/zenetys/rpm-aws-lc)
* [zenetys/rpm-ngtcp2](https://github.com/zenetys/rpm-ngtcp2)
* [zenetys/rpm-nghttp3](https://github.com/zenetys/rpm-nghttp3)
<br/>

## Build:

The package can be built easily using the rpmbuild-docker script provided
in this repository. In order to use this script, _**a functional Docker
environment is needed**_, with ability to pull Rocky Linux images from
internet if not already downloaded.

```
$ ./rpmbuild-docker -d el8
$ ./rpmbuild-docker -d el9
```

## Prebuilt packages:

Builds of these packages are available on ZENETYS yum repositories:<br/>
https://packages.zenetys.com/latest/redhat/
