# Refactor code
# -------------
# Not timed (good to get it back within 24 hours)
#
# An intern has provided the code below to update the version number
# within two different files.
# The intern has left and you need to review and improve the code before
# submitting to source control.
#
# Please do not be constrained by the existing code (i.e. you don't have
# to keep the same function names, structure)
# Aim for production quality 'best-practice/clean' code
#

# Original Requirements
# ---------------------
# A script in a build process needs to update the build version number in 2
# locations.
# - The version number will be in an environment variable "BuildNum"
# - The files to be modified will be under "$SourcePath/develop/global/src"
# directory
# - The "SConstruct" file has a line "point=123," (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# - The "VERSION"file has a line "ADLMSDK_VERSION_POINT= 123" (where 123
# (just an example) should be updated with the value of "BuildNum"
# Environment variable)
# import os
# import re
# SCONSTRUCT file interesting lines
# config.version = Version(
# major=15,
# minor=0,
# point=6,
# patch=0
#)
# def updateSconstruct():
#     #Update the build number in the SConstruct file
#     first_file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct")
#     second_file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","SConstruct1")

#     os.chmod(first_file_path, 755)
#     fin = open(first_file_path, 'r')
#     fout = open(second_file_path, 'w')
#     for line in fin:
#         line=re.sub("point\=[\d]+","point="+os.environ["BuildNum"],line)
#         fout.write(line)
#     fin.close()
#     fout.close()
#     os.remove(first_file_path)
#     os.rename(second_file_path, first_file_path)

# # VERSION file interesting line
# # ADLMSDK_VERSION_POINT=6
# def updateVersion():
# #Update the build number in the VERSION file

#     #previous version
#     prev_version_file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION")

#     #new version
#     new_version_file_path = os.path.join(os.environ["SourcePath"],"develop","global","src","VERSION1")

#     #given permissions to read and write
#     os.chmod(prev_version_file_path, 755)
#     fin = open(prev_version_file_path, 'r')
#     fout = open(new_version_file_path, 'w')
#     for line in fin:
#         line=re.sub("ADLMSDK_VERSION_POINT=[\d]+","ADLMSDK_VERSION_POINT="+os.environ["BuildNum"],line)
#         fout.write(line)
#     fin.close()
#     fout.close()
#     os.remove(prev_version_file_path)
#     os.rename(new_version_file_path, 
#               prev_version_file_path)

# def main():
#     updateSconstruct()
#     updateVersion()

# main()

import os
import re

# Constants for regular expressions
SCONSTRUCT_REGEX = r"point=[\d]+"
VERSION_REGEX = r"ADLMSDK_VERSION_POINT=[\d]+"

def update_file(file_path, temp_file_path, regex, replacement):
    """
    Updates a file by replacing content matching a regex with a replacement string.

    Args:
        file_path (str): Path to the original file.
        temp_file_path (str): Path to the temporary file.
        regex (str): Regular expression to search for.
        replacement (str): Replacement string.
    """
    try:
        # Ensure the file is writable
        os.chmod(file_path, 0o755)
        
        # Open files using context managers
        with open(file_path, 'r') as fin, open(temp_file_path, 'w') as fout:
            for line in fin:
                # Replace matching content
                updated_line = re.sub(regex, replacement, line)
                fout.write(updated_line)
        
        # Replace the original file with the updated file
        os.remove(file_path)
        os.rename(temp_file_path, file_path)
    except Exception as e:
        print(f"Error updating file {file_path}: {e}")

def update_sconstruct():
    """
    Updates the build number in the SConstruct file.
    """
    base_path = os.environ.get("SourcePath")
    if not base_path:
        raise EnvironmentError("Environment variable 'SourcePath' is not set.")
    
    build_num = os.environ.get("BuildNum")
    if not build_num:
        raise EnvironmentError("Environment variable 'BuildNum' is not set.")
    
    first_file_path = os.path.join(base_path, "develop", "global", "src", "SConstruct")
    second_file_path = os.path.join(base_path, "develop", "global", "src", "SConstruct1")
    
    update_file(first_file_path, second_file_path, SCONSTRUCT_REGEX, f"point={build_num}")

def update_version():
    """
    Updates the build number in the VERSION file.
    """
    base_path = os.environ.get("SourcePath")
    if not base_path:
        raise EnvironmentError("Environment variable 'SourcePath' is not set.")
    
    build_num = os.environ.get("BuildNum")
    if not build_num:
        raise EnvironmentError("Environment variable 'BuildNum' is not set.")
    
    prev_version_file_path = os.path.join(base_path, "develop", "global", "src", "VERSION")
    new_version_file_path = os.path.join(base_path, "develop", "global", "src", "VERSION1")
    
    update_file(prev_version_file_path, new_version_file_path, VERSION_REGEX, f"ADLMSDK_VERSION_POINT={build_num}")

def main():
    """
    Main function to update the build number in the required files.
    """
    update_sconstruct()
    update_version()

if __name__ == "__main__":
    main()