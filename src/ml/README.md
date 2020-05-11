
## Installation

* As cuML is under active work, the team probably did not wish it to be made a _default_ for all users.
Hence, if you wish to install the `conda` packages for `cuml` then you need to
consult this [rapidsai conda package selector](https://rapids.ai/start.html#rapids-release-selector)
and select the `cuml=0.13` or recent package versions.
  * E.g. without `cuml`, the installation command looks like : `conda install --yes -c rapidsai -c nvidia -c conda-forge -c defaults cudf=0.13 dask-cudf=0.13 dask-cuda=0.13 cudatoolkit=10.2`
  * E.g. **`with`** `cuml`, the installation command looks like : `conda install --yes -c rapidsai -c nvidia -c conda-forge -c defaults cuml=0.13 cudf=0.13 dask-cudf=0.13 dask-cuda=0.13 cudatoolkit=10.2`
* You also need to install `scipy` via `conda` because `RAPIDSAI` is leveraging it as a package manager.
  * `conda install scipy`
  * `conda install scikit-learn`

When running the sample programs, you can use `nvidia-smi` to get some insights
into the resources consumed (in this example, the `gpu-id` is `0` meaning i
have 1 GPU ready):
```
(base) ubuntu@ip-10-0-0-33:~$ nvidia-smi
Mon May 11 04:46:13 2020
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.33.01    Driver Version: 440.33.01    CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:00:1E.0 Off |                    0 |
| N/A   40C    P0    38W / 300W |    804MiB / 16160MiB |      0%      Default | <-- 800+ MB out of 16GB GPU DRAM is consumed for 1 python machine learning program
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0     12704      C   python                                       779MiB |
+-----------------------------------------------------------------------------+
```


