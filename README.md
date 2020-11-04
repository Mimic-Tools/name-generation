# Mimic Tools' Character Name Generation

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Mimic-Tools/name-generation) ![Python Tests](https://github.com/Mimic-Tools/name-generation/workflows/Python%20Tests/badge.svg)

A tool to generate character names for your RPGs, Novel or any sort of character creation.

## Features
- Python Interface, Sample HTML Page
- Male/Female/Neutral selections (Multiple Selection)
- Titles
- Origin based names NOT racial based names
- Multiple Name Order conventions
- Syllable based name generation for fantasy races.

## Contributions Welcome!

We are constantly looking to expanding both the variety and complexity of our names.
We are encouraging submissions for additional names and words to be added to our name generator. 
Check out our [Issues tab](https://github.com/Mimic-Tools/name-generation/issues)

### Non-technical
There are several places where non-technical help is appreciated:
 - Adding regional based names.
 - Adding Nouns/Adjectives for Surname generation based on region
 - Adding Syllables for Forename generation for fantasy races.
 
Check out our [Issues tab](https://github.com/Mimic-Tools/name-generation/issues)for more information

### Technical

Mostly looking for HTML layout improvements here, as well as improving test coverage and modularity.

## Installation

- Python3
- `pip3 install -r requirements.txt`
  
## Running the Name Generation

> cd src/name_generation/
>
> python3 generate.py

For all available configurable options, add --help

Some fast paths are available under scripts/ folder

### Connecting HTML Frontend

This should be managed by the backend application. The logic should import the python module and the views should use the provided html.

## Complaint?
Our project is evolving and while we wish our final product to be as inclusive as possible for all valid configurations, we will be starting at a simple base.
Please be patient with us as we try to best formulate how to enable all sorts of variations, cross-use of names, structural options, etc.

If you feel strongly about any decisions made, please raise an issue https://github.com/Mimic-Tools/name-generation/issues and we will do our best to resolve it, without hampering our project's trajectory.
