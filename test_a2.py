from assessment_2 import updateSconstruct, updateVersion

import os
import tempfile
import shutil
import unittest
class TestBuildVersionUpdate(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        os.environ["SourcePath"] = self.test_dir
        os.environ["BuildNum"] = "42"

        # Create the develop/global/src directory structure
        self.src_dir = os.path.join(self.test_dir, "develop", "global", "src")
        os.makedirs(self.src_dir)

        # Create a sample SConstruct file
        self.sconstruct_path = os.path.join(self.src_dir, "SConstruct")
        with open(self.sconstruct_path, 'w') as f:
            f.write("config.version = Version(\n")
            f.write("major=15,\n")
            f.write("minor=0,\n")
            f.write("point=6,\n")
            f.write("patch=0\n")
            f.write(")\n")

        # Create a sample VERSION file
        self.version_path = os.path.join(self.src_dir, "VERSION")
        with open(self.version_path, 'w') as f:
            f.write("ADLMSDK_VERSION_POINT=6\n")

    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)

    def test_updateSconstruct(self):
        updateSconstruct()
        with open(self.sconstruct_path, 'r') as f:
            content = f.read()
        self.assertIn("point=42,", content)

    def test_updateVersion(self):
        updateVersion()
        with open(self.version_path, 'r') as f:
            content = f.read()
        self.assertIn("ADLMSDK_VERSION_POINT=42", content)
if __name__ == '__main__':
    unittest.main()
