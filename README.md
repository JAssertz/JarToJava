###What does this do ?

This is a simple program that converts a .jar file back into .java files using the cfr decompiler and python to automate the process

###Requirements
The CFR Decompiler
   - https://www.benf.org/other/cfr/
The ability to use the jar command in cmd
   - If you don't have it use the following jdk download any version you want
   - https://adoptium.net/
Python
   - https://www.python.org/

###How to use
1. Open the script using python
2. Drag the jar that you want to source to into the cmd
3. Drag the cfr jar into the cmd the same way as the source jar
4. Wait until it isn't processing the jar anymore
5. Check the src dir for all the files within the jar all .class files are now .java files
