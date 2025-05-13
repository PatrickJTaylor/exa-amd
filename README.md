# exa-AMD: Exascale Accelerated Materials Discovery
exa-AMD is a Python framework designed to accelerate the discovery and design of functional materials. The framework uses [Parsl](https://parsl-project.org) to build customizable and automated workflows that connect AI/ML tools, material databases, quantum mechanical calculations, and state-of-the-art computational methods for novel structure prediction. exa-AMD was designed to scale up on high-performance computing systems including supercomputers equipped with accelerators, such as the Nvidia and AMD GPUs.

It comes with a flexible configuration system based on a global registry. You can choose which Parsl configuration to load at runtime by setting the `parsl_config` key in the global configuration.It is also possible to create new configs simply by creating a new file in the `parsl_configs` directory and registering it.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Register a new Parsl config](#register-parsl-config)
- [Examples](#examples)

## Prerequisites
This package requires:
- python = 3.12
- scikit-learn
- pytorch
- torchvision
- pymatgen
- parsl
- pytest

Additionally:
- Ensure you have a working [VASP](https://www.vasp.at) installation
- Ensure you have prepared the initial crystal structures in the Crystallographic Information File (CIF) format and put in a directory called `mpstrs` 
```bash
cp -R mpstrs ./ctest 
```
- Ensure you have [Conda](https://docs.conda.io/en/latest/miniconda.html) installed.
- Install the required packages and activate the `amd_env` environment
```bash
conda env create -f amd_env.yml
conda activate amd_env

```

### Required external packages 
- This package contains a modified version of Crystal Graph Convolutional Neural Networks (CGCNN). The original source code can be found [here](https://github.com/txie-93/cgcnn).

## Usage
- Copy the `mpstrs` directory into the `cms_dir`
- Set up a json configuration file (similar to [configs/chicoma.json](configs/chicoma.json))
- Run `python amd.py --config <your_config_file>`

The json config file can be overriden via command line arguments.

```bash
python amd.py --help
```

## Register a new Parsl config
Add your own Parsl config (if we do not support your system)

1. Create a new config similar to [parsl_configs/chicoma.py](parsl_configs/chicoma.py)
2. Register you config by calling `register_parsl_config()` and choosing an unique name `<my_parsl_config_name>`
3. Modify your json config accordingly (i.e. set `parsl_config` to `<my_parsl_config_name>`)

## Examples
Prediction of new CeFeIn compounds using this framework.

<img width="677" alt="thrust1" src="https://github.com/user-attachments/assets/b067d23f-fd43-4409-b44b-01d1457bb440" />

## Copyright
Copyright 2025. Iowa State University. All rights reserved. This software was produced under U.S. Government contract DE-AC02-07CH11358 for the Ames National Laboratory, which is operated by Iowa State University for the U.S. Department of Energy. The U.S. Government has rights to use, reproduce, and distribute this software. NEITHER THE GOVERNMENT NOR IOWA STATE UNIVERSITY MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR ASSUMES ANY LIABILITY FOR THE USE OF THIS SOFTWARE. If software is modified to produce derivative works, such modified software should be clearly marked, so as not to confuse it with the version available from the Ames National Laboratory.

© 2025. Triad National Security, LLC. All rights reserved.
This program was produced under U.S. Government contract 89233218CNA000001 for Los Alamos National Laboratory (LANL), which is operated by Triad National Security, LLC for the U.S. Department of Energy/National Nuclear Security Administration. All rights in the program are reserved by Triad National Security, LLC, and the U.S. Department of Energy/National Nuclear Security Administration. The Government is granted for itself and others acting on its behalf a nonexclusive, paid-up, irrevocable worldwide license in this material to reproduce, prepare. derivative works, distribute copies to the public, perform publicly and display publicly, and to permit others to do so.(Copyright request O4873).