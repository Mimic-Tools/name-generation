# Mimic Tools' Character Name Generation

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Mimic-Tools/name-generation)

A tool to generate character names for your RPGs, Novel or any sort of character creation.

## Current Status

We are constantly looking to expanding both the variety and complexity of our names.
We are encouraging submissions for additional names and words to be added to our name generator.

## Features
- Python Interface
- Male/Female/Neutral selections (Multiple Selection)
- Titles
- Origin based names NOT racial based names
- Multiple Name Order conventions
- Syllable based name generation for fantasy races.

## Seeking Contribution

We are participating in #hacktoberfest and welcome (meaningful) contribution.
Check out our [Issues tab](https://github.com/Mimic-Tools/name-generation/issues)

### Non-technical
There are several places where non-technical help is appreciated:
 - Adding regional based names.
 - Adding Nouns/Adjectives for Surname generation based on region
 - Adding Syllables for Forename generation for fantasy races.

All of these are located in different folders underneath the "name-segments" folder.

We also would love your input on the formation of names. 
> example: Dwarven surnames could be made up of a adjective + noun
> Trueaxe. Blackmountain. Fasthammer.

### Technical
We are editing the core right now, so any core generation code is not a stable place to start, unless otherwise stated, but any issues in Issues tab](https://github.com/Mimic-Tools/name-generation/issues) are fair game! Additionally, any standalone scripts, or improvements to the non-technical path (e.g. testing CI)

## Hurdles
Our project is evolving and while we wish our final product to be as inclusive as possible for all valid configurations, we will be starting at a simple base.
Please be patient with us as we try to best formulate how to enable all sorts of variations, cross-use of names, structural options, etc.

If you feel strongly about any decisions made, please raise an issue https://github.com/Mimic-Tools/name-generation/issues and we will do our best to resolve it, without hampering our project's trajectory.

Finally comply with our file naming and style conventions. 

## Installation

- Python3
- NLTK
  > pip3 install nltk
  
## Running the Name Generation

We're currently trying to make this more accessible, but for now the way to run is:
> cd src/name_generation/
>
> python3 generate.py

For all available configurable options, add --help

Some fast paths are available under scripts/ folder
