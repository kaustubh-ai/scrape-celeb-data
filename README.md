# Indian Celebrity Scraper and Crawler

### Table of Contents

- [Project Motivation](#motivation)
- [Project Components](#components)
  - [Spider](#encode_image)
  - [Download Images](#compare_face)
- [Usage](#usage)
- [Contribute](#contribute)

***

<a id='motivation'></a>

## 1. Project Motivation

Wish there was a project that automatically that downloads data and images about Indian celebrities automatically? Look no further 'cause here it is!

<a id='components'></a>

## 2. Project Components

There are two components in this project:

<a id='encode_image'></a>

### 2.1. Spider

File `celebs_insect.py` contains the code to crawl the web page using Scrapy's Spider. It does 2 things at once: scrapes the data and stores in a csv file for later use and also classifies the sentiments of the celebrities using `TextBlob`

<a id='compare_face'></a>

### 2.2. Download Images

Folder `celebs_images` contains the code to download images of the celebrities that have been scraped by the crawler. The files are also renamed using ImagePipeline and a custom built pipeline for convenience. 
<br>
This file also contains code that sends the proper signal to the arduino to switch on / switch off the motor based on the face recognition model's output.

***

<a name="usage"/>

## Usage

<a id='local'></a>

Run the file `celebs_insect.py` in the folders `spiders` by typing the following command in CLI<br>
* `scrapy crawl celebs_insect`
***

<a name="contribute"/>

## Contribute
1.  Fork the repository from Github
2.  Clone your fork

`git clone https://github.com/kaustubh-ai/scrape-celeb-data.git`

3.  Add the main repository as a remote

```git remote add upstream https://github.com/kaustubh-ai/scrape-celeb-data.git```

4.  Create a pull request!
