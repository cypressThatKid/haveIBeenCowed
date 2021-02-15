import os.path

if os.path.isfile('/tmp/bak'):
  print("[UH OH] Your machine has been exploited with DirtyCow! This means that someone had gained access to your system as a non-privledged user and gained root access with a kernel exploit. Please update your system to the latest version of your operating system.")
else:
  print ("[OK] Your system has not been exploited with DirtyCow")
