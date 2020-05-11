# Hands on BlazingSQL

Introductory material to getting started with BlazingSQL.

Why would you need something like BlazingSQL? Many a times, large amounts of data is not installed
on your local computer, chances are the data is living in some kind of external storage e.g. cloud storage
or NAS. Considering that the data is already on some kind of storage, you
probably would be wondering if analyzing the datasets needs a SQL-like
database? TLDR version is **`no`** and that's the beauty of blazingsql - you
can run SQL-like queries against the datasets without actually using a
database.

What's even better is that you can re-use/integrate your favourite machine
learning or deep learning libraries and conduct the data analysis.

This repository is sourced mostly from the rapidsai teams where they've actively working on delivering BSQL
to the community. Their github repository is [here](https://github.com/BlazingDB/blazingsql).

Why don't i just run the examples found on their juypter notebooks co-lab environment? Sure you can, but
i prefer to work directly with the code.

## Recordings

See `BlazingSQL` in action. The following 2 recordings _should be_ watched side-by-side so that you can observe the resource consumption while the programs are executing.
[![asciicast](https://asciinema.org/a/iWf1fNndRmeRMixCzlxatjdZ7.png)](https://asciinema.org/a/iWf1fNndRmeRMixCzlxatjdZ7)
[![asciicast](https://asciinema.org/a/nu17IGDTpiMkxLN9xWSEh2lNR.png)](https://asciinema.org/a/nu17IGDTpiMkxLN9xWSEh2lNR)


## Context

These demo code is run ontop of AWS EC2 Tesla V100 GPUs, CUDA Toolkit 10.2.89
installed. The code repository is organized as follows:
(a) everything in the root directory are stuff to get you started
(b) everything in the `df` sub-directory is for understanding a little bit more about `cudf.DataFrame`

### Git Large File System

I'm using the `git lfs` to store large amounts of data since github isn't
the right place for this kind of data. This is a good solution if you do not
wish to maintain data on cloud storages.

To install `git lfs` on Ubuntu 18.04, i've found these instructions to be
useful, lifted from this [site](https://github.com/git-lfs/git-lfs/wiki/Installation):

* `curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash`
* `sudo apt-get install git-lfs`
* `git lfs install`

## Supported Nvidia GPU architecture

As of May 2020, the support GPU for _BlazingSql_ is of _compute capability_ `>=
6.0` and you can refer to [nvidia's support gpu](https://developer.nvidia.com/cuda-gpus#compute)
to check out whether you have a supported GPU.

### AWS EC2 Pricing

Refer to this [pricing page](https://aws.amazon.com/ec2/pricing/on-demand/) on
EC2 to select which GPU suits you.


### Reference

* [CUDA](https://developer.nvidia.com)
* [BlazingSQL main site](https://blazingsql.com)
* [BlazingSQL repository](https://github.com/BlazingDB/blazingsql)
