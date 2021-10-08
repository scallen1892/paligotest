# Replace {folder-name} with the output name from the .zip file generated by Paligo.
import shutil, os, glob

def moveAllFilesinDir(srcDir, dstDir):
# Check if both the are directories

    print('Moved files from unzipped directory to root...')
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
    # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '/*'):
        # Move each file to destination Directory
            shutil.move(filePath, dstDir);
    else:
        print("[ERROR!] Unable to move files.")

sourceDir = './{*.zip}/out'
destDir =  '.'

moveAllFilesinDir(sourceDir,destDir)

# Version 1 of unzip-util, see https://github.com/johnapaz/unzip-util for details.
