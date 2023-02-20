<!-- Improved compatibility of back to top link: See: https://github.com/STASYA00/mini_gcp/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/STASYA00/mini_gcp">
    <img src="assets/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center" Mini GCP </h3>

  <p align="center">
    Save time during Data Science interviews!
    <br />
    <a href="https://github.com/STASYA00/mini_gcp">View Demo</a>
    ·
    <a href="https://github.com/STASYA00/mini_gcp/issues">Report Bug</a>
    ·
    <a href="https://github.com/STASYA00/mini_gcp/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#design">Design</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <ul>
        <li><a href="#challenges">Challenges</a></li>
        <li><a href="#futurework">Future work</a></li>
    </ul>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a framework (and base template) for data science technical interview tasks. Inspired by GCP structure and repeatedness of interview tasks.

### Intro

I'm sure that almost any person that went through data science interviews (and especially technical tasks) was surprised by the lack of creativity in the given questions. The technical tasks (unless there was someone who put his time and made a custom, company-adapted task for the applicants) are very trivial, require rewriting similar functions and reasoning. Most importantly, almost all are evaluating the candidate from the same point of view. \
This project was made during my interview with [Klarna](https://www.klarna.com/se/) to save time on the following interviews with similar tasks. The goal is to present a generic framework that would have most of the functions / recepts used in a common __basic__ task, make it __modular__, __extendable__, __reusable__ and __customizable__. \
Almost any data science project follows the standard pipeline: EDA -> Cleaning -> Feature Engineering -> Training -> Evaluation (cross) -> HP tuning -> Model Selection -> Training -> Deployment. Most of the cloud service providers made this pipeline and its orchestration automated and modular because of its repeatedness. I took inspiration from them and made a local framework to be used for common data science tasks. \
The main advantages here are:

* No need to rewrite the code 12931 times
* Missing pieces, additional feature engineering or cleaning recepts can be introduced in the framework
* The framework is modular, which shows software engineering skills of the applicant (so often missing in this field)
* Potentially gives an incentive to the managers and senior data scientists to put more time and effort into technical tasks.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [python](https://www.python.org/)
* [pandas](https://pandas.pydata.org/)
* [sklearn](https://scikit-learn.org/stable/)
* [Docker](https://docs.docker.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites


* Docker
  install [Docker](https://docs.docker.com/get-docker/)
* with conda or venv: create a new environment
```sh
conda create -n py3
```
```sh
conda activate py3
```

* to run with GPU install CUDA Toolkit and follow the instruction on configuring the environment
to run torch with CUDA
### Installation

* with Docker
  ```sh
  docker build . -t name:tag
  ```
  ```sh
  docker run -dit --name NAME name:tag
  ```
* alternatively
1. Clone the repo
   ```sh
   git clone https://github.com/STASYA00/mini_gcp.git
   ```
3. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. replace FILENAME, categorical columns and other parameters with your values
2. start with EDA.ipynb to understand which of the recepts and models fit your problem best; do some additional EDA if required
3. add the necessary recepts as children of ```Recept``` and models as children of ```Model```
4. combine all the ingridients in a child class of ```Experiment```, refer to ```BaseExperiment``` for an example
5. run the code:
```sh
python main.py
```
__The following steps will be automated in the future updates.__
6. Check your models' performance in ```log.csv```
7. Choose the best performing model and recept collection
8. Use this selection for the final model
9. Deploy the model

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DESIGN -->
## Design

The framework was designed to be reusable for most common cases, extendable (as we know, there is no one-fits-all solution), modular. It represents a typical data science pipeline: EDA -> Cleaning -> Feature Engineering -> Training -> Evaluation (cross) -> HP tuning -> Model Selection -> Training -> Deployment. The main extendable parts here are Cleaning + Feature Engineering, represented as ```Recept``` modules and training + evaluation + hp tuning, represented as ```Model``` modules. \
A UML of the framework will be added soon to provide more clarity.

<!-- ROADMAP -->
## Roadmap

### Challenges



### Future work

- [+] Add visualization notebook
- [ ] Add explanation notebook
- [ ] Add hyperparameter tuning module;
- [ ] Add logging of recepts as a separate table;
- [ ] Add different deployment methods;
- [ ] Add choosing the best model by result
- [ ] Add rebuilding model and recept by record from the log
- [ ] Add training on full dataset experiment
- [ ] Add prediction module (for the test set)

See the [open issues](https://github.com/STASYA00/mini_gcp/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Contact

Stasja - [@stasya00](https://stasyafedorova.wixsite.com/designautomation) - [e-mail](mailto:0.0stasya@gmail.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [GCP](https://cloud.google.com/)
* [My favorite README template](https://github.com/othneildrew/Best-README-Template)
* All the companies I had a DS interview at - inspiration!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/STASYA00/mini_gcp.svg?style=for-the-badge
[contributors-url]: https://github.com/STASYA00/mini_gcp/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/STASYA00/mini_gcp.svg?style=for-the-badge
[forks-url]: https://github.com/STASYA00/mini_gcp/network/members
[stars-shield]: https://img.shields.io/github/stars/STASYA00/mini_gcp.svg?style=for-the-badge
[stars-url]: https://github.com/STASYA00/mini_gcp/stargazers
[issues-shield]: https://img.shields.io/github/issues/STASYA00/mini_gcp.svg?style=for-the-badge
[issues-url]: https://github.com/STASYA00/mini_gcp/issues
[license-shield]: https://img.shields.io/github/license/STASYA00/mini_gcp.svg?style=for-the-badge
[license-url]: https://github.com/STASYA00/mini_gcp/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/stanislava-fedorova
[product-screenshot]: assets/screenshot.png




