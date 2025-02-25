from setuptools import setup, find_packages, find_namespace_packages
import platform

install_requires = [
    "datasets==2.12.0",
    "evaluate==0.4.0",
    "huggingface-hub==0.14.1",
    "iopath==0.1.10",
    "nltk==3.8.1",
    "numpy==1.22.0",
    "omegaconf==2.3.0",
    "pandas==1.3.5",
    "pyparsing==3.0.7",
    "PyYAML==6.0",
    "requests==2.31.0",
    "rouge-score==0.1.2",
    "sacrebleu==2.3.1",
    "scikit-learn==1.0.2",
    "torch==1.13.1",
    "torchvision==0.14.1",
    "tqdm==4.63.0",
    "tree-sitter==0.20.1",
    "bitsandbytes==0.39.0"
]

DEPENDENCY_LINKS = []
if platform.system() == "Windows":
    DEPENDENCY_LINKS.append("https://download.pytorch.org/whl/torch_stable.html")
DEPENDENCY_LINKS.append("git+https://github.com/huggingface/transformers.git")
DEPENDENCY_LINKS.append("git+https://github.com/huggingface/peft.git")
    
setup(
  name = 'salesforce-codetf',
  version = "1.0.1.1",
  py_modules = ['codetf'],
  description = 'CodeTF: A Transformer-based Library for Code Intelligence',
  author = 'Nghi D. Q. Bui',
  package_dir={"codeff": "codetf"},
  long_description=open("README.md", "r", encoding="utf-8").read(),
  long_description_content_type="text/markdown",
  keywords="AI4Code, Code Intelligence, Generative AI, Deep Learning, Library, PyTorch, HuggingFace",
  license="Apache 2.0",
  url = 'https://github.com/Salesforce/CodeTF',
  packages=find_packages(where=".", exclude=["tests", "assets", "datasets"]),
  package_data={'codetf': ['configs/*']},
  install_requires=install_requires,
  include_package_data=True,
  zip_safe=False,
  python_requires=">=3.8.0",
  dependency_links=DEPENDENCY_LINKS,
)