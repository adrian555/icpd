# py-oah

This repo hosts the `openaihub` python package. To install

```command line
pip install openaihub
```

## pre-requirements

* a kubernetes cluster
* `helm` must be installed

## install OpenAIHub

To use the cluster's default StorageClass, run following command:

```command line
openaihub install --namespace kubeflow
```

Note: if `namespace` parameter is not specified, all services will be installed to `operators` namespace.

Otherwise, to specifically use the `nfs-dynamic` StorageClass to be created by OpenAIHub as the default StorageClass, run following command:

```command line
openaihub install --storage nfs --namespace kubeflow
```