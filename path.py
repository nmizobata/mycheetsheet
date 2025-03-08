from pathlib import Path

p = Path(r"C:\Users\blues\Desktop")
oldPath = Path("c:hoge/hoge2/hoge3.txt")
newPath = oldPath.parent / "{}_new{}".format(oldPath.stem,oldPath.suffix)
newPath2 = oldPath.with_stem("{}_new".format(oldPath.stem))
print(newPath)
print(newPath2)

