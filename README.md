# Some basics on Computer Vision
# A note about the BoVW code
Most of the code is based on Adrian Rosebrock's tutorials/online course. His website is really useful to learn computer vision.

The ```Instructions``` file inside the ```bovw``` folder provides information and guidance about the process to extract the Bag of Visual Words.

# To install OpenCV
Check the tutorials on this website: https://www.pyimagesearch.com/opencv-tutorials-resources-guides/


# A note about CNN code
Most of the code was developed by Francisco Cantú  at the University of Houston. For a wonderful application of CNNs, check his paper: "The fingerprints of fraud: Evidence from Mexico's 1988 Presidental election" (Forthcoming in the APSR) [link of working paper: https://polmeth.polisci.wisc.edu/Papers/1988_1.pdf]


# To open the Jupyter notebook
1. Intall jupyter
2. Make sure to change the directory to the one that contains the notebook [in Terminal]
3. Type: ```jupyter notebook```
4. It will open a tab in  your browser. Click on the file with the notebook.

# To install imglab [program to  tag your images]
```wget http://dlib.net/files/dlib-19.16.tar.bz2
tar xvjf dlib-19.16.tar.bz2
cd dlib-19.16/tools/imglab
mkdir build
cd build
cmake ..
cmake --build . --config Release
sudo make install
```

# To use imglab
```
imglab -c <Name of the file storing your annotations>.xml <Folder where your images to be annotated are stored>
imglab <Name of the file storing your annotations>.xml
```
Press Shift to start drawing the boxes

