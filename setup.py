from setuptools import setup, find_packages

setup(
    name="notifier_client",
    version="0.1.0",
    description="Client library for sending notifications to a remote Telegram bot service",
    author="Yasaly",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)
