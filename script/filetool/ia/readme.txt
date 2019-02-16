
_____________________ Libmax _____________________

1. copylibmaxAtoC.py

  ConfigPath：Preference->Tools->ExternalTools

  Tool Setting:
    Program:           python
    Parameters:        libs/ihs/libMax/iatools/libmax/copylibmaxAtoC.py $ProjectFileDir$
    Working directory: $ProjectFileDir$

  功能:
    A区和C区文件在同一git节点时，将A区修改或新增的文件同步到C区。


2. deletelibmaxAwithC.py

  ConfigPath：Preference->Tools->ExternalTools

  Tool Setting:
    Program:           python
    Parameters:        libs/ihs/libMax/iatools/libmax/deletelibmaxAwithC.py $ProjectFileDir$ $FilePath$
    Working directory: $ProjectFileDir$

  功能：
    A区和C区文件在同一git节点时，鼠标右键选中A区文件执行autodeletelibmax，脚本删除该文件和其C区对应文件。
    选中A区文件夹则批量处理多文件。


3. copylibmaxCtoA.py

  ConfigPath：Preference->Tools->ExternalTools

  Tool Setting:
    Program:           python
    Parameters:        libs/ihs/libMax/iatools/libmax/copylibmaxCtoA.py $ProjectFileDir$
    Working directory: $ProjectFileDir$

  功能：
    A区文件没有被修改则更新A区文件。
    该脚本同build.gradle中libMaxStructureClosure闭包功能相同。
    C区文件是多module模式，脚本读取build.gradle文件并模式匹配"def libMaxClassConfig = []"字段，然后选择性拷贝module.


4. comparewithC.py

  Tool Setting:
    Program:           python
    Parameters:        libs/ihs/libMax/iatools/libmax/comparewithC.py $ProjectFileDir$ $FilePath$
    Working directory: $ProjectFileDir$

  功能：
    用Android Studio的比较工具比较A区和C区，B区和C区的文件或文件夹区别
    选中文件或文件夹，执行此工具

  配置：
  	Create Android Studio Command-line Launcher
    1. Open Android Studio
    2. Go to: Tools > Create Command-line Launcher
    3. Leave as default, Press OK
___________________________________________________