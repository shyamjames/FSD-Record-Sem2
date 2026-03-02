from setuptools import setup, find_packages
import os

readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = "A helper library for AI web applications"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="ai_web_helper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
        "markdown",
        "flask",
        "python-dotenv"
    ],
    author="AI Assistant",
    description="A helper library for AI web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
