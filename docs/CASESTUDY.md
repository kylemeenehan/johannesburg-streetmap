# OpenStreetMap Data Case Study: Johannesburg

## Map Area

Johannesburg, South Africa

* [OpenStreetMap](https://www.openstreetmap.org/search?query=johannesburg#map=12/-26.2023/28.0436)
* [MapZen](https://mapzen.com/data/metro-extracts/metro/johannesburg_south-africa/) (Use this download to replicate results)

Johannesburg, South Africa, is where I was born and where I live now. I grew up in Hekpoort, but there aren't many streets there, so I've decided to take a look at the Jozi streets for this case study.

## Initial exploration

For the exploratory phase of this data extraction, I used a combination of example code and my own code to look through the data looking for innacuracies. I quickly discovered that passing the whole dataset through each function in series was inneficient, so I started to spread out the functions into classes that could process data by receiving a single element at a time from the main process. This process turned this:

