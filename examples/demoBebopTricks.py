"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop
from pyparrot.Model import Model

bebop = Bebop(drone_type=Model.BEBOP)

print("connecting")
success = bebop.connect(10)
print(success)

print("sleeping")
bebop.smart_sleep(5)

bebop.ask_for_state_update()

bebop.safe_takeoff(10)

print("flip left")
print(f"flying state is {bebop.sensors.flying_state}")
success = bebop.flip(direction="left")
print(f"mambo flip result {success}")
bebop.smart_sleep(5)

print("flip right")
print(f"flying state is {bebop.sensors.flying_state}")
success = bebop.flip(direction="right")
print(f"mambo flip result {success}")
bebop.smart_sleep(5)

print("flip front")
print(f"flying state is {bebop.sensors.flying_state}")
success = bebop.flip(direction="front")
print(f"mambo flip result {success}")
bebop.smart_sleep(5)

print("flip back")
print(f"flying state is {bebop.sensors.flying_state}")
success = bebop.flip(direction="back")
print(f"mambo flip result {success}")
bebop.smart_sleep(5)

bebop.smart_sleep(5)
bebop.safe_land(10)

print("DONE - disconnecting")
bebop.disconnect()
