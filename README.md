= Playground for Oracle ETL stuff =

= Setup =
1. create dir drivers/ and download and unzip Oracle Client normal and SDK packages into the drivers folder: drivers/libclntshcore.dylib.12.1
  * update env.sh to match the folder name of the drivers you downloaded
2. probably need to `ln -s` libclntsh.dylib.12.1 and libclntshcore.dylib.12.1 files into names that don't end in 12.1
3. pip install -r requirements.txt
