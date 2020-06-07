import vaex
import glob

path = "files/vx_files/*"
vx_list = []
for name in glob.glob(path):
    print(name)
    vx_t = vaex.open(name)
    cols = list(vx_t.columns)
    vx_list.append(vx_t[cols[:100]])
    print(str(name) + " read done")
    print(vx_t.shape)

print("reading done")
vx = vaex.concat(vx_list)
print(vx['col0'].mean())
print(vx.shape)
print("done")
