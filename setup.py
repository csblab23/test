from setuptools import setup, find_packages

setup(
    name="SCART",
    version="0.1.0",
    description="Single-cell Antigen Ranking Tool",
    author="CSB LAB",
    packages=find_packages(include=["SCART", "SCART.*"]),
    python_requires=">=3.9,<3.12",
    include_package_data=True,
    package_data={
        "SCART": [
            "**/*.json",
            "**/*.csv",
            "**/*.txt",
            "**/*.pkl",
            "**/*.h5ad",
            "**/*.yaml",
            "**/*.yml",
            "**/*.joblib",
            "**/*.gmt",
            "**/*.tsv"
        ]
    },
    zip_safe=False,
    install_requires=[
        "scanpy==1.9.3",
        "geofetch",
        "GEOparse",
        "popv==0.4.2",
        "scvi-tools",
        "numpy",
        "pandas",
        "scikit-learn",
        "torch",
        "tensorflow",
        "deap==1.4",
        "typer",
        "rich",
        "rpy2",
    ],
    extras_require={
        "copykat": [
            "rpy2",
        ]
    }
)
