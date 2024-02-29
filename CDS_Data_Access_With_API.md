# CDS Data Access Guide

This document outlines the process of accessing climate data from the Copernicus Climate Data Store (CDS), inlcuding obtaining an API key, configure the local environment, and troubleshooting common issues.

## Table of Contents

- [Introduction](#introduction)
- [Setting up the environment](#setting-up-the-environment)
- [Obtaining and Configuring the API Key](#obtaining-and-configuring-the-api-key)
- [Installing the CDS API Client](#installing-the-cds-api-client)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
- [Accepting Terms and Conditions](#accepting-terms-and-conditions)

## Introduction

The Copernicus Climate Data Store offers a wealth of climate data. Accessing this data requires an API key, installation of the CDS API client, and acceptance of data usage terms and conditions.

## Setting up the environment

Ensure Python is installed and accessible. The `cdsapi` package requires Python and `pip` for installation.

Check Python installation:

```shell
python --version
```

Check pip installation:

```shell
pip --version
```

## Obtaining and Configuring the API Key

1. Register/Login to an account on the [CDS Website](https://cds.climate.copernicus.eu/)
2. Navigate to user profile to find the API key.
3. Create a `.cdsapirc` file **in home directory** with the following content:

```plaintext
url: https://cds.climate.copernicus.eu/api/v2
key: USER_ID:API_KEY
```

Replace USER_ID and API_KEY with the actual values.

## Installing the CDS API Client

Install the `cdsapi` package using `pip`:

```shell
pip install cdsapi
```

## Troubleshooting Common Issues

- API Key Not Recognized: Ensure the .cdsapirc file is correctly placed and formatted.
- Installation Issues: Verify Python and pip are correctly installed and accessible. Use virtual environments to avoid conflicts. (i.e., moved my .exe too far down the PATH)

## Accepting Terms and Conditions

Before accessing specific data sets, it is needed to accept terms and conditions, **as CDS processes the request, it takes time before getting access to the data set**:

1. Log into the CDS website.
2. Navigate to the data set of interest.
3. Read and accept the terms and conditions.

## Drink some water and have a snack while waiting for access

as title says.
