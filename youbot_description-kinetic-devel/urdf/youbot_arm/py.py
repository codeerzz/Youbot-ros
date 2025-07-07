from urdf_parser_py.urdf import URDF
from math import degrees
import pandas as pd

# URDF dosyasını yükle (önceden xacro ile üretilmiş youbot_arm.urdf)
robot = URDF.from_xml_file("youbot_arm.urdf")

# DH tablosu verilerini toplayacağımız liste
dh_params = []

# Sadece youBot kolundaki eklemleri al (5 eklem var: arm_joint_1 - arm_joint_5)
for i, joint in enumerate(robot.joints):
    if joint.type in ['revolute', 'continuous'] and "arm_joint" in joint.name:
        origin = joint.origin
        xyz = origin.xyz if origin else [0, 0, 0]
        rpy = origin.rpy if origin else [0, 0, 0]

        a_i = xyz[0]              # x ekseni boyunca (a)
        d_i = xyz[2]              # z ekseni boyunca (d)
        alpha_i = degrees(rpy[0]) # x ekseni etrafındaki açı (alpha), rad → derece
        theta_i = f"θ{i+1}"       # Z ekseni etrafında dönme (değişken)

        dh_params.append([i+1, round(a_i, 4), round(alpha_i, 1), round(d_i, 4), theta_i])

# DH tablosunu pandas ile yazdır
df = pd.DataFrame(dh_params, columns=["Link (i)", "aᵢ (m)", "αᵢ (°)", "dᵢ (m)", "θᵢ"])
print(df.to_string(index=False))

