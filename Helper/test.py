import DataFormation as df
import DataCreate
data = DataCreate.Create(1,1,1,12,12,13,14,[12,14,15,15],[13,15,16,14])
df.Data().PacketJSON(data)
print(data)
