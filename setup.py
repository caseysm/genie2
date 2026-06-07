from setuptools import find_namespace_packages, setup

setup(
      name='genie',
      version='0.0.1',
      description='de novo protein design through equivariantly diffusing oriented residue clouds',
      packages=find_namespace_packages(include=['genie*']),
      install_requires=[
            'tqdm',
            'numpy',
            'torch',
            'scipy',
            'wandb',
            'tensorboard',
            'pytorch_lightning',
      ],
)
