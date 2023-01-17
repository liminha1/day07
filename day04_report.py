# 8.1
e2f = {"dog" : "chien", "cat" : "chat", "walrus" : "morse"}
print(e2f)
# 8.2
print(e2f["walrus"])
# 8.3
f2e = list(e2f.items())
print(f2e)
f2e_mix = []
for i in range(0,3):
     f2e_mix.append(list(f2e[i]))
print(f2e_mix)
f2e_key = []
for i in range(0,3):
    f2e_key.append(f2e_mix[i][0])
print(f2e_key)
f2e_vel = []
for i in range(0,3):
    f2e_vel.append(f2e_mix[i][1])
print(f2e_vel)
f2e = {
    f2e_vel[0] : f2e_key[0],
    f2e_vel[1] : f2e_key[1],
    f2e_vel[2] : f2e_key[2],
}
print(f2e)
# 8.4
print(e2f["dog"])
# 8.5
print(', '.join(list(e2f.keys())))