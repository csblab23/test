from setuptools import setup, find_packages

setup(
    name="SCART",
    version="0.1.0",
    description="Single-cell Antigen Ranking Tool",
    author="CSB LAB",
    packages=find_packages(include=["SCART", "SCART.*"]),
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
        # ✅ core flexible deps
        "numpy",
        "pandas",
        "scikit-learn",
        "typer",
        "rich",
        "GEOparse",
        "geofetch",

        # ✅ pinned (as requested)
        "popv==0.4.2",
        "deap==1.4",
        "scipy>=1.10",   # ✅ relaxed

        # ✅ heavy deps (still required, but not pinned)
        "scanpy",
        "scvi-tools",
        "torch",
        "tensorflow",

        # ✅ keep rpy2 flexible
        "rpy2>=3.5"
    ],
)
