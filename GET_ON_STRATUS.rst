=======================================
Getting started with CMAC2.0 on Stratus
=======================================

CMAC2.0 is a framework for doing corrections and retrievals on ARM radar data in
antenna coordinates. It runs under Python 3.x using Py-ART.

Step 0: Get an account on Stratus
---------------------------------
Need ADC input

Step 1: Install Anaconda Python locally
---------------------------------------
Grab Anaconda python by running:

wget https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh

change permissions

chmod +x Anaconda3-4.4.0-Linux-x86_64.sh

Execute

./Anaconda3-4.4.0-Linux-x86_64.sh

Press scroll through licence agreement, type yes to accept. Hit enter to install
to default location. type yes to update your path. **This will not take effect
until you log in and log out again**

Log out of stratus, back to the condo landing node and then log back into
stratus. Test your install by simply typing "python" you should get:

.. code_block:: python

  Python 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:09:58) 
  [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
  Type "help", "copyright", "credits" or "license" for more information.

Note that the version number includes anaconda so we are good to go!

finally update conda to the latest version with

conda update conda

Step 2: Install the conda environment for CMAC2.0
-------------------------------------------------
Go to your favourite directory for repositories.. I use ~/projects

clone the cmac2.0 repository

git clone https://github.com/EVS-ATMOS/cmac2.0

change directories into cmac2.0. Now you create your new fancy cmac_env
environment by typing:

conda env create -f environment.yml

This will take some time. 


