
These are the scripts to run the Apache Spark course of Taming Big Data Sets with Apache Spark hands on

# Installation guide

This guide assumes Python is already installed on the system. The python version where the scripts where tested is Python 3.6.7

## For ubuntu 18.04 http://ubuntuhandbook.org/index.php/2018/05/install-oracle-java-jdk-8-10-ubuntu-18-04/

## Installation of JDK8

sudo add-apt-repository ppa:webupd8team/java

sudo apt-get install oracle-java8-installer

## Check installation

java -version

## This should be promted

java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)

## If java 8 not default

sudo apt-get install oracle-java8-set-default

## Uninstall Java 8

sudo apt-get remove --autoremove oracle-java8-installer oracle-java10-installer

## Install Apache Spark

wget https://www-us.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
tar -xzvf spark-2.4.0-bin-hadoop2.7.tgz
sudo mv spark-2.4.0-bin-hadoop2.7 /usr/local/spark

## Into ~/.bashrc add

export PATH=$PATH:/usr/local/spark/bin
source ~/.bashrc
To install 

# Data Sources

Most of the data files were provided by the course, however this are the links to other Datasets material needed

ml-100K movies:
- wget http://files.grouplens.org/datasets/movielens/ml-100k.zip

# Changes to the scripts from the original source material

- Since all scripts where written for Windows ("file///PATH") was replaced with (PATH)
- The name of the u.ITEM file in the ml-100K database changed and now goes by u.item
- popular-movies-nicer.py The encoding to open the u.item file needed to be specified ('iso-8859-15)

# Notes

- This repository does not contain any of the datasets for the course.
- Unlike the course all scripts were tested in the terminal by running:

```bash
python3 script.py
```

