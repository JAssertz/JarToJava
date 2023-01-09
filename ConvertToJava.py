import os


def main():
   #Get the location of the jar that we want to convert to .java files
   sourceJar = input("Drag and drop the jar file here: ")
   locationOfLastSlashInSourceJar = sourceJar.rindex("\\")
   
   
   #Get the location of the jar that we want to convert to .java files
   print("\n"+ "If you don't have cfr you can download it here! https://www.benf.org/other/cfr/cfr-0.152.jar")
   cfrDecompilerLocation = input("Drag and drop the cfr decompiler jar: ")
   locationOfLastSlashInCfrJar = cfrDecompilerLocation.rindex("\\")
   
   
   pathPostExtract = jarToSource(sourceJar)
   convertClassToJava(pathPostExtract, cfrDecompilerLocation)
            
def jarToSource(jar):
   if not os.path.exists("src"):
      os.mkdir("src")
   os.chdir("src")
   os.system(f"cmd /c jar xf {jar}")
   return os.getcwd() + "\\"

def convertClassToJava(rootdir, cfrPath):
   print(rootdir)
   for subdir, dirs, files in os.walk(rootdir):
      for file in files:
         fileAsString = str(file)
         if file.endswith(".class"):
            os.system(f'cmd /c java -jar {cfrPath} {subdir}\\{file} --outputdir ./')
            os.remove(subdir + "\\" + file)
            print(os.path.join(subdir, file))
            
if __name__ == "__main__":
   main()
      
   
        