# Mimic Tools' Character Name Generation
A tool to generate character names for your RPGs, Novel or any sort of character creation.

## Current Status

We are currently expanding both the variety and complexity of our names.
- We are encouraging submissions for additional names and words, to be added for selection
- We have released a v0.1 of the name generator and are working on an easier interface for people to use.

## Features
- Python Interface
- Male/Female/Neutral name selection (Multiple Selection)
- Titles
- Origin based names NOT racial based names
- Multiple Name Order conventions

## Seeking Contribution

We are participating in #hacktoberfest and welcome (meaningful) contribution.
Check out our Issues tab

### Non-technical
You can help populate our name banks. In particular, our name 'decorators' such as titles, etc. could use some additional words. Have a look around the name-segments folder for what you can contribute to

We also would love your input on the formation of names. 
> example: Dwarven surnames could be made up of a adjective + noun
> Trueaxe. Blackmountain. Fasthammer.

### Technical
We are editing the core right now, so any core generation code is not a stable place to start, unless otherwise stated, but any issues in https://github.com/Mimic-Tools/name-generation/issues are fair game! Additionally, any standalone scripts!

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
> python3 generate.py

For all available configurable options, add --help
