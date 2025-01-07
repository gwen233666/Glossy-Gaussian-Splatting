## Glossy-Gaussian: Adaptive Anisotropic Gaussian splatting <br><sub>PyTorch Implementation</sub> 

### [[Paper](later on)](https://arxiv.org/abs/) 

This work introduces "Glossy-Gaussian," a novel approach that leverages Adaptive Anisotropic Gaussians (AAG) as a plug-and-play integration for 3D Gaussian Splatting (3DGS) to handle glossy and reflective materials in real-time rendering. By enhancing the view-adaptive spherical harmonic (SH)-based Gaussian kernels, the method imparts anisotropy to the transparency field, enabling accurate representation of specular and smooth reflective surfaces without sacrificing rendering speed. Additionally, they support extension to other Gaussian properties. Experimental results demonstrate significant improvements in rendering quality, achieving better performance in glossy scene reconstruction with enhanced metrics like PSNR, SSIM, and LPIPS across diverse datasets.


## Cloning the Repository

The repository contains submodules, thus please check it out with 
```shell
# HTTPS
git clone https://github.com/gwen233666/Glossy-Gaussian-Splatting.git
```

## Overview

The codebase has 2 main components:
- PyTorch-based optimizer, this component optimizes a Glossy-Gaussian model from SfM, most parameter settings align with those in [gaussian splatting](https://github.com/graphdeco-inria/gaussian-splatting).
- Adaptive Anisotropic Gaussian rasterizer, this plug-and-play component enhances the 3D Gaussian Splatting (3DGS) method by introducing view-adaptive spherical harmonic-based Gaussian kernels, such as providing more detailed transparency information.

## Setup
We provide conda install instructions in this repo:
```shell
conda env create --file environment.yml
conda activate Glossy-GS
```
Please ensure the installation of the dedicated rasterizer used by AAG.
```shell
conda activate Glossy-GS
pip install ./submodules/diff-gaussian-rasterization
pip install ./submodules/simple-knn
```

## Running
Our code operates in the same way as the original 3DGS. Please refer to [gaussian splatting](https://github.com/graphdeco-inria/gaussian-splatting) for details.
## BibTeX
If you find our paper/project useful, please consider citing our paper:
```bibtex
@article{li20243d,
  title={Glossy-Gaussian: Adaptive Anisotropic Gaussians for View-Dependent Appearances},
  author={Wendi Zhang, Tengfei Wang, Zongqian Zhan, Xin Wang},
  journal={},
  year={2024}
}
```
