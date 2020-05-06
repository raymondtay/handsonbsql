# Hands on BlazingSQL

Introductory material to getting started with BlazingSQL.

Why would you need something like BlazingSQL? Many a times, large amounts of data is not installed
on your local computer, chances are the data is living in some kind of external storage e.g. cloud storage
or NAS.

This repository is sourced mostly from the rapidsai teams where they've actively working on delivering BSQL
to the community. Their github repository is [here](https://github.com/BlazingDB/blazingsql).

Why don't i just run the examples found on their juypter notebooks co-lab environment? Sure you can, but
i prefer to work directly with the code.

## Context

These demo code is run ontop of AWS EC2 Tesla V100 GPUs, CUDA Toolkit 10.2.89
installed. The code repository is organized as follows:
(a) everything in the root directory are stuff to get you started
(b) everything in the `df` sub-directory is for understanding a little bit more about `cudf.DataFrame`

## Supported Nvidia GPU architecture

As of May 2020, the support GPU for _BlazingSql_ is of _compute capability_ `>=
6.0` and you can refer to [nvidia's support gpu](https://developer.nvidia.com/cuda-gpus#compute)
to check out whether you have a supported GPU.

### AWS EC2 Pricing

Refer to this [pricing page](https://aws.amazon.com/ec2/pricing/on-demand/) on
EC2 to select which GPU suits you.


