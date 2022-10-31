[![Tests][tests-shield]][tests-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

Python implementation for the Exploding Kittens board game
==========================================================


<summary>Table of Contents</summary>
<ol>
  <li><a href="#about-the-project">About The Project</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#tests">Tests</a></li>
  <li><a href="#roadmap">Roadmap</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>



## About The Project
`exploding_kittens` is a python library that implements and simulates the logic behind the Exploding Kittens card game. 


## Installation
Quick installation instructions (TBD):


Install a development version of this library by cloning the repository and running `flit`:
    
    $ git clone https://github.com/VasilisChrysanthou/ExplodingKittens.git
    $ cd ExplodingKittens
    $ python -m pip install flit
    $ python -m flit install --symlink


## Activate the conda environment (need to have conda installed)

    $ conda --env create -f environment.yml
    $ conda activate ExplodingKittEnv



## Usage
To play a game of Exploding Kittens, simply run the `play.py` script (TBD):

To import the library in a python environment run:

```python
import exploding_kittens as exp

team_size = 3
new_battle = pkm.Battle(team_size)
new_battle.start_battle()
```
Then run the script in your terminal:

    $ python my_script.py


## Tests
Run all tests developed by first installing and then running `tox` (TBD):

    $ python -m pip install tox
    $ python -m tox


## Roadmap
See the [open issues](https://github.com/VasilisChrysanthou/ExplodingKittens/issues) for a list of proposed features (and known issues).


## License
Distributed under the MIT License. See `LICENSE` for more information.


## Contributing
1. Fork the repository
2. Clone the forked repository
3. Create a new branch
4. Apply changes to the `exploding_kittens` library
5. Run tests and make sure they pass
6. Commit changes
7. Push changes to GitHub
8. Open PR on GitHub


## Contact
Vasilis Chrysanthou - chrysanthouv95@gmail.com

Michalis Panayides - michalis.pan1@hotmail.com

Project Link: [exploding_kittens](https://github.com/VasilisChrysanthou/ExplodingKittens)



<!-- MARKDOWN LINKS & IMAGES -->
[tests-shield]: https://img.shields.io/badge/Tests-passing-GREEN.svg
[tests-url]: https://github.com/VasilisChrysanthou/ExplodingKittens/actions
[issues-shield]: https://img.shields.io/github/issues/VasilisChrysanthou/ExplodingKittens.svg
[issues-url]: https://github.com/VasilisChrysanthou/ExplodingKittens/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg
[license-url]: https://github.com/VasilisChrysanthou/ExplodingKittens/blob/master/LICENSE.txt
