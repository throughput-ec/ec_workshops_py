# EarthCube Workshops

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/throughput-ec/ec-workshops/binder)

[![example workflow](https://github.com/throughput-ec/ec-workshops/actions/workflows/gatsby-publish.yaml/badge.svg)](https://github.com/throughput-ec/ec-workshops/actions)

## Objective

This project aims to show some powerful use cases of Data Science tools in the Earth Sciences. 
You can view the different modules deployed at  [site](https://throughput-ec.github.io/ec-workshops/)

## Contributors

This project is an open project, and contributions are welcome from any individual.  All contributors to this project are bound by a [code of conduct](CODE_OF_CONDUCT.md).  Please review and follow this code of conduct as part of your contribution.

  * [Socorro Dominguez Vidana](https://sedv8808.github.io/) [![orcid](https://img.shields.io/badge/orcid-0000--0002--7926--4935-brightgreen.svg)](https://orcid.org/0000-0002-7926-4935)
* [Simon Goring](http://www.goring.org/) [![orcid](https://img.shields.io/badge/orcid-0000--0002--2700--4605-brightgreen.svg)](https://orcid.org/0000-0002-2700-4605)

### Tips for Contributing

Issues and bug reports are always welcome.  Code clean-up, and feature additions can be done either through branches.
Any official communication for this project will be done using Github Issues.

All products of the Mid Project are licensed under an [MIT License](LICENSE) unless otherwise noted.

## How to use this repository

Simply go to the deployed version at [link]().

If you would like to run this repository from your local directory, you can follow these [instructions]().

Files and directory structure in the repository are as follows:
This structure might be modified as the project progresses.

```bash
ec-workshops
├── .gitignore          # Files you change on your local that you do not want to track changes for or commit to the repo. 
├── LICENSE             # Terms able to use this platform 
├── README.md           # Documentation and Description 
├── gatsby-browser.js    
├── gatsby-config.js    
├── gatsby-node.js      
├── ec-workshops.Rproj
├── meta.json           # Add necessary customization such as descriptions bio and branch needed to make binder from 
├── package-lock.json
├── package.json
├── theme.sass          # Can be customizable to change fonts style and size and website colours and font 
│   │    
├── binder  
|   ├── runtime.txt
|   └── install.R       # A file containing all the packages needed for the coding exercises
├── chapters            # Modules to be reviewed 
|   ├── chapter1.md
|   ├── ...
|   └── chapter7.md
│   │
├── exercises           # This file will contain all the coding exercise scripts. 
|   ├── exercise_01.py
|   ├── solution_01.py
|   ├── test_01.py
|   ├── function.py
|   └── price_linearanalysis3.png
│   │
├── data                # Store exercise datafiles here 
    └── exercise-data.csv
├── slides              # This is where the slide decks live
|   ├── module0_00.md
|   ├── ...
|   └── moduleN_nn.md
│   │
├── src                 # Don't want to go too much into this 
|   ├── markdown.js
|   ├── context.js
|   ├── components              
|   |   ├── button.js
|   |   ├── choice.js
|   |   ├── code.js
|   |   ├── exercise.js
|   |   ├── hint.js
|   |   ├── juniper.js
|   |   ├── layout.js
|   |   ├── link.js
|   |   ├── seo.js
|   |   ├── slides.js
|   |   └── typography.js
|   |   |   
|   ├── pages              
|   |   └── index.js
|   |   |
|   ├── styles               
|   |   ├── button.module.sass
|   |   ├── choice.module.sass
|   |   ├── code.module.sass
|   |   ├── exercise.module.sass
|   |   ├── hint.module.sass
|   |   ├── index.module.sass
|   |   ├── index.sass
|   |   ├── layout.module.sass
|   |   ├── link.module.sass
|   |   ├── reveal.css
|   |   ├── slides.module.sass
|   |   └── typography.module.sass
|   |   |
|   └── templates              
|   |   └── chapter.js
|   |   |
└── static               # This is where most of your media will live, be it for slides, or anything else. 
    ├── icon.png
    ├── icon_check.svg
    ├── icon_slides.svg
    ├── logo.svg
    ├── profile.jpg
    └── social.jpg
```

### System Requirements

This project is developed using Binder, Gatsby and md files.  
It runs on a MacOS system.

### Data Requirements

For the sake of reproducibility, public data files will be used.

### Key Goals

This project will teach about DS tools that can be helpful for ES research.