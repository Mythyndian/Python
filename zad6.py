import RocketEngine

# low power engines
small_engine_1 = RocketEngine.RocketEngine('low_power_engine_1', 50)
small_engine_2 = RocketEngine.RocketEngine('low_power_engine_2', 50)
print(small_engine_1)
print(small_engine_2)
small_engine_1.start()
small_engine_2.start()
print(small_engine_1)
print(small_engine_2)
print('------------------------------------------------')
# changing engine to higher power engine
small_engine_1.stop()
small_engine_2.stop()
# medium power engines
medium_engine_1 = RocketEngine.RocketEngine('medium_power_engine_1', 50)
medium_engine_2 = RocketEngine.RocketEngine('medium_power_engine_2', 50)
print(medium_engine_1)
print(medium_engine_2)
medium_engine_1.start()
medium_engine_2.start()
print(medium_engine_1)
print(medium_engine_2)
print('------------------------------------------------')
# changing engine to higher power engine
medium_engine_1.stop()
medium_engine_2.stop()
# high power engines
big_engine_1 = RocketEngine.RocketEngine('medium_power_engine_1', 50)
big_engine_2 = RocketEngine.RocketEngine('medium_power_engine_2', 50)
print(big_engine_1)
print(big_engine_2)
big_engine_1.start()
big_engine_2.start()
print(big_engine_1)
print(big_engine_2)
print('------------------------------------------------')
del big_engine_1, big_engine_2, medium_engine_1, medium_engine_2
